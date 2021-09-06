#Python Assignment

#Python Program to Print Hello world!

print("Hello World")


# Python Program to Add Two Numbers

num1 =int(input("Enter the First Num:"))
num2 =int(input("Enter the Second Num:"))
num3 =num1+num2
print("sum of %0.d and %0.d are:"%(num1,num2),num3)


# Python Program to Find the Square Root

import math
num =int(input("Enter the Number for finding square root:"))
square_root =math.sqrt(num)
print("The square root of %0.d is:"%(num),square_root)


# Python Program to Calculate the Area of a Triangle

# HINT : Formulea =1/2*b*h
base =float(input("Enter the base  of a traingle: "))
height =float(input("Enter the height of a traingle:"))
Area =(base * height)/2
print("The area of the traingle is %d and %d:"%(base,height),Area )


# Python Program to Solve Quadratic Equation

import math  
a =int(input("Enter the value of a:"))
b =int(input("Enter the value of b:"))
c =int(input("Enter the value of c:"))
dis =(b**2)-(4*a*c)
if(dis>0):
    root1 =(-b +math.sqrt(dis)/(2*a))
    root2 =(-b -math.sqrt(dis)/(2*a))
    print("Two distinct real roots are %.2f and %.2f" %(root1, root2))
elif(dis==0):
    root1 =root2 =-b/(2*a)
    print("Two equal and real roots are %.2f and %.2f" %(root1, root2))
elif(dis<0):
    root1 =root2 = -b/(2*a)
    imaginary = math.sqrt(-dis)/(2*a)
    print("Two distinct complex roots are %.2f+%.2f and %.2f-%.2f" %(root1, imaginary, root2, imaginary))


# Python Program to Swap Two Variables

num1 =int(input("Enter the num1: "))
num2 =int(input("Enter the num2: "))
print("Before Swapping")
print("num1=",num1)
print("num2=",num2)
num1,num2 = num2,num1
print("Before Swapping")
print("num1=",num1)
print("num2=",num2)

#method-II
num1 =int(input("Enter the num1: "))
num2 =int(input("Enter the num2: "))
print("Before Swapping")
print(num1,num2)
temp=num1
num1=num2
num2=temp
print("After Swapping")
print(num1,num2)


# Python Program to Generate a Random Number

import random
lower =int(input("Enter the lower bound:"))
upper =int(input("Enter the upper bound:"))
print(random.randint(lower,upper))


# Python Program to Convert Kilometers to Miles

km =int(input("Enter the kilometers:"))
mile =0.62137119*km
print("%0.d kilometers equal to"%km,mile,"miles")


# Python Program to Convert Celsius To Fahrenheit

celsius =float(input("Enter the celsius degree: "))
fahrenhiet =(celsius * 1.8) + 32
print('%0.1f Celsius is equal to %0.1f Fahrenheit'%(celsius,fahrenhiet))  


# Python Program to Check if a Number is Positive, Negative or 0

num =float(input("Enter the number to check for Positive/Negative/0: "))
if(num == 0):
    print('%0.d is ZERO'%(num))
elif(num >=0):
    print('%0.1f is POSITIVE Number'%(num))
else:
    print('%0.1f is NEGATIVE Number'%(num))


# Python Program to Check if a Number is Odd or Even

num =float(input("Enter the Number: "))
if(num%2==0):
    print('%0.d is even number'%(num))
else:
    print('%0.d is odd number'%(num))


# Python Program to Check Leap Year

year =input("Please enter year:")
if len(year)==4:
    year =int(year)
    if ((year%400==0)or((year%4==0)and(year%100!=0))):
        print("%d is a Leap Year" %year)
    else:
        print("%d is Not the Leap Year" %year)
else:
    print("please re-enter the valid year")


# Python Program to Find the Largest Among Three Numbers

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: ")) 
if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3
print("The largest number is",largest)


# Python Program to Check Prime Number

num = int(input("Enter The Number"))
if num > 1:
    for i in range(2,int(num/2)+1):
        if (num % i == 0):
            print(num, "is not a Prime Number")
            break
    else:
        print(num,"is a Prime number")
else:
    print(num,"is not a Prime number")


# Python Program to Print all Prime Numbers in an Interval

