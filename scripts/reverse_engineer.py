#!/usr/bin/env python3
"""
Reverse Engineering Engine — Library of Alexander
Clones, analyzes, and documents the architecture of popular AI projects.
"""

import os
import re
import json
import subprocess
import tempfile
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
RE_DIR = BASE_DIR / "23-reverse-engineering"
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(ex_ok=True)

# Top AI repos to reverse engineer
TARGET_REPOS = [
    # Agent frameworks
    "langchain-ai/langchain",
    "run-llama/llama_index",
    "crewAIInc/crewAI",
    "microsoft/autogen",
    "google/adk-python",
    "letta-ai/letta",
    "agno-agi/agno",
    "bytedance/deer-flow",
    "Significant-Gravitas/AutoGPT",
    # Image/Video
    "Stability-AI/generative-models",
    "CompVis/stable-diffusion",
    "comfyanonymous/ComfyUI",
    "Wan-Video/Wan2.1",
    "THUDM/CogVideoX",
    # Audio
    "openai/whisper",
    "FunAudioLLM/CosyVoice",
    "FunAudioLLM/F5-TTS",
    "suno-ai/bark",
    # Local LLMs
    "ggerganov/llama.cpp",
    "vllm-project/vllm",
    "oobabooga/text-generation-webui",
    # Chinese
    "deepseek-ai/DeepSeek-V3",
    "QwenLM/Qwen3",
    "THUDM/ChatGLM3",
    "OpenBMB/MiniCPM",
    "2noise/ChatTTS",
    # Tools
    "continuedev/continue",
    "Codium-ai/pr-agent",
    "open-webui/open-webui",
    "Mintplex-Labs/anything-llm",
]


def clone_repo(full_name, temp_dir):
    """Clone a repo to temp directory."""
    url = f"https://github.com/{full_name}.git"
    dest = Path(temp_dir) / full_name.replace("/", "_")
    try:
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", url, str(dest)],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode == 0:
            return dest
    except Exception as e:
        print(f"  Clone error: {e}")
    return None


def analyze_structure(repo_path):
    """Analyze the directory structure of a repo."""
    structure = {"files": [], "dirs": [], "languages": {}, "total_files": 0}

    try:
        for root, dirs, files in os.walk(repo_path):
            # Skip .git and node_modules
            dirs[:] = [d for d in dirs if d not in (".git", "node_modules", "__pycache__", ".venv", "venv")]
            for f in files:
                filepath = os.path.join(root, f)
                rel_path = os.path.relpath(filepath, repo_path)
                structure["files"].append(rel_path)
                structure["total_files"] += 1
                ext = os.path.splitext(f)[1]
                if ext:
                    structure["languages"][ext] = structure["languages"].get(ext, 0) + 1
            for d in dirs:
                structure["dirs"].append(os.path.relpath(os.path.join(root, d), repo_path))
    except Exception as e:
        print(f"  Structure error: {e}")

    return structure


def analyze_code_quality(repo_path):
    """Basic code quality metrics."""
    metrics = {
        "has_tests": False,
        "has_ci": False,
        "has_license": False,
        "has_docs": False,
        "has_security_policy": False,
        "has_contributing": False,
        "has_code_of_conduct": False,
        "has_readme": False,
        "readme_length": 0,
        "python_files": 0,
        "test_files": 0,
        "max_file_lines": 0,
        "avg_file_lines": 0,
        "has_type_hints": False,
        "has_docker": False,
        "has_makefile": False,
        "has_precommit": False,
        "dependencies": [],
    }

    try:
        # Check for key files
        metrics["has_license"] = any(
            (repo_path / f).exists() for f in ["LICENSE", "LICENSE.md", "LICENSE.txt", "LICENSE-MIT", "LICENSE-APACHE"]
        )
        metrics["has_contributing"] = any(
            (repo_path / f).exists() for f in ["CONTRIBUTING.md", "CONTRIBUTING.rst", "CONTRIBUTING"]
        )
        metrics["has_security_policy"] = any(
            (repo_path / f).exists() for f in ["SECURITY.md", "SECURITY.rst"]
        )
        metrics["has_code_of_conduct"] = any(
            (repo_path / f).exists() for f in ["CODE_OF_CONDUCT.md", "CODE_OF_CONDUCT"]
        )
        metrics["has_readme"] = any(
            (repo_path / f).exists() for f in ["README.md", "README.rst", "README"]
        )
        metrics["has_ci"] = any(
            (repo_path / d).exists() for d in [".github", ".circleci", ".travis.yml"]
        )
        metrics["has_docker"] = any(
            (repo_path / f).exists() for f in ["Dockerfile", "docker-compose.yml", "docker-compose.yaml"]
        )
        metrics["has_makefile"] = (repo_path / "Makefile").exists()
        metrics["has_precommit"] = any(
            (repo_path / f).exists() for f in [".pre-commit-config.yaml", ".pre-commit-config.yml"]
        )

        # Check for tests
        test_dirs = ["tests", "test", "__tests__", "spec", "specs"]
        metrics["has_tests"] = any((repo_path / d).exists() for d in test_dirs)

        # Check for docs
        doc_dirs = ["docs", "doc", "documentation", "wiki"]
        metrics["has_docs"] = any((repo_path / d).exists() for d in doc_dirs)

        # Analyze Python files
        python_lines = []
        test_files = 0
        has_type_hints = False
        for f in repo_path.rglob("*.py"):
            if ".git" in str(f) or "__pycache__" in str(f):
                continue
            try:
                content = f.read_text(errors="ignore")
                lines = len(content.splitlines())
                python_lines.append(lines)
                if "def " in content and "->" in content:
                    has_type_hints = True
                if "test_" in f.name or "_test.py" in f.name or "tests" in str(f.parent):
                    test_files += 1
            except:
                pass

        metrics["python_files"] = len(python_lines)
        metrics["test_files"] = test_files
        metrics["max_file_lines"] = max(python_lines) if python_lines else 0
        metrics["avg_file_lines"] = sum(python_lines) // len(python_lines) if python_lines else 0
        metrics["has_type_hints"] = has_type_hints

        # Get dependencies
        for dep_file in ["requirements.txt", "pyproject.toml", "setup.py", "setup.cfg", "Pipfile"]:
            dep_path = repo_path / dep_file
            if dep_path.exists():
                try:
                    content = dep_path.read_text(errors="ignore")
                    metrics["dependencies"].append({"file": dep_file, "content": content[:500]})
                except:
                    pass

        # README length
        for readme in ["README.md", "README.rst", "README"]:
            readme_path = repo_path / readme
            if readme_path.exists():
                try:
                    metrics["readme_length"] = len(readme_path.read_text(errors="ignore").splitlines())
                except:
                    pass
                break

    except Exception as e:
        print(f"  Quality error: {e}")

    return metrics


