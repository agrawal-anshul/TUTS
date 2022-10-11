from time import sleep, perf_counter
from threading import Thread

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
new_alphabets = []

def task(arr,start_index,end_index):
    print('Starting a task...')
    for i in range(start_index,end_index):
      print(arr[i]) 
      new_alphabets.append(arr[i])
      sleep(1)
    print('done')

start_time = perf_counter()

# create new threads
arr_length = len(alphabets)
print(arr_length)

num_threads = 10
sub_array_size = arr_length//num_threads

threads = []


for n in range(0, num_threads):
   # n = 0,1,2
   if num_threads <= arr_length:
      if n != num_threads-1:
         start_index = (n)*sub_array_size
         end_index= start_index + sub_array_size
         t = Thread(target=task, args=(alphabets, start_index, end_index))
      else:
         start_index = (n)*sub_array_size
         end_index= arr_length
         t = Thread(target=task, args=(alphabets, start_index, end_index))
      threads.append(t)
      t.start()
   else:
      print('Number of threads should be lesser than or equal to array length')

# wait for the threads to complete
for t in threads:
    t.join()


# t1 = Thread(target=task, args=(alphabets,0,10))
# t2 = Thread(target=task, args=(alphabets,10,26))

# # start the threads
# t1.start()
# t2.start()

# # wait for the threads to complete
# t1.join()
# t2.join()

print('Finally done')
if len(alphabets) == len(new_alphabets):
   print('Equal')
   alphabets.sort()
   new_alphabets.sort()
   print(alphabets)
   print(new_alphabets)
else:
   print('Unequal')
   alphabets.sort()
   new_alphabets.sort()
   print(alphabets)
   print(new_alphabets)
end_time = perf_counter()

print(f'It took {end_time- start_time: 0.2f} second(s) to complete.')