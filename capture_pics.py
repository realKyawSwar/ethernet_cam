import cv2
import os
import datetime

address = 'http://128.53.209.100/stream'
cap = cv2.VideoCapture(address)
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
