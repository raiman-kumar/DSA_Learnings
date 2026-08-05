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

arr = [50,20,10,40,30,60,35,23,75,11]
for j in range(len(arr)-1):
    swapped = False
    for i in range(len(arr)-j-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            swapped = True
    if swapped == False:
        break
print(arr)