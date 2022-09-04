import time
import random

lst = []
for i in range(50000):
    lst.append(random.randint(1,10000000))

initial_time = time.time()
initial_clock = time.process_time()
#print(lst)
lst.sort()
#print(lst)
final_time = time.time()
final_clock = time.process_time()
print("Time Taken (Wall): %.50f" % (final_time - initial_time))
print(f"Time Taken (CPU Cycles): {final_clock - initial_clock:.50f}")