def extract_architecture(repo_path, full_name):
    """Extract architecture information from key source files."""
    arch = {
        "entry_points": [],
        "main_modules": [],
        "classes": [],
        "functions": [],
        "imports": [],
        "patterns": [],
    }

    try:
        # Find main Python modules
        for f in repo_path.rglob("*.py"):
            if ".git" in str(f) or "__pycache__" in str(f):
                continue
            try:
                content = f.read_text(errors="ignore")
                # Extract class definitions
                classes = re.findall(r'^class\s+(\w+)', content, re.MULTILINE)
                arch["classes"].extend(classes[:20])
                # Extract main functions
                funcs = re.findall(r'^def\s+(\w+)', content, re.MULTILINE)
                arch["functions"].extend(funcs[:20])
                # Extract imports
                imports = re.findall(r'^(?:from|import)\s+(\w+)', content, re.MULTILINE)
                arch["imports"].extend(imports[:30])
            except:
                pass

        # Deduplicate
        arch["classes"] = list(set(arch["classes"]))[:50]
        arch["functions"] = list(set(arch["functions"]))[:50]
        arch["imports"] = list(set(arch["imports"]))[:50]

        # Detect patterns
        all_content = ""
        for f in list(repo_path.rglob("*.py"))[:20]:
            try:
                all_content += f.read_text(errors="ignore")
            except:
                pass

        if "Agent" in all_content and "Tool" in all_content:
            arch["patterns"].append("Agent-Tool pattern")
        if "Chain" in all_content:
            arch["patterns"].append("Chain pattern")
        if "RAG" in all_content or "retrieval" in all_content.lower():
            arch["patterns"].append("RAG pattern")
        if "ReAct" in all_content or "Thought" in all_content:
            arch["patterns"].append("ReAct reasoning")
        if "MCP" in all_content or "Model Context Protocol" in all_content:
            arch["patterns"].append("MCP integration")
        if "async" in all_content and "await" in all_content:
            arch["patterns"].append("Async/await")
        if "pydantic" in all_content or "BaseModel" in all_content:
            arch["patterns"].append("Pydantic models")
        if "fastapi" in all_content or "Flask" in all_content:
            arch["patterns"].append("Web API")
        if "streamlit" in all_content or "gradio" in all_content:
            arch["patterns"].append("Web UI")

    except Exception as e:
        print(f"  Architecture error: {e}")

    return arch


