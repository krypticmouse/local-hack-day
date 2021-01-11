import argparse
import sys
from datetime import datetime

def random(start, end, seed):
    number = (seed ** 3 + seed * 2 + 1) * datetime.now().microsecond
    return number % (end-start) + start


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--s', type=int, default=0,
                        help='Starting of the Range.')
    parser.add_argument('--e', type=int, default=10,
                        help='Ending of the Range.')
    parser.add_argument('--seed', type=int, default=12, help='seed')
    args = parser.parse_args()
    sys.stdout.write(str(random(args.s,args.e,args.seed)) + '\n')