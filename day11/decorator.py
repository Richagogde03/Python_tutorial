def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning!!")

        fx(*args, **kwargs)
        print("Thanks for using this function!!\n")
    return mfx


# decorator without parameters
@greet
def hello():
    print("hello people")


# decorator with parameters
@greet
def add(a, b):
    print(f"Sum = {a + b}")


# decorator with keyword arguments
@greet
def keyword(fname, lname):
    print(f"The full name of a person is {fname} {lname}")


hello()
# greet(hello)(), {2nd method}
add(10, 20)
# greet(add)(1, 2),  {2nd method}
keyword(lname="soni", fname="Priyanka")
