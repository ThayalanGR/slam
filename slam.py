import cv2
import sdl2
import sdl2.ext

# commons
W = 1920 // 2
H = 1080 // 2

sdl2.ext.init()
window = sdl2.ext.Window("Test Board", size=(W, H))
window.show()


def process_frame(frame):
    img = cv2.resize(frame, (W, H))

    # breaking process
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            exit(0)

    # writing and refreshing sdl surface
    surf = sdl2.ext.pixels2d(window.get_surface())
    surf[:] = img.swapaxes(0, 1)[:, :, 0]
    window.refresh()


if __name__ == "__main__":
    cap = cv2.VideoCapture("./test_data/test.mp4")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret):
            process_frame(frame)
        else:
            break
