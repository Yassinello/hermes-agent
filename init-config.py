import pathlib, os

p = pathlib.Path('/opt/data/config.yaml')
if not p.exists():
    p.write_text("""model:
  provider: openrouter
  default: google/gemini-2.5-flash
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
  composio:
    url: "https://connect.composio.dev/mcp"
    config:
      headers:
        x-consumer-api-key: "${COMPOSIO_API_KEY}"  
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
  yass-mcp:
    url: "https://mcp-yass.vercel.app/api/mcp?token=yass_mcp_prod_2026"
""")
    print("Config created (first run)")
else:
    print("Config exists, skipping")

# Always dump env vars to .env
e = pathlib.Path('/opt/data/.env')
lines = []
for k, v in os.environ.items():
    if k.startswith('_') or k in ('PATH', 'HOME', 'PWD', 'SHLVL', 'HOSTNAME'):
        continue
    lines.append(f'{k}={v}')
e.write_text('\n'.join(sorted(lines)) + '\n')
print(f"{len(lines)} env vars dumped to .env")