def generate_report(full_name, structure, quality, arch):
    """Generate a markdown report for a reverse-engineered repo."""
    report = f"""# 🔬 Reverse Engineering: {full_name}

> Auto-generated analysis by Library of Alexander

## Overview

| Metric | Value |
|--------|-------|
| Total Files | {structure['total_files']} |
| Python Files | {quality['python_files']} |
| Test Files | {quality['test_files']} |
| Max File Lines | {quality['max_file_lines']} |
| Avg File Lines | {quality['avg_file_lines']} |
| README Length | {quality['readme_length']} lines |

## Quality Checklist

| Check | Status |
|-------|--------|
| License | {'✅' if quality['has_license'] else '❌'} |
| Tests | {'✅' if quality['has_tests'] else '❌'} |
| CI/CD | {'✅' if quality['has_ci'] else '❌'} |
| Documentation | {'✅' if quality['has_docs'] else '❌'} |
| Contributing Guide | {'✅' if quality['has_contributing'] else '❌'} |
| Security Policy | {'✅' if quality['has_security_policy'] else '❌'} |
| Docker | {'✅' if quality['has_docker'] else '❌'} |
| Makefile | {'✅' if quality['has_makefile'] else '❌'} |
| Pre-commit | {'✅' if quality['has_precommit'] else '❌'} |
| Type Hints | {'✅' if quality['has_type_hints'] else '❌'} |

## Architecture Patterns

{chr(10).join(f'- {p}' for p in arch['patterns']) if arch['patterns'] else 'No patterns detected'}

## Key Classes

{chr(10).join(f'- `{c}`' for c in arch['classes'][:20]) if arch['classes'] else 'None detected'}

## Key Functions

{chr(10).join(f'- `{f}`' for f in arch['functions'][:20]) if arch['functions'] else 'None detected'}

## Top Imports

{chr(10).join(f'- `{i}`' for i in arch['imports'][:20]) if arch['imports'] else 'None detected'}

## Language Breakdown

| Extension | Count |
|-----------|-------|
{chr(10).join(f'| {ext} | {count} |' for ext, count in sorted(structure['languages'].items(), key=lambda x: x[1], reverse=True)[:15])}

## Verdict

"""

    # Generate verdict
    score = 0
    if quality["has_license"]: score += 1
    if quality["has_tests"]: score += 2
    if quality["has_ci"]: score += 1
    if quality["has_docs"]: score += 1
    if quality["has_type_hints"]: score += 1
    if quality["has_docker"]: score += 1
    if quality["max_file_lines"] < 500: score += 1
    if quality["test_files"] > 5: score += 2
    if quality["readme_length"] > 100: score += 1

    if score >= 8:
        report += "**🟢 High Quality** — Well-structured, tested, and documented. Good reference.\n"
    elif score >= 5:
        report += "**🟡 Medium Quality** — Functional but has gaps. Use with caution.\n"
    else:
        report += "**🔴 Low Quality** — Likely vibe-coded. Missing tests, docs, or license. Avoid or fork and fix.\n"

    report += f"\n**Quality Score:** {score}/10\n"
    report += f"\n---\n*Generated: {datetime.utcnow().isoformat()} UTC*\n"

    return report


def main():
    print(f"🔬 Library of Alexander — Reverse Engineering Engine")
    print(f"Time: {datetime.utcnow().isoformat()} UTC")
    print(f"Targets: {len(TARGET_REPOS)} repos")
    print()

    results = []

    with tempfile.TemporaryDirectory() as temp_dir:
        for full_name in TARGET_REPOS:
            print(f"\n=== Analyzing {full_name} ===")

            # Clone
            repo_path = clone_repo(full_name, temp_dir)
            if not repo_path:
                print(f"  ❌ Failed to clone {full_name}")
                continue

            # Analyze
            structure = analyze_structure(repo_path)
            quality = analyze_code_quality(repo_path)
            arch = extract_architecture(repo_path, full_name)

            # Generate report
            report = generate_report(full_name, structure, quality, arch)

            # Save report
            safe_name = full_name.replace("/", "_")
            report_path = RE_DIR / f"RE_{safe_name}.md"
            report_path.write_text(report)
            print(f"  ✅ Report saved: {report_path.name}")

            results.append({
                "repo": full_name,
                "quality_score": sum([
                    1 if quality["has_license"] else 0,
                    2 if quality["has_tests"] else 0,
                    1 if quality["has_ci"] else 0,
                    1 if quality["has_docs"] else 0,
                    1 if quality["has_type_hints"] else 0,
                    1 if quality["has_docker"] else 0,
                    1 if quality["max_file_lines"] < 500 else 0,
                    2 if quality["test_files"] > 5 else 0,
                    1 if quality["readme_length"] > 100 else 0,
                ]),
                "patterns": arch["patterns"],
            })

    # Save summary
    summary = {
        "timestamp": datetime.utcnow().isoformat(),
        "results": results,
    }
    with open(DATA_DIR / "re_results.json", "w") as f:
        json.dump(summary, f, indent=2)

    # Generate summary report
    summary_md = f"# 🔬 Reverse Engineering Summary\n\n"
    summary_md += f"Generated: {datetime.utcnow().isoformat()} UTC\n\n"
    summary_md += "## Quality Rankings\n\n"
    summary_md += "| Repo | Score | Verdict |\n"
    summary_md += "|------|-------|---------|\n"
    for r in sorted(results, key=lambda x: x["quality_score"], reverse=True):
        verdict = "🟢" if r["quality_score"] >= 8 else "🟡" if r["quality_score"] >= 5 else "🔴"
        summary_md += f"| {r['repo']} | {r['quality_score']}/10 | {verdict} |\n"

    (RE_DIR / "SUMMARY.md").write_text(summary_md)
    print(f"\n✅ Reverse engineering complete. {len(results)} repos analyzed.")


if __name__ == "__main__":
    main()
