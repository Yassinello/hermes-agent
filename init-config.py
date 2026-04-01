import pathlib, os

# 1. Write config.yaml
p = pathlib.Path('/opt/data/config.yaml')
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

# 2. Dump ALL env vars to .env so Hermes can read them
e = pathlib.Path('/opt/data/.env')
lines = []
for k, v in os.environ.items():
    if k.startswith('_') or k in ('PATH', 'HOME', 'PWD', 'SHLVL', 'HOSTNAME'):
        continue
    lines.append(f'{k}={v}')
e.write_text('\n'.join(sorted(lines)) + '\n')

print(f"Config written + {len(lines)} env vars dumped to .env")
