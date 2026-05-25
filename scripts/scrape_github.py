#!/usr/bin/env python3
"""
GitHub AI Repo Scraper — Library of Alexander
Continuously scrapes GitHub for new AI projects, models, and tools.
"""

import os
import json
import time
import re
from datetime import datetime, timedelta
from pathlib import Path

try:
    from github import Github, GithubException
except ImportError:
    print("PyGithub not installed, using curl fallback")
    Github = None

BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Search queries for different categories
SEARCH_QUERIES = {
    "llm": "language model LLM AI stars:>100",
    "image_gen": "image generation diffusion stars:>100",
    "video_gen": "video generation stars:>100",
    "audio": "text to speech TTS audio AI stars:>100",
    "agent": "AI agent autonomous stars:>100",
    "rag": "RAG retrieval augmented generation stars:>100",
    "coding": "AI coding assistant copilot stars:>100",
    "chinese": "chinese AI 中文 stars:>50",
    "local_llm": "local LLM inference stars:>100",
    "fine_tuning": "fine-tuning LLM stars:>100",
    "embedding": "embedding model stars:>100",
    "multimodal": "multimodal vision language stars:>100",
    "robotics": "robotics AI stars:>50",
    "edge_ai": "edge AI embedded stars:>50",
    "mcp": "MCP model context protocol stars:>50",
}

# Chinese AI orgs to monitor
CHINESE_ORGS = [
    "deepseek-ai", "QwenLM", "THUDM", "InternLM", "01-ai",
    "MoonshotAI", "MiniMax-AI", "FunAudioLLM", "OpenBMB",
    "FlagOpen", "PaddlePaddle", "baichuan-inc", "modelscope",
    "TencentARC", "Kwai-Kolors", "Wan-Video", "OpenGVLab",
    "IDEA-CCNL", "netease-youdao", "stepfun-ai",
]

# Major AI orgs to monitor
MAJOR_ORGS = [
    "openai", "anthropic", "google", "google-deepmind", "meta-llama",
    "microsoft", "huggingface", "stability-ai", "vllm-project",
    "langchain-ai", "run-llama", "crewAIInc", "Significant-Gravitas",
    "oobabooga", "ggerganov", "comfyanonymous", "lllyasviel",
    "Stability-AI", "CompVis", "diffusers-community",
]


def scrape_with_curl(query, sort="stars", order="desc", per_page=30):
    """Fallback scraper using curl + GitHub search page HTML."""
    import subprocess
    url = f"https://github.com/search?q={query.replace(' ', '+')}&s={sort}&o={order}&type=repositories"
    try:
        result = subprocess.run(
            ["curl", "-sL", url],
            capture_output=True, text=True, timeout=30
        )
        # Extract repo names from HTML
        repos = re.findall(r'href="/([^/]+/[^/]+)"[^>]*>', result.stdout)
        return list(set(repos))[:per_page]
    except Exception as e:
        print(f"Curl scrape error: {e}")
        return []


def scrape_org_repos(org_name, token=None):
    """Scrape all repos from a GitHub org."""
    repos = []
    if Github and token:
        try:
            g = Github(token)
            org = g.get_organization(org_name)
            for repo in org.get_repos(sort="updated", direction="desc"):
                repos.append({
                    "full_name": repo.full_name,
                    "description": repo.description or "",
                    "url": repo.html_url,
                    "language": repo.language,
                    "stars": repo.stargazers_count,
                    "forks": repo.forks_count,
                    "updated": repo.updated_at.isoformat() if repo.updated_at else "",
                    "created": repo.created_at.isoformat() if repo.created_at else "",
                    "topics": repo.get_topics(),
                    "license": repo.license.spdx_id if repo.license else None,
                })
        except Exception as e:
            print(f"Error scraping {org_name}: {e}")
    else:
        # Use curl fallback
        import subprocess
        url = f"https://api.github.com/orgs/{org_name}/repos?per_page=100&sort=updated&direction=desc"
        try:
            result = subprocess.run(
                ["curl", "-sL", url],
                capture_output=True, text=True, timeout=30
            )
            data = json.loads(result.stdout)
            if isinstance(data, list):
                for repo in data:
                    repos.append({
                        "full_name": repo.get("full_name", ""),
                        "description": repo.get("description", "") or "",
                        "url": repo.get("html_url", ""),
                        "language": repo.get("language"),
                        "stars": repo.get("stargazers_count", 0),
                        "forks": repo.get("forks_count", 0),
                        "updated": repo.get("updated_at", ""),
                        "created": repo.get("created_at", ""),
                        "topics": repo.get("topics", []),
                        "license": repo.get("license", {}).get("spdx_id") if repo.get("license") else None,
                    })
        except Exception as e:
            print(f"Curl error for {org_name}: {e}")
    return repos


