import asyncio
from pyppeteer import launch

# 要设置显示内容的宽度、高度
width, height = 1366, 768


async def main():
    browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://www.baidu.com')
    await asyncio.sleep(100)


asyncio.get_event_loop().run_until_complete(main())