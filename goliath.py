import time

import cv2
import numpy as np
import pyautogui
from easyocr import Reader

import text

def crop_time(img, height_crop, width_crop):
    '''
    Crop image to only look at time
    '''

    width,height = pyautogui.size()
    width = int(width*width_crop)
    height = int(height*height_crop)
    cropped_image = img[0:height, 0:width]
    return cropped_image

def crop_speed(img, height_crop, width_crop):
    '''
    Crop image to only look at speed
    '''

    width,height = pyautogui.size()
    width_crop = int(width*width_crop)
    height_crop = int(height*height_crop)
    cropped_image = img[height_crop:height, width_crop:width]
    return cropped_image


def check_for_gltich(time_img):
    '''
    To check for a frozen or blank screen we will observe the time
    '''

    results = reader.readtext(time_img)
    results.sort(reverse=True, key=lambda x: x[1])

    # Black screen
    if results == None:
        print('Game likely crashed')
        return False

    # Check time to see if game isn't frozen
    times = []
    old_time = ''
    new_time = ''

    for (bbox, text, prob) in results:
        if bbox[3][0] > 250:
            times.append(text)
            new_time = max(times)

    if new_time > old_time:
        old_time == new_time
        print('Game has not crashed')
        return True
    else:
        print('Game likely crashed')
        return False


def check_for_crash(time_img):
    '''
    To check for a low speed to indicate crash
    '''

    results = reader.readtext(time_img)
    results.sort(reverse=True, key=lambda x: x[1])

    # Black screen or blank speed
    if results == None:
        print('Car likely crashed')
        return False

    # Check speed to see if car has crashed
    speed = 0

    # Try block in the event that text can't be read. Assume a greyed out 000
    try:
        for (bbox, text, prob) in results:
            speed = int(text)
    
            if speed > 10:
                print('Game has not crashed')
                return True
            else:
                print('Crash likely happened')
                return False
    except:
        print('Crash likely happened')
        return False

reader = Reader(['en'])

racing = True
while(racing == True):
    # Adjust if you need more/less time to start the race
    time.sleep(10)

    frame = pyautogui.screenshot("img/outcome.PNG")
    img = np.array(frame)

    # Get image for the time
    time_img = crop_time(img, height_crop=.25, width_crop=.15)

    # Get image for the speed 
    speed_img = crop_speed(img, height_crop=.85, width_crop=.75)

    racing = check_for_gltich(time_img)
    racing = check_for_crash(speed_img)

    time.sleep(10)


# ENTER INFORMATION FOR TEXTING TO WORK
text.send_text(email="EMAIL@gmail.com", pas="PASSWORD", sms_gateway='PHONE_NUMBER@CARRIER')
