# -*- coding: utf-8 -*-
"""omar task 3 session1 .py

Original file is located at
    https://colab.research.google.com/drive/1eQ1vijOOVEnJoEQzA7Re9AcaohmPj09r
"""
# ‼️👇👇الكود بيبدا من هنا
number = input("Enter a number: ")

print("As a string:", number)

try:
    print("As an integer:", int(number))
except :
    print("Cannot convert to integer.")

try:
    print("As a float:", float(number))
except :
    print("Cannot convert to float.")
