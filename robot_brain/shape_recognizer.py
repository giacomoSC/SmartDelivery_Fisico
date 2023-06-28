import numpy as np
import cv2
import base64


def shape_recognizer(img_str):

    tmp = base64.b64decode(img_str)

    nparr = np.frombuffer(tmp, np.uint8)

    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # converting image into grayscale image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # setting threshold of gray image
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # using a findContours() function
    contours, _ = cv2.findContours(
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    i = 0

    # list for storing names of shapes
    for contour in contours:

        # here we are ignoring first counter because
        # findcontour function detects whole image as shape
        if i == 0:
            i = 1
            continue

        # cv2.approxPloyDP() function to approximate the shape
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

        # using drawContours() function
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 5)

        print(len(approx))
        # putting shape name at center of each shape
        if len(approx) == 3:
            #cv2.putText(img, 'Triangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            print('triangle')

            cv2.imshow('Papa\'', img)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return 'triangle'

        elif len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspectRatio = float(w) / h
            if 0.95 <= aspectRatio < 1.05:
                #cv2.putText(img, 'Square', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                print('square')

                cv2.imshow('Papa\'', img)

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                return 'square'
            else:
                #cv2.putText(img, 'Rectangle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                print('rectangle')

                cv2.imshow('Papa\'', img)

                cv2.waitKey(0)
                cv2.destroyAllWindows()

                return 'rectangle'
        elif len(approx) < 20:
            #cv2.putText(img, 'circle', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            print('circle')

            cv2.imshow('Papa\'', img)

            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return 'circle'

    return 'indefinito'


class Recognizer:

    def __init__(self, shape):
        self.target = shape

    def check(self, img_str):
        if shape_recognizer(img_str) == self.target:
            return True
        return False
