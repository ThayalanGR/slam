import cv2
import sdl2
import sdl2.ext
import numpy as np
from display import Display
from extractor import Extractor

# commons
W = 1920 // 2
H = 1080 // 2

# objects
display = Display(W, H)
fe = Extractor()


def process_frame(frame):
    img = cv2.resize(frame, (W, H))
    kps, des, matches = fe.extract(img)
    if matches is None:
        return

    for p in kps:
        u, v = map(lambda x: int(round(x)), p.pt)
        cv2.circle(img, (u, v), color=(0, 255, 0), radius=3)
    display.paint(img)


if __name__ == "__main__":
    cap = cv2.VideoCapture("./test_data/test.mp4")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret):
            process_frame(frame)
        else:
            break
