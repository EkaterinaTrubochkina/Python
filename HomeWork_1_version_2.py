import random

# 1.create list of 100 random numbers from 0 to 1000
# empty list
# declare variable for counter of numbers in list
# iteration
# filling list with random values
# print of final list

list_randoms = []
N = 100
for i in range(N):
    list_randoms.append(random.randint(0, 1000))
print (list_randoms)

# 2.sort list from min to max (without using sort()) by bubble method
# iteration
# if one element more then second
# then swap them
# print the list after sorting
for i in range(N - 1):
    for j in range(N - i - 1):
        if list_randoms[j] > list_randoms[j+1]:
            list_randoms[j], list_randoms[j+1] = list_randoms[j+1], list_randoms[j]
print (list_randoms)

# 3 and 4.calculate average for even and odd numbers and print results
# declare variable for sum of odd numbers in list
# declare variable for sum of even numbers in list
# declare variable for number of even numbers in list
# declare variable for number of odd numbers in list
# iteration for all number of numbers in list
# if remainder of the division by 2 equals 0
# then add number in sum of even numbers
# and count number of even numbers in list
# else iteration for odd number in list
# then add number in sum of odd numbers
# and count number of odd numbers in list
# try to count even average
# divide sum of numbers to count of numbers
# and print if no exceptions
# if catch exception
# then print that even average equals zero. It means that count of numbers and count of sum equals zero
# try the same for odd and print value
odd_sum = 0
even_sum = 0
even_count = 0
odd_count = 0
for i in range(N):
    if list_randoms[i] % 2 == 0:
        even_sum = even_sum + list_randoms[i]
        even_count += 1
    else:
        odd_sum = odd_sum + list_randoms[i]
        odd_count += 1
try:
    even_avg = even_sum / even_count
    print('even_avg =', even_avg)
except ZeroDivisionError:
    print('even_avg = 0')

try:
    odd_avg = odd_sum / odd_count
    print('odd_avg =', odd_avg)
except ZeroDivisionError:
    print('odd_avg = 0')