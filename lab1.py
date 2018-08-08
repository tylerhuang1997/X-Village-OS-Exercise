import threading
import numpy as np
import time

# x is the amount of row and colume
x = 100

# Build and control the matrix A & B
# Multi-thread can use global available
matA = np.random.randint(10, size = (x, x))
matB = np.random.randint(10, size = (x, x))

def thread_func(a, b, result):                                      # a = axis begin row, b = axis end row
    for row in range(a, b):
        result[row] = np.matmul(matA[row], matB)
    #print(result)                                                   # Remind me the circumstance of the matrix buiding by multi-thread

def main():
    # Assign job to threads
    result = np.zeros((matA.shape[0], matB.shape[1]))

    thread_num = 10
    threads = []
    start_time = time.time()

    for i in range(thread_num):
        # Pass argument to function with tuple
        thread = threading.Thread(target = thread_func, args=(i*(x//thread_num), (i+1)*(x//thread_num), result))
        threads.append(thread)
    #print(threads)

    # run all threads
    for thread in threads:
        thread.start()

    # Wait for threads finish
    for thread in threads:
        thread.join()
    
    # Calculate the time usnig Multi-thread
    end_time = time.time()
    print('Time elapsed:\t', end_time - start_time)
    print(result)
    print(np.matmul(matA, matB))
    print('Answer is correct:', np.all(np.matmul(matA, matB) == result))

if __name__ == "__main__":
    main()