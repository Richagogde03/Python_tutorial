import multiprocessing
import time

# global variables , will not append value in it
# because two process do not share memory or variables
# it will create a copy again whenever we use in any process
# if we want to print this list we need to do in a process not
# globally anywhere
squares_result = []
cube_result = []


def calc_cube(numbers):
    for i in numbers:
        time.sleep(1)
        cube_result.append(i*i*i)
        print(f"Cube of {i} : {i*i*i}")
    print("Cube List from function or process: " + str(cube_result))


def calc_sq(numbers):
    for i in numbers:
        time.sleep(1)
        squares_result.append(i*i)
        print(f"Square of {i} : {i*i}")
    print(f"Square List from function or process: {squares_result}")


arr = (2, 3, 4, 5)

p1 = multiprocessing.Process(target=calc_sq, args=(arr,))
p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

p1.start()
p2.start()

p1.join()
p2.join()

print("Square List : " + str(squares_result))
print("Cube List : " + str(cube_result))

print("Done!!")
