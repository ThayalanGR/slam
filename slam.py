import cv2
import sdl2
import sdl2.ext
import numpy as np
from display import Display
from extractor import Extractor

# commons
W = 1920 // 2
H = 1080 // 2
F = 1

# objects
display = Display(W, H)
K = np.array([[F, 0, W//2], [0, F, H//2], [0, 0, 1]])
print(K)
fe = Extractor(K)


def process_frame(frame):
    img = cv2.resize(frame, (W, H))
    matches = fe.extract(img)
    print("matches", len(matches))

    for pt1, pt2 in matches:
        u1, v1 = fe.denormalize(pt1)
        u2, v2 = fe.denormalize(pt2)
        cv2.circle(img, (u1, v1), color=(0, 255, 0), radius=3)
        cv2.line(img, (u1, v1), (u2, v2), color=(255, 0, 0))

    display.paint(img)


if __name__ == "__main__":
    cap = cv2.VideoCapture("./test_data/test.mp4")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret):
            process_frame(frame)
        else:
            break
