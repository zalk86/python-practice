#For and While loops

#for loops 1 - print numbers 1-10
#-------------------------------------------------------
for i in range(1,11):
    print (i)

#------------------------------------------------------
#2 - sum of numbers 1- 100 using for loop

total = 0
for i in range(1,101):
    total = total +i
print(total)

# 3 - print even numbers between 1 and 20

for i in range(1,21):
    if i%2 == 0:
     print(i)

#4 - count characters in a string

string = "hello"
count = 0
for i in string:
    count = count +1
print(count)

#5 - count vowels in a string

string = "zalan"
vowels = "aeiou"
count = 0
for i in string:
    if i in vowels:
        count = count +1
        
print(count)

#6 - multiplication table for a number

number = 3
for i in range(1,11):
    result = number * i
    print(number, "x", i, "=", result)

#7 - reverse string

v_string = "zalan"
v_reversed_string = ""
for i in v_string:
    v_reversed_string = i + v_reversed_string

print(v_reversed_string)

#8 - largest number in the list

numbers = [2,5,7,9,24,8,6,34]
largest = numbers[0]

for i in numbers:
    if i>largest:
        largest = i
print(largest)

#9 - count occurences 

numbers = [3,7,9,3,7,0,7,3,6]
rep_char = 0
count = 0

for i in numbers:
    if i == rep_char:
        break
    print(i)

#10 - repeat string printing
for i in range(1,20):
    print(i*"*")

#11 - sum of even numbers

even_Nums = 0
for i in range(1,51):
    if i%2==0:
        even_Nums+= i
print(even_Nums)

#12 - count digits in a number

number = "12345"
total = 0
for i in number:
    total = total + 1

print(total)

#13  - print square pattern
for i in range(5):
    print(5*"*")

#14 - print right aligned triangle pattern

for i in range(1,6):
    spaces = " "*(5-i)
    stars = "*"*i
    print(spaces + stars)

#15 - sum of digits

num = 1234
total = 0
for i in str(num):
    total = total + int(i)
print(total)

#16 = count words in a sentence

sentence = "I live in Newpot"
count = 1
for i in sentence:
    if i ==" ":
        count = count +1
print(count)

#17 - find second largest number from a list

list = [4,5,3,8,2,11]
largest = list[0]
second_largest = list[0]

for i in list:
    if i>largest:
        second_largest = largest
        largest = i
    elif i>second_largest and i != largest:
        second_largest = i
print(second_largest)

#18 - check if string is all digits

string = "12345"
is_digit = True
for i in string:
    if not i.isdigit():
        is_digit = False
        break
        
print(is_digit)

#19 - print star pyramid

n = 10
for i in range(1, n+1):
    spaces = " "*(n-i)
    stars = "*"*(2*i-1)
    print(spaces +stars)

#20 - FizzBuZZ

for i in range(1,31):
    if i % 3 ==0 and i % 5 ==0:
        print("FizzBuzz")
    elif i%3 ==0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)
        





