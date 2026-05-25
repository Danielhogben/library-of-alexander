#!/bin/bash
# Library of Alexander — Continuous Scraper
# Runs every 4 hours via cron

set -e
cd /home/donn/repos/library-of-alexander

echo "=== Library of Alexander Scraper ==="
echo "Time: $(date -u +%Y-%m-%dT%H:%M:%S) UTC"

# 1. Scrape GitHub for new repos
echo "--- Scraping GitHub ---"
python3 scripts/scrape_github.py 2>&1 | tail -20

# 2. Run reverse engineering on new repos
echo "--- Reverse Engineering ---"
python3 scripts/reverse_engineer.py 2>&1 | tail -20

# 3. Commit and push
echo "--- Committing ---"
git add -A
CHANGES=$(git diff --cached --stat | tail -1)
if [ -n "$CHANGES" ]; then
    git commit -m "🔄 Auto-scrape: $(date -u +%Y-%m-%d-%H:%M) UTC"
    git push origin main 2>&1 | tail -3
    echo "✅ Pushed: $CHANGES"
else
    echo "No changes to commit"
fi

echo "=== Done ==="
