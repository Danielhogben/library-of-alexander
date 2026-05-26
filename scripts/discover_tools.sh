#!/usr/bin/env bash
# Global AI Tool Discovery Pipeline
# Runs every 4 hours, discovers tools from ALL countries and languages

set -euo pipefail

LIBRARY_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TIMESTAMP=$(date +%Y%m%d_%H%M)
LOG_FILE="$LIBRARY_DIR/data/discovery_${TIMESTAMP}.log"

log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"; }

# Global search queries - every language, every region
declare -A CATEGORY_MAP

# English queries
CATEGORY_MAP["ai agent framework"]="08-ai-agents"
CATEGORY_MAP["mcp server"]="08-ai-agents"
CATEGORY_MAP["local llm inference"]="10-local-llms"
CATEGORY_MAP["text to speech ai"]="07-voice-tts"
CATEGORY_MAP["image generation ai"]="04-image-generation"
CATEGORY_MAP["rag knowledge base"]="09-rag-knowledge"
CATEGORY_MAP["vector database"]="09-rag-knowledge"
CATEGORY_MAP["ai coding assistant"]="03-coding-tools"
CATEGORY_MAP["llm router"]="10-local-llms"
CATEGORY_MAP["ai workflow automation"]="08-ai-agents"
CATEGORY_MAP["model serving"]="14-devops-mlops"
CATEGORY_MAP["ai monitoring"]="14-devops-mlops"
CATEGORY_MAP["prompt engineering"]="12-learning"
CATEGORY_MAP["fine tuning llm"]="13-frameworks"
CATEGORY_MAP["ai evaluation"]="18-benchmarks"
CATEGORY_MAP["ai security"]="22-vibe-code-audit"
CATEGORY_MAP["ai red team"]="22-vibe-code-audit"
CATEGORY_MAP["ai benchmark"]="18-benchmarks"
CATEGORY_MAP["ai dataset"]="17-datasets"
CATEGORY_MAP["ai robotics"]="15-robotics-edge"
CATEGORY_MAP["embedded ai"]="24-esp-embedded-ai"
CATEGORY_MAP["tinyml"]="24-esp-embedded-ai"
CATEGORY_MAP["edge ai"]="24-esp-embedded-ai"
CATEGORY_MAP["ai voice clone"]="07-voice-tts"
CATEGORY_MAP["ai music generation"]="06-audio-music"
CATEGORY_MAP["ai video generation"]="05-video-generation"
CATEGORY_MAP["ai chatbot framework"]="08-ai-agents"
CATEGORY_MAP["ai memory"]="09-rag-knowledge"
CATEGORY_MAP["ai planning"]="08-ai-agents"
CATEGORY_MAP["ai tool use"]="08-ai-agents"

# Chinese queries
CATEGORY_MAP["AI 人工智能"]="21-chinese-ai-ecosystem"
CATEGORY_MAP["大语言模型"]="21-chinese-ai-ecosystem"
CATEGORY_MAP["机器学习"]="21-chinese-ai-ecosystem"
CATEGORY_MAP["智能体"]="08-ai-agents"
CATEGORY_MAP["语音合成"]="07-voice-tts"
CATEGORY_MAP["图像生成"]="04-image-generation"

# Turkish queries
CATEGORY_MAP["yapay zeka"]="12-learning"
CATEGORY_MAP["derin öğrenme"]="12-learning"
CATEGORY_MAP["makine öğrenmesi"]="12-learning"

# Spanish queries
CATEGORY_MAP["inteligencia artificial"]="12-learning"
CATEGORY_MAP["aprendizaje automático"]="12-learning"

# Portuguese queries
CATEGORY_MAP["inteligência artificial"]="12-learning"
CATEGORY_MAP["aprendizado de máquina"]="12-learning"

# Arabic queries
CATEGORY_MAP["الذكاء الاصطناعي"]="12-learning"
CATEGORY_MAP["تعلم الآلة"]="12-learning"

# Japanese queries
CATEGORY_MAP["AI 機械学習"]="12-learning"
CATEGORY_MAP["深層学習"]="12-learning"

# French queries
CATEGORY_MAP["intelligence artificielle"]="12-learning"
CATEGORY_MAP["apprentissage automatique"]="12-learning"

