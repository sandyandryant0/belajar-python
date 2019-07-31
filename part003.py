# num = -1

# if num > 0:
# 	print("Positive number")
# elif num == 0:
# 	print("Zero")
# else:
# 	print("Negative number")

# if False:
# 	print("I am inside the body of if.")
# 	print("I am also inside the body of if.")
# print("I am outside the body of if.")

# n = 100

# sum = 0
# i = 1

# while i <= n:
# 	sum = sum + i
# 	i = i+1

# print("The sum is ", sum)


# numbers = [6, 5, 3, 8, 4, 2]
# sum = 0

# for val in numbers:
# 	sum  = sum + val

# print("The sum is ", sum)

# for val in "string":
# 	if val  == "r":
# 		break
# 	print(val)

# print("The End")

# for val in "string":
# 	if val  == "r":
# 		continue
# 	print(val)

# print("The End")

#Pas Sequence

# sequence = {'p', 'a', 's', 's'}
# for val in sequence:
# 	pass

# Function and method

# def print_lines():
# 	print("I am line1.")
# 	print("I am line2.")


# print_lines()

# def add_numbers(a, b):
# 	sum = a + b
# 	return sum


# result = add_numbers(4, 5)
# print(result)


# def calc_factorial(x):
# 	if x == 1:
# 		return 1
# 	else:
# 		return (x * calc_factorial(x - 1))

# num = 4
# print("The factorial of ", num, "is ",calc_factorial(num))

# square = lambda x:x ** 2
# print(square(100))

# import example

# output = example.add(4, 5.5)

# print(output)

# import math

# result = math.log2(5)
# print(result)

# from math import pi
# print("The value of pi is ", pi)

# with open("test.txt", "w", encoding = 'utf-8') as f:
# 	f.write("my first file\n")
# 	f.write("This file\n\n")
# 	f.write("contains three lines\n")


# import sys

# randomList = ['a', 0, 2]

# for entry in randomList:
# 	try:
# 		print("The entry is ", entry)
# 		r = 1 / int(entry)
# 		break
# 	except:
# 		print("Oops!", sys.exc_info()[0], "occured.")
# 		print("Next extry.")
# 		print()


# print("The reciprocal of", entry, "is", r)


# Class and object

# class MyClass:
# 	"This is my class"
# 	a = 10
# 	def func(self):
# 		print('hello')


# print(MyClass.a)
# print(MyClass.func)
# print(MyClass.__doc__)


# obj1 = MyClass()
# print(obj1.a)

# obj2 = MyClass()
# print(obj1.a + 5)

# class ComplexNumber:

# 	def __init__(self, r = 0, i = 0):
# 		self.real = r
# 		self.imag = i

# 	def getData(self):
# 		print("{0}+{1}j".format(self.real, self.imag))


# c1 = ComplexNumber(2, 3)
# c1.getData()

# c2 = ComplexNumber()
# c2.getData()

# class Mamal:
# 	def displayMamalFeatures(self):
# 		print("Mamal is a warm-blooded animal.")

# class Dog(Mamal):
# 	def displayDogFeatures(self):
# 		print("Dog has 4 legs")


# d = Dog()
# d.displayMamalFeatures()
# d.displayDogFeatures()

# my_list = [4, 7, 0, 3]
# my_iter = iter(my_list)

# print(next(my_iter))
# print(next(my_iter))

def print_msg(msg):
	def printer():
		print(msg)
	return printer

another = print_msg("Hello")
another()














