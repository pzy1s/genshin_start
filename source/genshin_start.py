from PIL import ImageGrab
import numpy as np
import time
import os

def is_white_screen(image, threshold=0.95):
    np_image = np.array(image)
    white_pixels = np.sum(np_image > 200)
    total_pixels = np_image.size
    
    ratio = white_pixels / total_pixels
    return ratio > threshold
print("原神小助手正在运行")
while True: 
    # 获取屏幕截图
    screenshot = ImageGrab.grab()
    
    # 判断是否为白屏
    if is_white_screen(screenshot):
        # 原神，启动!
        os.startfile(".\\Shed_a_Light.mp3")
        os.startfile(".\\YuanShen.exe.lnk")
        time.sleep(600)

    time.sleep(1)