# Russian queries
CATEGORY_MAP["искусственный интеллект"]="12-learning"
CATEGORY_MAP["машинное обучение"]="12-learning"

# Hindi/Indian queries
CATEGORY_MAP["AI India"]="12-learning"
CATEGORY_MAP["bharat AI"]="12-learning"

# Vietnamese queries
CATEGORY_MAP["trí tuệ nhân tạo"]="12-learning"
CATEGORY_MAP["học máy"]="12-learning"

# Korean queries
CATEGORY_MAP["AI 한국어"]="12-learning"
CATEGORY_MAP["인공지능"]="12-learning"

log "Starting GLOBAL tool discovery pipeline"
NEW_TOOLS=0
SEARCHES_RUN=0

for search in "${!CATEGORY_MAP[@]}"; do
  category="${CATEGORY_MAP[$search]}"
  log "Searching: $search → $category"
  
  # Search GitHub
  results=$(gh search repos "$search" --sort stars --order desc --limit 20 --json name,fullName,description,stargazersCount,updatedAt,language 2>/dev/null || echo "[]")
  SEARCHES_RUN=$((SEARCHES_RUN + 1))
  
  # Process results
  echo "$results" | python3 -c "
import json, sys, os, re

results = json.load(sys.stdin)
category = '$category'
library_dir = '$LIBRARY_DIR'
readme_path = os.path.join(library_dir, category, 'README.md')

# Load existing tools
existing = set()
if os.path.exists(readme_path):
    with open(readme_path) as f:
        for line in f:
            if '|' in line and 'github.com' in line:
                parts = line.split('|')
                for p in parts:
                    if 'github.com' in p:
                        match = re.search(r'github\.com/([^/\)]+/[^/\)\s]+)', p)
                        if match:
                            existing.add(match.group(1).lower())

new_count = 0
new_entries = []
for r in results:
    full_name = r.get('fullName', '').lower()
    if full_name in existing:
        continue
    if r.get('stargazersCount', 0) < 30:
        continue
    name = r.get('name', '')
    desc = (r.get('description', '') or '')[:120]
    stars = r.get('stargazersCount', 0)
    lang = r.get('language', '')
    updated = r.get('updatedAt', '')[:10]
    url = f'https://github.com/{r[\"fullName\"]}'
    
    entry = f'| [{name}]({url}) | {desc} | ⭐{stars} | {lang} | {updated} |'
    new_entries.append(entry)
    new_count += 1

if new_count > 0:
    # Create README if it doesn't exist
    if not os.path.exists(readme_path):
        os.makedirs(os.path.dirname(readme_path), exist_ok=True)
        with open(readme_path, 'w') as f:
            f.write(f'# {category}\n\n| Tool | Description | Stars | Language | Updated |\n')
            f.write('|------|-------------|-------|----------|---------|\n')
    
    with open(readme_path, 'a') as f:
        for entry in new_entries:
            f.write(entry + '\n')
    print(f'ADDED:{new_count}:{category}')
else:
    print('NONE')
" 2>/dev/null | while IFS=: read -r action count cat; do
    if [[ "$action" == "ADDED" ]]; then
      log "Added $count new tools to $cat"
      NEW_TOOLS=$((NEW_TOOLS + count))
    fi
  done
done

log "Discovery complete. Searches run: $SEARCHES_RUN. New tools found: $NEW_TOOLS"

# Commit if changes
cd "$LIBRARY_DIR"
if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -m "global-discover: auto-added $NEW_TOOLS new tools from $SEARCHES_RUN global searches"
  git push origin main 2>/dev/null || true
  git push thoughtforge main 2>/dev/null || true
  log "Committed and pushed to both repos"
else
  log "No changes to commit"
fi

# Save run metadata
cat > "$LIBRARY_DIR/data/latest_discovery.json" << METAEOF
{
  "timestamp": "$(date -Iseconds)",
  "new_tools": $NEW_TOOLS,
  "searches_run": $SEARCHES_RUN,
  "languages": ["English", "Chinese", "Turkish", "Spanish", "Portuguese", "Arabic", "Japanese", "French", "Russian", "Hindi", "Vietnamese", "Korean"],
  "log_file": "$LOG_FILE"
}
METAEOF

log "Global pipeline finished"
