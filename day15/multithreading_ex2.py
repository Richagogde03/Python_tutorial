import threading
import time
from concurrent.futures import ThreadPoolExecutor


def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


def main():
    # time1 = time.perf_counter()
    # func(4)
    # func(2)
    # time2 = time.perf_counter()
    # print(time2 - time1)

    time11 = time.perf_counter()
    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[3])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    time12 = time.perf_counter()
    print(time12 - time11)


def poolingDemo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future1 = executor.submit(func, 3)
        # print(future1.result())
        # future2 = executor.submit(func, 2)
        # print(future2.result())
        # future3 = executor.submit(func, 5)
        # print(future3.result())

        # future1 = executor.submit(func, 3)
        # future2 = executor.submit(func, 4)
        # future3 = executor.submit(func, 5)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())

        l1 = [3, 4, 5, 7, 8]
        results = executor.map(func, l1)
        for result in results:
            print(result)


poolingDemo()
