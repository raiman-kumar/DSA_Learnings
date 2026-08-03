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

# mylist = [10, 5, 18, 7, 20, 3]
# largest = mylist[0]
# second_largest = mylist[0]
# for i in mylist:
#     if i > largest:
#         largest = i
# print(largest)

mylist = [10, 5, 18, 7, 20, 3]
largest = mylist[0]
second_largest = mylist[0]
for i in mylist:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print(second_largest)