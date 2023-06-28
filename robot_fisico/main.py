import signal

import readchar
import redis

from agent import Agent


def handler(signum, frame):
    msg = "Ctrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True)  # clear the printed line
        print("    ", end="\r", flush=True)


if __name__ == '__main__':
    r = redis.Redis(host='192.168.0.128', port=6379, decode_responses=True)
    while True:
        way = r.get('way')

        if way is not None:
            break

    Agent().drive_for_way(way)
    signal.signal(signal.SIGINT, handler)
