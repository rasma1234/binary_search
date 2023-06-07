import time 

def measure_time(func):
    
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Execution time: {func.__name__}{ execution_time} seconds: " )

        return execution_time, result
    return wrapper

@measure_time
def binary_search(lst_sorted, value):
    
    step = 0
    while len(lst_sorted) > 0:
        step += 1
        middle = len(lst_sorted) // 2
        if lst_sorted[middle] != value:
            if lst_sorted[middle] > value:
                lst_sorted = lst_sorted[:middle]
            elif lst_sorted[middle] < value:
                lst_sorted = lst_sorted[middle:]
        else:
            return True
    return False, step 

input_size = [1,100, 2, 5,200, 5, 6, 9, 600, 10, 100, 1000, 10000, 100000]
execution_times = []

for num in input_size:
    lst = list(range(1,(num*100) + 1))
    target = num // 2

    print(f"binary search on input size {num}: ")
    time__taken, result =  binary_search(lst, target)
    execution_times.append(time__taken*1000)

    print()

print(execution_times)

import matplotlib.pylab as plt


plt.plot(input_size,execution_times,label='log(N)')

plt.xlabel('Input Size') 
plt.ylabel('Time')
plt.legend()
plt.title('Binary Search')
plt.show()
