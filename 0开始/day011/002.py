import asyncio
import time

from pyppeteer import launch


async def main():
    browser = await launch({"headless": False})
    page = await browser.newPage()
    await page.goto('https://www.baidu.com')

    time.sleep(5)

    await browser.close()


asyncio.get_event_loop().run_until_complete(main())