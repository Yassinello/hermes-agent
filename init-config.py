import pathlib, os, stat

p = pathlib.Path('/opt/data/config.yaml')
p.write_text("""model:
  provider: openrouter
  default: qwen/qwen3.6-plus:free
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
  yass-mcp:
    url: "https://mcp-yass.vercel.app/api/mcp?token=${YASS_MCP_TOKEN}"
  composio:
    command: npx
    args: ["-y", "@composio/mcp", "start"]
    env:
      COMPOSIO_API_KEY: "${COMPOSIO_API_KEY}"
""")
os.chmod(str(p), stat.S_IRUSR | stat.S_IRGRP | stat.S_IROTH)

e = pathlib.Path('/opt/data/.env')
lines = []
for k, v in os.environ.items():
    if k.startswith('_') or k in ('PATH', 'HOME', 'PWD', 'SHLVL', 'HOSTNAME'):
        continue
    lines.append(f'{k}={v}')
e.write_text('\n'.join(sorted(lines)) + '\n')

print(f"Config written (read-only) + {len(lines)} env vars dumped")
