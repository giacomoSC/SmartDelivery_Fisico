import redis

import config
from motor import Motor
from infrared_line_tracking import Line_Tracking
from servo import Servo


class PhysicalBody:

    def __init__(self):
        self.R = redis.Redis(host=config.REDIS_HOST, port=config.REDIS_PORT, decode_responses=True)
        self._PWM = Motor()
        self._infrared = Line_Tracking()
        self._servo = Servo()

    def line(self):
        self._infrared.run()

    def move_forward(self, velocity):
        self._PWM.setMotorModel(velocity, velocity, velocity, velocity)

    # ACT
    def move_backward(self, velocity):
        self._PWM.setMotorModel(-velocity, -velocity, -velocity, -velocity)

    # ACT
    def turn(self, left_velocity, right_velocity):
        self._PWM.setMotorModel(left_velocity, left_velocity, right_velocity, right_velocity)

    # ACT
    def stop(self):
        self._PWM.setMotorModel(0, 0, 0, 0)

    def look_right(self):
        self._servo.setServoPwm('0', 180)

    def look_left(self):
        self._servo.setServoPwm('0', 0)

    def look_forward(self):
        self._servo.setServoPwm('0', 90)