import cv2
import sdl2
import sdl2.ext
from display import Display

# commons
W = 1920 // 2
H = 1080 // 2

# Display object
display = Display(W, H)


def process_frame(frame):
    img = cv2.resize(frame, (W, H))
    display.paint(img)


if __name__ == "__main__":
    cap = cv2.VideoCapture("./test_data/test.mp4")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret):
            process_frame(frame)
        else:
            break
