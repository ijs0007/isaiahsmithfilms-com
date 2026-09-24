import asyncio, os
from playwright.async_api import async_playwright
OUT="/mnt/user-data/outputs"
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page()
        await pg.goto("file:///home/claude/offer/offer.html")
        await pg.wait_for_timeout(500)
        await pg.pdf(path=os.path.join(OUT,"What I Can Set Up For Your Business.pdf"),
                     format="Letter", print_background=True, prefer_css_page_size=True)
        await b.close(); print("ok")
asyncio.run(main())
