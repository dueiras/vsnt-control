import cv2
import sys
import threading
from sensecam_control import onvif_control


ip = '172.18.14.155'
login = 'admin'
password = 'admin1234'

exit_program = 0


def event_keyboard(k):
    global exit_program

    if k == 27:  # esc
        exit_program = 1

    elif k == ord('w') or k == ord('W'):
        # Up
        X.relative_move(0, 0.1, 0)

    elif k == ord('a') or k == ord('A'):
        # Left
        X.relative_move(-0.1, 0, 0)

    elif k == ord('s') or k == ord('S'):
        # Down
        X.relative_move(0, -0.1, 0)

    elif k == ord('d') or k == ord('D'):
        # Right
        X.relative_move(0.1, 0, 0)

    elif k == ord('h') or k == ord('H'):
        X.go_home_position()

    elif k == ord('z') or k == ord('Z'):
        # Zoom In
        X.relative_move(0, 0, 0.05)

    elif k == ord('x') or k == ord('X'):
        # Zoom Out
        X.relative_move(0, 0, -0.05)


def capture(ip_camera):
    global exit_program

    #url http login axis camera
    #ip2 = 'http://' + login + ':' + password + '@' + ip_camera

    #url rtsp axis camera
    ip2 = 'rtsp://' + login + ':' + password + '@' + ip_camera

    cap = cv2.VideoCapture(ip2)

    while True:
        ret, frame = cap.read()
        if ret is not False:
            break

    while True:
        ret, frame = cap.read()

        if exit_program == 1:
            sys.exit()

        #cv2.namedWindow('Camera', cv2.WINDOW_NORMAL)
        cv2.imshow('Camera', frame)
        event_keyboard(cv2.waitKey(1) & 0xff)


X = onvif_control.CameraControl(ip, login, password)
X.camera_start()

#capture(ip)

t = threading.Thread(target=capture, args=(ip,))
t.start()