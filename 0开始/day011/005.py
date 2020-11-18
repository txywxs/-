import asyncio
import os
import random
import sys
from PIL import Image
from pyppeteer import launch

sys.path.append(os.getcwd() + "./chaojiying_Python")
from chaojiying import Chaojiying_Client

width, height = 1366, 768


def input_time_random():
    return random.randint(100, 151)


async def main():
    browser = await launch(headless=False, args=['--disable-infobars', f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://kyfw.12306.cn/otn/resources/login.html')
    await asyncio.sleep(3)
    await page.click('.login-hd-account')
    await page.type('#J-userName', '123123', {'delay': input_time_random()})
    await page.type('#J-password', '123123', {'delay': input_time_random()})
    # 一些网站主要通过 window.navigator.webdriver 来对 webdriver 进行检测，所以我们只需要使用 JavaScript 将它设置为 false 即可
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    yazhengma = await page.waitForSelector('#J-loginImg')  # 通过css selector定位验证码元素
    await yazhengma.screenshot({'path': 'yazhengma.png'})  # 注意这里用的是ele.screenshot方法与教程1 page.screenshot是不同的
    box = await yazhengma.boundingBox()
    # box = await el.boundingBox()

    # left = int(box.get('x'))
    # top = int(box.get('y'))
    # right = int(left + int(box.get('width')))
    # bottom = int(top + int(box.get('height')))
    # im = Image.open('screenshort.png')
    # im = im.crop((left, top, right, bottom))
    # # 保存得到的验证码图片
    # im.save('code.png')
    chaojiying = Chaojiying_Client('2096953234', '15889307930', '96001')
    im = open('yazhengma.png', 'rb').read()
    ret = chaojiying.PostPic(im, 9004)
    xy = ret.get('pic_str')
    xy = xy.split('|')
    for i in xy:
        a = i.split(',')
        print(a[0],a[1])
        await page.hover('#J-loginImg')
        await page.mouse.click(box['x']+int(a[0]), box['y']+int(a[1]), {'delay': random.randint(1000, 2000), 'steps': 3})
    await asyncio.sleep(100)


asyncio.get_event_loop().run_until_complete(main())