def search_github(query, token=None, per_page=30):
    """Search GitHub for repos matching query."""
    repos = []
    if Github and token:
        try:
            g = Github(token)
            results = g.search_repositories(query, sort="stars", order="desc")
            for repo in results[:per_page]:
                repos.append({
                    "full_name": repo.full_name,
                    "description": repo.description or "",
                    "url": repo.html_url,
                    "language": repo.language,
                    "stars": repo.stargazers_count,
                    "forks": repo.forks_count,
                    "updated": repo.updated_at.isoformat() if repo.updated_at else "",
                    "topics": repo.get_topics(),
                    "license": repo.license.spdx_id if repo.license else None,
                })
        except Exception as e:
            print(f"Search error: {e}")
    return repos


def update_category_file(category, repos):
    """Update a category markdown file with new repos."""
    cat_dir = BASE_DIR / category
    if not cat_dir.exists():
        return

    # Find the main .md file
    md_files = list(cat_dir.glob("*.md"))
    if not md_files:
        return

    target = md_files[0]

    # Read existing content
    existing = target.read_text() if target.exists() else ""

    # Check which repos are already listed
    existing_names = set(re.findall(r'\[([^\]]+)\]\(https://github\.com/[^)]+\)', existing))

    new_repos = [r for r in repos if r["full_name"] not in existing_names]

    if not new_repos:
        print(f"No new repos for {category}")
        return

    # Append new repos
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    section = f"\n\n## 🆕 Auto-discovered ({timestamp})\n\n"
    section += "| Repo | Stars | Language | Description |\n"
    section += "|------|-------|----------|-------------|\n"

    for repo in sorted(new_repos, key=lambda x: x.get("stars", 0), reverse=True):
        name = repo["full_name"]
        url = repo.get("url", f"https://github.com/{name}")
        stars = repo.get("stars", 0)
        lang = repo.get("language", "?")
        desc = (repo.get("description", "") or "")[:80]
        section += f"| [{name}]({url}) | ⭐{stars} | {lang} | {desc} |\n"

    # Append to file
    with open(target, "a") as f:
        f.write(section)

    print(f"Added {len(new_repos)} new repos to {category}")


def main():
    token = os.environ.get("GITHUB_TOKEN")
    print(f"🔍 Library of Alexander — GitHub Scraper")
    print(f"Time: {datetime.utcnow().isoformat()} UTC")
    print(f"Token: {'Yes' if token else 'No (rate limited)'}")
    print()

    # 1. Scrape Chinese AI orgs
    print("=== Scanning Chinese AI orgs ===")
    all_chinese = []
    for org in CHINESE_ORGS:
        repos = scrape_org_repos(org, token)
        all_chinese.extend(repos)
        print(f"  {org}: {len(repos)} repos")
        time.sleep(1)

    update_category_file("21-chinese-ai-ecosystem", all_chinese)

    # 2. Scrape major AI orgs
    print("\n=== Scanning major AI orgs ===")
    all_major = []
    for org in MAJOR_ORGS:
        repos = scrape_org_repos(org, token)
        all_major.extend(repos)
        print(f"  {org}: {len(repos)} repos")
        time.sleep(1)

    # 3. Search for trending categories
    print("\n=== Searching trending categories ===")
    for category, query in SEARCH_QUERIES.items():
        repos = search_github(query, token, per_page=20)
        print(f"  {category}: {len(repos)} repos found")
        update_category_file(f"01-ai-models" if "llm" in category else f"02-free-apis", repos)
        time.sleep(2)

    # 4. Save raw data
    raw_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "chinese_repos": all_chinese,
        "major_repos": all_major,
    }
    with open(DATA_DIR / "latest_scrape.json", "w") as f:
        json.dump(raw_data, f, indent=2)

    print(f"\n✅ Scrape complete. Data saved to {DATA_DIR}/latest_scrape.json")


if __name__ == "__main__":
    main()
