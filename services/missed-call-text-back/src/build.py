import asyncio, os
from playwright.async_api import async_playwright
OUT="/mnt/user-data/outputs"
os.makedirs(OUT, exist_ok=True)
JOBS=[("customer.html","Missed-Call Text-Back - For Clients.pdf"),
      ("internal.html","Missed-Call Text-Back - Internal Runbook.pdf")]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page()
        for src,dst in JOBS:
            await pg.goto("file:///home/claude/textback/"+src)
            await pg.wait_for_timeout(500)
            await pg.pdf(path=os.path.join(OUT,dst), format="Letter",
                         print_background=True, prefer_css_page_size=True)
            print("ok", dst)
        await b.close()
asyncio.run(main())
