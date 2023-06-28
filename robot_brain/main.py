import redis
import config

from shape_recognizer import Recognizer

if __name__ == '__main__':
    way = int(input("Way number:"))
    destination = input("Destination shape:")

    r = redis.Redis(host=config.REDIS_HOST_REAL, port=config.REDIS_PORT, decode_responses=True)
    r.flushall()

    r.set('way', way)

    while True:
        img_str = r.get('image')

        if img_str is not None:
            print(img_str)
            print(type(img_str))
            chk = Recognizer(destination).check(img_str)
            if chk:
                break
            else:
                r.set('image_result', "not found")
                print("not found")
                r.delete('image')

    r.set('image_result', "found")
    print("found")
