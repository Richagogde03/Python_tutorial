import threading
import time

balance = 1000


def withdraw(amount):
    global balance
    if balance >= amount:
        time.sleep(0.01)
        balance -= amount
        print(f"Withdrawal successful. Remaining balance: {balance}")
    else:
        print("Insufficient funds.")


thread1 = threading.Thread(target=withdraw, args=(600,))
thread2 = threading.Thread(target=withdraw, args=(600,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Final balance: {balance}")