lower = int(input("Enter the lower bound:"))
upper = int(input("Enter the upper bound:"))
print("Prime numbers between %0.d and %0.d are"%(lower,upper))
for num in range(lower, upper + 1):   
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# Python Program to Find the Factorial of a Number

num =int(input("Enter number:"))
fact=1
while(num>0):
    fact=fact*num
    num=num-1
print("Factorial of given number is:",fact)

#method-II
import math  
num = int(input("Enter the number:"))  
print(math.factorial(num))


# Python Program to Display the multiplication Table

num =int(input('Enter the number for multiplication table: '))
upper =int(input('Enter the number of limit: '))
for i in range(1,upper+1):
    print(num, 'x', i, '=', num*i)


# Python Program to Check Armstrong Number

num =int(input("Enter a number: "))
add =0
temp =num
while temp>0:
    digit=temp%10
    add+=digit**3
    temp//=10
if num==add:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


# Python Program to Find Armstrong Number in an Interval

lower =int(input("Enter the lower bound:"))
upper =int(input("Enter the upper bound:"))
for num in range(lower, upper + 1):
    order =len(str(num))
    add =0
    temp =num
    while temp>0:
        digit=temp % 10
        add+=digit ** order
        temp//=10
    if num == add:
        print(num)


# Python Program to Find the Sum of Natural Numbers

num =int(input("Enter a number: "))
add =0
if(num>=0):
    while(num > 0):
        add=add+num
        num=num-1
    print("The sum of first n natural numbers is",add)
else:
    print("Enter the positive value")


# Python Program to Display Powers of 2 Using Anonymous Function

num =int(input("Enter the Total Number of Terms: "))
for i in range(num):
    print("2 ^", i, " is ", 2 ** i)


# Python Program to Find Numbers Divisible by Another Number

numn = int(input("Enter a Number (Numerator): "))
numd = int(input("Enter a Number (denominator): "))
if numn%numd==0:
    print("%0.d is divisible by %0.d"%(numn,numd))
else:
    print("%0.d is not-divisible by %0.d"%(numn,numd))


# Python Program to Convert Decimal to Binary, Octal and Hexadecimal

num =int(input("Enter the Decimal Value:   "))
print("The decimal value of", num, "is:")
print("Binary: ",bin(num))
print("Octal: ",oct(num))
print("Hexadecimal: ",hex(num))


# Python Program to Find ASCII Value of Character

alpha = input('Enter the Alphabet value:  ')
print('The ASCII value of ', alpha ,' is', ord(alpha))


# Python Program to Find HCF or GCD

num1 =int(input("Enter First Number:"))
num2 =int(input("Enter Second Number:"))
if num1 >num2:
    smaller =num2
else:
    smaller =num1
for i in range (1,smaller+1):
    if((num1%i == 0) and (num2%i == 0)):
        gcd =i
print('The GCD of',num1,'and',num2,'is',gcd)


# Python Program to Find LCM

num1 =int(input("Enter first number: "))  
num2 =int(input("Enter second number: "))  
print(lcm(num1,num2))
def lcm(num1,num2):
    if num1>num2:
        temp =num1
    else:
        temp =num2
    while(True):
        if((temp %num1 ==0)and(temp %num2 ==0)):
            lcm =temp
            break
        temp+=1
    return lcm


# Python Program to Find the Factors of a Number

num =int(input("Enter the value:"))
print_factors(num)
def print_factors(x):
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
        if x % i == 0:
            print(i)


# Python Program to Make a Simple Calculator

print("\n 1.addition \n 2.subraction \n 3.multiplication \n 4.disvision")
num =int(input("choose any of the above option like 1/2/3/4 for calculator operation:"))
if(num==1 or num==2 or num==3 or num==4):
    num1 =float(input("Enter the first number:"))
    num2 =float(input("Enter the second number:"))
    if num==1:
        print(num1+num2)
    elif num==2:
        print(num1-num2)
    elif num==3:
        print(num1*num2)
    else:
        print(num1/num2)
else:
    print("Please enter the correct option")


# Python Program to Shuffle Deck of Cards

import itertools, random
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)
for i in range(5):
    print(deck[i][0], "for", deck[i][1])


# Python Program to Display Calendar

