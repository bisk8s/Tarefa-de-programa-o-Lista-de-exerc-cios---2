# -*- coding: utf-8 -*-
num = float(input('entre um número:'))

fizz = num % 3 == 0
buzz = num % 5 == 0

if fizz and buzz:
  print("FizzBuzz")
else:
  print(num)