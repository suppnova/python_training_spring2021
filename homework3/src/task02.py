import hashlib
import random
import struct
import time
from multiprocessing import Pool, cpu_count
from timeit import default_timer as timer


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack("<" + "B" * len(data), data))


def main():
    start = timer()

    np = cpu_count()
    print(f"\nMultiprocessing calculation on {np} cores")

    with Pool(60) as pool:
        count = pool.map(slow_calculate, range(501))
        total = sum(count)

        end = timer()

        print(f"time: {end - start}")
        print(f"total_sum: {total}")

        return total, end - start


if __name__ == "__main__":
    main()
