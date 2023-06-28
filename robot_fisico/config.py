"""
    Configuration file
"""

# redis config
REDIS_HOST = "localhost"  # "192.168.43.125"
REDIS_HOST_REAL = '192.168.43.125'
REDIS_PORT = 6379

REDIS_COMMAND_TOPIC = 'command_topic'
REDIS_SENSOR_TOPIC = 'sensor_topic'
REDIS_KEY_CAM_IMAGE = 'image'
REDIS_KEY_TRAFFIC_SIGN = 'traffic_sign'
REDIS_KEY_TRAFFIC_SIGN_AREA = 'area'

# commands

###################################

VIRTUAL_TURN_SPEED = 1.0
VIRTUAL_COURSE_SPEED = 2.0
VIRTUAL_TURN_ANGLE = 10
VIRTUAL_TURN_RATE = 0.065

DEBUG = True

REAL_TURN_SPEED = 700
REAL_COARSE_SPEED = 700
REAL_TURN_ANGLE = 15

REDIS_KEY_STEERING = 'steering'
REDIS_KEY_STEERING_RATE = 'steering_rate'
