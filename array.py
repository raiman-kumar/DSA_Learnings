# # array in DSA
# # array applies through list in python

# myarr = [12,18,16,14,22,11]
# print(myarr)

# n = 5000
# print("start")
# for i in range(n):
#     print(i)
# print("stop")

# n = 5
# for i in range(n):
#     for j in range(n):
#         print(i,j)

# n = 5
# count = 0
# for i in range(n):
#     count += 1
# print(count)

# n = 5
# count = 0
# for i in range(n):
#     for j in range(n):
#         count += 1
# print(count)

# n = 1000
# count = 0

# while n > 0:
#     count += 1
#     n = n // 2

# print(count)

# find largest elemeent in array

# mylist = [10, 5, 18, 7, 20, 3]
# largest = mylist[0]
# second_largest = mylist[0]
# for i in mylist:
#     if i > largest:
#         largest = i
# print(largest)

# find second largest in array

# mylist = [10, 5, 18, 7, 20, 3]
# largest = mylist[0]
# second_largest = mylist[0]
# for i in mylist:
#     if i > largest:
#         second_largest = largest
#         largest = i
#     elif i > second_largest and i != largest:
#         second_largest = i
# print(second_largest)

# arr = [10,20,30,40,50]

# print(arr[0])
# print(arr[2])
# print(arr[4])

# traversal in array

# arr = [10,20,30,40,50]
# print(arr)

# # method 1 : via pythonic
# for i in arr:
#     print(i)

# # method 2 : via index

# for i in range(len(arr)):
#     print(arr[i])

# # method 3 : professional

# for index, value in enumerate(arr):
#     print(index, value)

# # sum of the elements
# summ = 0
# for i in arr:
#     summ += i
# print(summ)

# # count even numbers
# arr = [10,25,18,31,40]
# count = 0

# for i in arr:
#     if i % 2 == 0:
#         count += 1

# print(count)

# # largest element in array
# largest = arr[0]
# for i in arr:
#     if i > largest:
#         largest = i

# print(largest)

# search element in array
# linear search

# arr = [10,20,30,40,50]

# for index, value in enumerate(arr):
#     if value == 40:
#         print(value,"found at index",index)
#         break

# binary search

# arr = [10,20,30,40,50]
# target = 30
# def binary_search(array,target_value):
#     left = 0
#     right = len(array)-1
#     while left <= right:
#         mid = (left + right) // 2
#         if array[mid] == target_value:
#             return mid
#         elif target_value > array[mid]:
#             left = mid + 1
#         elif target_value < array[mid]:
#             right = mid - 1
#     else:
#         return -1

# status = binary_search(arr,target)
# if  status == -1:
#     print('element not found')
# else:
#     print(target,'found at index',binary_search(arr,target))

# sorting 
# bubble sort

# arr = [50,20,10,40,30,60,35,23,75,11]
# for j in range(len(arr)-1):
#     swapped = False
#     for i in range(len(arr)-j-1):
#         if arr[i] > arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
#             swapped = True
#     if swapped == False:
#         break
# print(arr)

# selection sort

# arr = [50,20,10,40,30,60,35,23,75,11]
# for j in range(len(arr)-1):
#     minimum = j
#     for i in range(j,len(arr)):
#         if arr[minimum] > arr[i]:
#             minimum = i
#     if minimum != j:
#         arr[j], arr[minimum] = arr[minimum], arr[j]
# print(arr)

# insertion sort

# arr = [50,20,40,30,10]

# for i in range(1,len(arr)):
#     insert_index = i
#     current_value = arr[i]

#     for j in range(i-1,-1,-1):
#         if arr[j] > current_value:
#             arr[j+1] = arr[j]
#             insert_index = j
#         else:
#             break
#     arr[insert_index] = current_value

# print(arr)

# recursion

# def show(n):
#     if n == 0: # base case
#         return
#     print('show method calling')
#     show(n-1)  # recursive relation
# show(3)

# print 1 to n
# def show(n):
#     if n == 0: # base case
#         return 0   
#     show(n-1)  # recursive relation
#     print(n)   # print backword
# show(5)

# print n to 1
# def show(n):   # base case
#     if n == 0: # recursive relation
#         return 0   
#     print(n)   # print forward
#     show(n-1)
# show(5)

# sum of n to 1
# def add(n):
#     if n == 0: 
#         return 0
    
#     return n + add(n-1)  
# print(add(5))

# factorial
# def fact(n):
#     if n == 0: 
#         return 1   
#     return n * (n-1)
    
# print(fact(5))

# fibonacci
def fib(n):
    if n <= 0: 
        return []
    if n == 1:
        return [0]
    series = [0, 1]
    for _ in range(2, n):
        next_term = series[-1] + series[-2]
        series.append(next_term)       
    return series

print(fib(5))

# power a^b

def power(a,b):
    if b == 0:
        return 1
    if b == 1:
        return a

    