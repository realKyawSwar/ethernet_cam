import cv2
import os
import datetime
import requests


ip = "128.53.209.100"
vid_address = f'http://{ip}/stream'
try:
    response = requests.get(f'http://{ip}/')
    # print(response.text)
    # print(len(response.text))
    # print(type(response.text))
    if response.text[:4] == "Cool":
        cap = cv2.VideoCapture(vid_address)
        basename = "202_CRC4"
        dir_path = "data/"
        ext = 'jpg'
        # just showing video to screen
        os.makedirs(dir_path, exist_ok=True)
        base_path = os.path.join(dir_path, basename)
        print(base_path)
        if cap.isOpened():
            ret, frame = cap.read()
            cv2.imwrite(f"{base_path}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')}.{ext}", frame)
        cap.release()
        cv2.destroyAllWindows()
except Exception as err:
    print(err)

