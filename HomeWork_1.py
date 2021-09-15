import random

# 1.create list of 100 random numbers from 0 to 1000
list_randoms = []  # empty list
N = 2  # declare variable for counter of numbers in list
for i in range(N):  # iteration
    list_randoms.append(random.randint(0, 1000))  # filling list with random values
print (list_randoms)  # print of final list

# 2.sort list from min to max (without using sort()) by bubble method
for i in range(N - 1):  # iteration
    for j in range(N - i - 1):
        if list_randoms[j] > list_randoms[j+1]:  # if one element more then second
            list_randoms[j], list_randoms[j+1] = list_randoms[j+1], list_randoms[j]  # then swap them
print (list_randoms)  # print the list after sorting

# 3.calculate average for even and odd numbers
odd_sum = 0  # declare variable for sum of odd numbers in list
even_sum = 0  # declare variable for sum of even numbers in list
even_count = 0  # declare variable for number of even numbers in list
odd_count = 0  # declare variable for number of odd numbers in list
for i in range(N):  # iteration for all number of numbers in list
    if list_randoms[i] % 2 == 0:  # if remainder of the division by 2 equals 0
        even_sum = even_sum + list_randoms[i]  # then add number in sum of even numbers
        even_count += 1  # and count number of even numbers in list
    else:  # esle iteration for odd number in list
        odd_sum = odd_sum + list_randoms[i]  # then add number in sum of odd numbers
        odd_count += 1  # and count number of odd numbers in list
try:  #
    even_avg = even_sum / even_count
    print('even_avg =', even_avg)
except ZeroDivisionError:
    print('even_avg = 0')

try:
    odd_avg = odd_sum / odd_count
    print('odd_avg =', odd_avg)
except ZeroDivisionError:
    print('odd_avg = 0')

# Checks of code
# print (even_sum)
# print (odd_sum)
# print (even_count)
# print (odd_count)
# print (even_avg)
# print (odd_avg)



    # 4.print both average result in console

