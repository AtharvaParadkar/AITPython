import threading
import time

# Function to be executed by the first thread
def thread_one_func():
    for i in range(5):
        print("Thread One:", i)
        time.sleep(1)

# Function to be executed by the second thread
def thread_two_func():
    for i in range(5):
        print("Thread Two:", i)
        time.sleep(1)

# Create the first thread
thread_one = threading.Thread(target=thread_one_func)

# Create the second thread
thread_two = threading.Thread(target=thread_two_func)

# Start both threads
thread_one.start()
thread_two.start()

# Wait for both threads to finish
thread_one.join()
thread_two.join()

print("Execution completed.")
