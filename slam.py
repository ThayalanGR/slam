import cv2
import pygame

# commons
W = 1920 // 2
H = 1080 // 2

# creating pygame window
pygame.init()
screen = pygame.display.set_mode((W, H))



def process_frame(frame):
    img = cv2.resize(frame, (W, H))
    print(img.shape)


if __name__ == "__main__":
    cap = cv2.VideoCapture("./test_data/test.mp4")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret):
            process_frame(frame)
        else:
            break

    # print("hello world")
