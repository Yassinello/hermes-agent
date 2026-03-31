import os, pathlib
p = pathlib.Path('/opt/data/config.yaml')
if not p.exists():
    p.write_text("""model:
  provider: openrouter
  default: google/gemini-2.5-flash-preview
memory:
  memory_enabled: true
  user_profile_enabled: true
terminal:
  backend: local
  timeout: 180
compression:
  enabled: true
  threshold: 0.50
approvals:
  mode: smart
display:
  tool_progress: off
TELEGRAM_HOME_CHANNEL: '6461243820'
mcp_servers:
  github:
    command: npx
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "${GITHUB_PAT}"
  apify:
    command: npx
    args: ["-y", "@apify/actors-mcp-server", "--actors", "docs,supreme_coder/linkedin-post,harvestapi/linkedin-profile-scraper,harvestapi/linkedin-company,bestscrapers/linkedin-company-insights-scraper,harvestapi/linkedin-profile-posts,harvestapi/linkedin-company-posts"]
    env:
      APIFY_TOKEN: "${APIFY_TOKEN}"
""")
    print("Config created")
else:
    print("Config exists, skipping")
```

Puis le **Custom Start Command** devient simplement :
```
bash -c "python3 init-config.py && /opt/hermes/docker/entrypoint.sh gateway"
