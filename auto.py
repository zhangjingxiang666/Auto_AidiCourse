#请将屏幕分辨率调至1920*1080
#请将chrome浏览器的缩放调成正常（100%）
#请将视频播放窗口调至正常，不要全屏
#请将右侧课程播放列表展开，不要收起
import pyautogui
import time
from PIL import ImageGrab
import PIL
import random

while True:
    time.sleep(random.randint(3,20))
    img = ImageGrab.grab()
    img.save('12.jpg')
    rgb_img = img.convert ('RGB')
    r, g, b = rgb_img.getpixel((988, 410))#自己调“确定”框所出现的像素位置
    print (r, g, b)
    print(r)
    print(type(r))
    if r==8 and  g==128 and b==241:#如果这个位置是淡蓝色【r==8 and  g==128 and b==241】则说明有确定框出现
        #print('Hello World')
        pyautogui.moveTo(988, 410)#自己可以调节点击“确定”的位置
        pyautogui.click()
    else:
        print('error')
