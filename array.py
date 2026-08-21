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

# # fibonacci
# def fib(n):
#     if n <= 0: 
#         return []
#     if n == 1:
#         return [0]
#     series = [0, 1]
#     for _ in range(2, n):
#         next_term = series[-1] + series[-2]
#         series.append(next_term)       
#     return series

# print(fib(5))

# power a^b using recursion

# def power(a,b):
#     if b == 0:
#         return 1
#     if b == 1:
#         return a

# quick sort

# def partition(array, low, high):
#     pivot = array[high]
#     i = low - 1

#     for j in range(low, high):
#         if array[j] <= pivot:
#             i += 1
#             array[i], array[j] = array[j], array[i]

#     array[i+1], array[high] = array[high], array[i+1]
#     return i+1

# def quicksort(array, low=0, high=None):
#     if high is None:
#         high = len(array) - 1

#     if low < high:
#         pivot_index = partition(array, low, high)
#         quicksort(array, low, pivot_index-1)
#         quicksort(array, pivot_index+1, high)

# arr = [64, 43, 67, 34, 25, 83, 12, 22, 11, 90, 5]
# quicksort(arr)
# print("Sorted array:", arr)

# merge sort

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     sortedLeft = merge_sort(left_half)
#     sortedRight = merge_sort(right_half)

#     return merge(sortedLeft, sortedRight)

# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# unsorted_arr = [33, 74, 6, 10, 15, 23, 55, 13, 64]
# sorted_arr = merge_sort(unsorted_arr)
# print("Sorted array:", sorted_arr)

# counting sort


# def counting_sort(array):
#     if not array:
#         return array
        
#     max_val = max(array)
#     count = [0] * (max_val + 1)

#     for num in array:
#         count[num] += 1
        
#     array[:] = []

#     for num, freq in enumerate(count):
#         array.extend([num] * freq)

#     return array

# unsorted_arr = [4, 7, 3, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
# sorted_arr = counting_sort(unsorted_arr)
# print("Sorted array:", sorted_arr)

# class linked_list:
#     data = None
#     address = None

# def fact(n):
#     factorial = 1
#     for i in range(2,n+1):
#         factorial = factorial * i
#     print(factorial)
# fact(5)

# def fact(n):
#     if n == 0:
#         return 1
#     return n * fact(n-1)
# print(fact(6))

# def fact(n):
#     if n == 0:
#         return 1
#     print(n)
#     return n * fact(n-1)
# print(fact(6))

# def fib(n):
#     num1, num2 = 0, 1
#     print(num1)
#     print(num2)
#     for i in range(n-2):
#         num3 = num1 + num2
#         num1 = num2
#         num2 = num3
#         print(num3)
# fib(6)

# def fib(n):
#     if n <= 0:
#         return []
#     if n == 1:
#         return [0]
#     series = [0,1]
#     for i in range(2,n):
#         new_value = series[-1] + series[-2]
#         series.append(new_value)
#     return series
# print(fib(8))

# # insertion sort without recursion

# array = [3,2,4,6,8,5,7,1]

# for i in range(1,len(array)):
#     insert_index = i
#     insert_value = array.pop(i)
#     for j in range(i-1,-1,-1):
#         if array[j] > insert_value:
#             insert_index = j
#     array.insert(insert_index,insert_value)

# print(array)

# array = [10,20,30,60,50,40]
# for i in range(len(array)):
#     for j in range(len(array)-i-1):
#         if array[j] >= array[j+1]:
#             array[j], array[j+1] = array[j+1], array[j]
# print(array)

# simple stack using linked list method

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next : None

# class linkedliststack:
#     def __init__(self):
#         self.top = None

#     def push(self, item):
#         new_node = node(item)
#         new_node.next = self.top
#         self.top = new_node
#         print(item,'inserted into the stack')

# lls = linkedliststack()
# lls.push(10)

# simple tree implimentation using linked list
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class tree:
#     def push(data):
#         new_node = node(data)

# def inorder(root):
#     if root:
#         inorder(root.left)
#         print(root.data, end=" ")
#         inorder(root.right)

# root = node(10)
# node_b = node(20)
# node_c = node(30)
# node_d = node(40)
# node_e = node(50)

# root.left = node_b 
# root.right = node_c

# node_b.left = node_d
# node_b.right = node_e  

# inorder(root)

# a simple linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(30)
node3 = Node(20)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

# using loop

nodes = [node1,node2,node3,node4]
for i in nodes:
    print(i.data)
    if i.next == None:
        break

# using recursion method1

def travarsal(node):
    print(node.data)
    if node.next != None:
        travarsal(node.next)

# using recursion method2

def travarsal(node):
    print(node.data)
    if node.next == None:
        return
    travarsal(node.next)

travarsal(node1)