import calendar
yy =int(input("Enter the year: ")) 
mm =int(input("Enter the month: ")) 
print(calendar.month(yy, mm))


# Python Program to Display Fibonacci Sequence Using Recursion

nterms =int(input("Enter the number"))  
if nterms <= 0:  
    print("Plese enter a positive integer")  
else:  
    print("Fibonacci sequence:")  
    for i in range(nterms):  
        print(recur_fibo(i))  
def recur_fibo(n):  
    if n <= 1:  
        return n  
    else:  
        return(recur_fibo(n-1) + recur_fibo(n-2))  


# Python Program to Find Sum of Natural Numbers Using Recursion

num =int(input("Enter an integer: "))
if num < 0:
    print("Enter a positive number")
else:
    print("The sum is",recur_sum(num))
def recur_sum(num):
    if num<= 1:
        return num
    else:
        return num+recur_sum(num-1)


# Python Program to Find Factorial of Number Using Recursion

num =int(input("Enter an integer: "))
print("Factorial of",num,"is",factorial(num))
def fact(n):
    return 1 if (n==1 or n==0) else n * fact(n - 1)


# Python Program to Convert Decimal to Binary Using Recursion

num = int(input("Enter an integer: "))
binary(num)
def binary(num):
    if num>1:
        binary(num//2)
    print(num % 2,end = '')


# Python Program to Add Two Matrices

m1 =[[6,2,3],[7,5,6],[7,8,9]]
m2 =[[6,6,1],[6,3,4],[3,6,1]]
m3 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        m3[i][j] = m1[i][j]+m2[i][j]
for final in m3:
    print(r)


# Python Program to Transpose a Matrix

m1 =[[1,8],[8,2],[3,6]]
m2 =[[0,0,0],[0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        m2[j][i] = m1[i][j]
for final in m2:
    print(r)


# Python Program to Multiply Two Matrices

m1 =[[1,2,3],[4,5,6],[7,8,9]]
m2 =[[12,11,10,9],[8,7,6,5],[4,3,2,1]]
m3 =[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(m1)):
    for j in range(len(m1[0])):
        for k in range(len(m2)):
            m3[i][j]+= m1[i][k]*m2[k][j]
for final in m3:
    print(final)


# Python Program to Check Whether a String is Palindrome or Not

string =input("Please enter your own String : ")
if(string == string[::-1]):
    print(string, "Palindrome String")
else:
    print(string, "is Not a Palindrome")


# Python Program to Remove Punctuations From a String

punctuations ='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string =input("Enter a string:")
new =""
for i in string:
    if i not in punctuations:
        new = new+i
print("Punctuation Free String:",new)


# Python Program to Sort Words in Alphabetic Order

string =input('Enter the sentence:')
words =[word.lower() for word in string.split()]
words.sort()
print("The sorted words are:")
for word in words:
    print(word)


# Python Program to Illustrate Different Set Operations

A ={1,2,3,4,5,6,7,8,9};
B ={1,2,7,9,};
print("Union",A | B)
print("Intersection",A & B)
print("Difference ",A - B)
print("Symmetric difference",A ^ B)


# Python Program to Count the Number of Each Vowel

vowels ='aeiou'
string =input("Enter the string: ")
string =string.casefold()
cnt ={}.fromkeys(vowels,0)
for char in string:
    if char in cnt:
        cnt[char] += 1
print(cnt)


# Python Program to Merge Mails

with open("C://Users/VarunNagendra/Desktop/dump.txt", 'r', encoding='utf-8') as names_file:
    with open("C://Users/VarunNagendra/Desktop/dump1.txt", 'r', encoding='utf-8') as body_file:
        body = body_file.read()
        for name in names_file:
            mail = "Hello " + name.strip() + "\n" + body
            with open(name.strip()+".txt", 'w', encoding='utf-8') as mail_file:
                mail_file.write(mail)


# Python Program to Find the Size (Resolution) of a Image

import PIL
from PIL import Image
img = PIL.Image.open("C://Users/VarunNagendra/Downloads/KPI.jpeg")
print(img.size)


# Python Program to Find Hash of File

import hashlib
with open("C://Users/VarunNagendra/Desktop/dump.txt","rb") as f:
    bytes = f.read() 
    readable_hash = hashlib.md5(bytes).hexdigest();
    print(readable_hash)


# Python Program to Create Pyramid Patterns

#pyramid-I
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")

#pyramid-II
rows = int(input("Enter number of rows: "))
ascii_value = 65
for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")    
    ascii_value += 1
    print("\n")

#pyramid-III
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("\n")

#pyramid-VI
rows = int(input("Enter number of rows: "))
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")

#pyramid-V
rows = int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    for j in range(0, i):
        print("* ", end=" ")   
    print("\n")

#pyramid-VII
rows = int(input("Enter number of rows: "))
k = 0
for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end="  ")
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
    k = 0
    print()

#pyramid-VIII
rows = int(input("Enter number of rows: "))
for i in range(rows, 1, -1):
    for space in range(0, rows-i):
        print("  ", end="")
    for j in range(i, 2*i-1):
        print("* ", end="")
    for j in range(1, i-1):
        print("* ", end="")
    print()


# Python Program to Merge Two Dictionaries

dict1 ={'a':1,'b':2}
dict2 ={'c':3,'d':4}
dict3 =dict1.update(dict2)
print(dict1)


# Python Program to Safely Create a Nested Directory

import os
os.makedirs("C:/Users/VarunNagendra/Desktop/training/Directory1/Directory2")


# Python Program to Access Index of a List Using for Loop

list1 = []
temp = int(input("Enter the number of elements : "))
for i in range(0,temp):
    list1.append(int(input()))
print(list1)
print()
print('The listed elements are from loop as')
for i in list1:
    print(i,end='\t')


# Python Program to Make a Flattened List from Nested List

list1 =[[1,2,3],[4,5,6], [7,8,9]]
list2 =[num for list3 in list1 for num in list3]
print(list2)


# Python Program to Slice Lists

list1 = [1,2,3,4,5,6,7,8,9]
print(list1[::-1])
print(list1[::1])
print(list1[2:6])
print(list1[6:4:-1])


# Python Program to Iterate Over Dictionaries Using for Loop

dict1={'name':'varun','age': 23,'company':'KPI'}
for idd,key in dict1.items():
    print(idd,':',key)


# Python Program to Sort a Dictionary by Value

dt = {1:500, 2:1000, 3:1500}
sort = {key: value for key, value in sorted(dt.items(), key=lambda item: item[1])}
print(sort)


# Python Program to Check If a List is Empty

list1 = []
temp = int(input("Enter the number of elements : "))
for i in range(0,temp):
    list1.append(int(input()))
print(list1)
print("Checking for list is empyt or not")
if(len(list1)==0):
    print('Null')
else:
    print('It is having objects')


# Python Program to Catch Multiple Exceptions in One Line

def division(a,b):
    try:
        print(a/b)
        if b==0:
            raise ZeroDivisionError('Division by zero')
        if b==1:
            raise ValueError('Should not use this function')
    except(ZeroDivisionError,ValueError) as e:
        print(e)                  
sample =division(20,5)
print(sample)


# Python Program to Copy a File

from shutil import copyfile
sample =copyfile("C://Users/VarunNagendra/Desktop/doughts.txt", "C://Users/VarunNagendra/Desktop/dump.txt")
print(sample)


# Python Program to Concatenate Two Lists

list1 = []
temp = int(input("Enter the number of elements for list1 : "))
for i in range(0,temp):
    list1.append(int(input()))
print(list1)

list2 = []
temp = int(input("Enter the number of elements for list2 : "))
for i in range(0,temp):
    list2.append(int(input()))
print(list2)
print('The concatenate of list1 and list2 is')
list3 =list1+list2
print(list3)


# Python Program to Check if a Key is Already Present in a Dictionary

dict1 = {1:'a',2:'b',3:'c'}
a =int(input("Enter the key value:"))
if a in dict1:
    print(a,"is present")
else:
    print(a,"is not present")


# Python Program to Split a List Into Evenly Sized Chunks

list1 = []
temp = int(input("Enter the number of elements for list1 : "))
for i in range(0,temp):
    list1.append(int(input()))
print(list1)
n=int(input('Enter the evenly size'))
print('The splitting of list into evenly sized chunks are as')
for i in range(0,len(list1),n):
    x=i
    print (list1[x:x+n])


# Python Program to Parse a String to a Float or Int

name =input("Enter a value: ")
print(name,type(name))
int_name = int(name)
print(int_name,type(int_name))
float_name = float(name)
print(float_name,type(float_name))


# Python Program to Print Colored Text to the Terminal

import colorama
from colorama import Fore,Back,Style
print(Fore.YELLOW + 'My name is varun')
print(Fore.RED + 'My name is varun')
print(Fore.GREEN + 'My name is varun')
print(Back.YELLOW + 'My name is varun')
print(Back.RED + 'My name is varun')
print(Back.GREEN + 'My name is varun')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('My name is varun')


# Python Program to Convert String to Datetime

from datetime import datetime
string =input('Enter the day ,month and year as like"dd-mm-yyyy"')
date = datetime.strptime(string, '%d-%m-%Y')
print(date)
print(type(date))


# Python Program to Get the Last Element of the List

list1 = []
temp = int(input("Enter the number of elements for list1 : "))
for i in range(0,temp):
    list1.append(int(input()))
print(list1)
print('The last element in the list is')
print(list1[-1])


# Python Program to Get a Substring of a String

list1 = []
temp = int(input("Enter the number of elements for list1 : "))
for i in range(0,temp):
    list1.append(int(input()))
print(list1)
x =int(input("Enter the substring initial index value: "))
y =int(input("Enter the substring last index value: "))
if(x >= 0 & y <= len(list1)):
    print(list1[x:y])
else:
    print('please enter the limited boundary')


# Python Program to Print Output Without a Newline

print("Hello guys",end =' ')
print("Welcome to KPI")


# Python Program Read a File Line by Line Into a List

with open("C://Users/VarunNagendra/Desktop/varun.txt") as test:
    line =test.readlines()
print(line)
print()
new_line =[x.strip() for x in line]
print(new_line)


# Python Program to Randomly Select an Element From the List

import random
list1 = []
temp = int(input("Enter the number of elements for list1 : "))
for i in range(0,temp):
    list1.append(int(input()))
print(list1)
n =int(input("Enter the random sample number"))
print(random.sample(list1 ,n))


# Python Program to Check If a String Is a Number (Float)

sample = input("Enter the number:")
print(sample ,type(sample))


# Python Program to Count the Occurrence of an Item in a List

list1 = []
temp = int(input("Enter the number of elements for list1 : "))
for i in range(0,temp):
    list1.append(int(input()))
print(list1)
cnt =int(input('Enter the list item for count: '))
cnt =list1.count(cnt)
print(cnt)


# Python Program to Append to a File

fin = open("C://Users/VarunNagendra/Desktop/dump.txt", "a")
fin.write('\n Welcome to KPI Partners');
fin.close()


# Python Program to Delete an Element From a Dictionary

dict1 = {'Name':'varun','age':23,'company':'KPI Partners'}
print(dict1)
del dict1['age']
print('After Deletion of element from the dictionary')
print(dict1)


# Python Program to Create a Long Multiline String

str1 ='''Hai Team Gd mng How are u...'''
print(str1)
str2 =('Hai Team\nGd mng \nHow are u...')
print(str2)


# Python Program to Extract Extension From the File Name

import os
f1 =os.path.splitext('C://Users/VarunNagendra/Desktop/dump.txt')
print(f1[1])


# Python Program to Measure the Elapsed Time in Python

import time
start = time.time()
print('Hello World')
end = time.time()
print(end-start)


# Python Program to Get the Class Name of an Instance

class bike:
    def name(self,name,cost):
        self.name = name
        self.cost = cost
b =bike()
print(b.__class__.__name__)


# Python Program to Convert Two Lists Into a Dictionary

listK =["Name","Age","Company"]
listV =['Varun','23','KPI']
res = {}
for key in listK:
    for value in listV:
        res[key] = value
        listV.remove(value)
        break
print(res)


# Python Program to Differentiate Between type() and isinastance()

print('type()')
temp ='hello world'
print(type(temp))
print('isinstance()')
temp =isinstance("hello world", (float, int, str, list, dict, tuple))
print(temp)


# Python Program to Trim Whitespace From a String

string =input("Enter any string:")
print(string.strip())


# Python Program to Get the File Name From the File Path

import os
name =os.path.basename("C://Users/VarunNagendra/Desktop/dump.txt")
print(name)


# Python Program to Represent enum

list1 =['apple','banana','cherry']
for i,j in enumerate(list1):
    print(i,j)


# Python Program to Return Multiple Values From a Function

def details():
    return "Varun",23
name ,age =details()
print(name)
print(age)


# Python Program to Get Line Count of a File

with open(r"C://Users/VarunNagendra/Desktop/dump.txt", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('Total Lines', count + 1)


# Python Program to Differentiate Between del, remove, and pop on a List

list1 =[1,2,3,4,5,6,7,8,9]
del list1[2]
print(list1)
list1.remove(4)
print(list1)
list1.pop(1)
print(list1)


# Python Program to Find All File with .txt Extension Present Inside a Directory

import glob, os
os.chdir("C://Users/VarunNagendra/Desktop")
for file in glob.glob("*.txt"):
    print(file)


# Python Program to Get File Creation and Modification Date

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("C://Users/VarunNagendra/Desktop/dump.txt")))
print("Created: %s" % time.ctime(os.path.getctime("C://Users/VarunNagendra/Desktop/dump.txt")))


# Python Program to Get the Full Path of the Current Working Directory

import os
print(os.getcwd())


# Python Program to Iterate Through Two Lists in Parallel

list1 = ['A','B','C']
list2 = [1,2,3,4,5,6,7,8,9]
for i, j in zip(list1, list2):
    print(i, j)


# Python Program to Check the File Size

file =os.stat('C://Users/VarunNagendra/Desktop/dump.txt')
print(file.st_size,'\t bytes')


# Python Program to Reverse a Number

num =int(input("Enter the Number "))
temp =num
rev = 0
while num != 0:
    dump =num % 10
    rev =rev * 10 +dump
    num //= 10
print("Reverse of",temp," is" ,rev)

#method -II
num =input("Enter the Number ")
rev=num[::-1]
print(rev)


# Python Program to Compute the Power of a Number

base =int(input("Enter the base value: "))
exp =int(input("Enter the exponential value: "))
power =base ** exp
print(base,'power',exp,'is',power )


# Python Program to Count the Number of Digits Present In a Number

num = int(input("Please Enter any Number: "))
cnt = 0
while(num > 0):
    num =num // 10
    cnt =cnt+ 1
print("Number of Digits in a Given Number = %d" %cnt)


# Python Program to Check If Two Strings are Anagram

str1 =input('Enter first string: ')
str2 =input('Enter second string: ') 
str1 =str1.lower()
str2 =str2.lower()
if(len(str1) ==len(str2)):
    sorted1 =sorted(str1)
    sorted2 =sorted(str2)
    if(sorted1 ==sorted2):
        print(str1,"and",str2,"are anagrams")
    else:
        print(str1,"and",str2,"are not anagrams")
else:
    print(str1,"and",str2,"are not anagrams")


# Python Program to Capitalize the First Character of a String

string =input("Enter the string: ")
print(string.capitalize())


# Python Program to Compute all the Permutation of the String

from itertools import permutations
string =input("Enter the string for permutations: ")
words = [''.join(i) for i in permutations(string)]
print(words)


# Python Program to Create a Countdown Timer

import time
seconds =int(input('Enter the time in seconds for countdown timer'))
print(seconds)
time.sleep(seconds)
print('welcome to the world!')

#method -II
import time
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('welcome to the world!')
t = input("Enter the time in seconds for countdown timer: ")
countdown(int(t))


# Python Program to Count the Number of Occurrence of a Character in String

cnt = 0
string =input('Enter the string:')
print(string)
char =input('Enter the character u want to count on the above string')
for i in string:
    if i ==char:
        cnt+= 1
print(cnt)


# Python Program to Remove Duplicate Element From a List

list1 = []
temp = int(input("Enter the number of elements for list1 : "))
for i in range(0,temp):
    list1.append(int(input()))
print('List having with duplicates ',list1)
new =[]
for i in list1:
    if i not in new:
        new.append(i)
print('List without having duplicates',new)


# Python Program to Convert Bytes to a String

byte = b"Hello welcome to the world!"  
print(type(byte))  
string = byte.decode('UTF-8')  
print(type(string))  
print(string)
