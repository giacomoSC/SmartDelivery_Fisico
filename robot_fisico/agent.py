import time

from picamera2 import Picamera2
import redis

import config
from physical_body import PhysicalBody


class Agent:

    def __init__(self):
        self._physical_body = PhysicalBody()

        self._R = redis.Redis(host=config.REDIS_HOST_REAL, port=config.REDIS_PORT, decode_responses=True)
        self._R.flushall()

        self.regular_velocity = 700
        self.turn_left_velocity = 700
        self.turn_right_velocity = 700
        self.old_signal = ""
        self.curr_steering_angle = 90

    # ACT
    def drive_for_way(self, dest):
        way = dest
        intr = 0
        while True:
            self._physical_body.line()
            if way - (intr*2) == '1':
                self._steer(0)
                break
            elif way - (intr*2) == '2':
                self._steer(180)
                break
            else:
                intr = intr + 1
        self.drive_for_shape()

    def drive_for_shape(self):
        while True:
            self._physical_body.line()
            self._shapes()
            self._physical_body.move_forward(700)


    def _steer(self, steering_angle) -> None:
        if steering_angle == -90:
            self._physical_body.stop()
            return

        STEERING_RATE = 10
        print(self.regular_velocity, STEERING_RATE)
        if steering_angle <= 90:
            self._physical_body.stop()
            steer = abs(steering_angle - 90)
            self._physical_body.turn(-int(steer * STEERING_RATE / 4), steer * STEERING_RATE)
            time.sleep(0.005)
            self._physical_body.move_forward(700)
            return
        elif steering_angle >= 90:
            self._physical_body.stop()
            steer = abs(steering_angle - 90)
            self._physical_body.turn(steer * STEERING_RATE, -int(steer * STEERING_RATE / 4))
            time.sleep(0.005)
            self._physical_body.move_forward(700)
            return

        self._physical_body.move_forward(self.regular_velocity)

    def _shapes(self):
        picam2 = Picamera2()
        picam2.start()

        self._physical_body.line()
        self._physical_body.look_left()

        img_array = picam2.capture_array()
        img_str = img_array.tostring()
        self._R.set('image', img_str)

        while True:
            res = self._R.get('image_result')

            if res is not None:
                if res == "found":
                    print("found")
                    return "found"
                break

        self._physical_body.look_right()

        img_array = picam2.capture_array()
        img_str = img_array.tostring()
        self._R.set('image', img_str)

        while True:
            res = self._R.get('image_result')

            if res is not None:
                if res == "found":
                    print("found")
                    return "found"
                break

        self._physical_body.look_forward()
        return "not found"
