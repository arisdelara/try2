# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 12:08:51 2022

@author: user
"""

largest = None
smallest = None
while True:

  try:
     num = input("Enter a number: ")
     num2 = float(num)


     if smallest is None or num < smallest:
      smallest = num
     if largest is None or num > largest:
      largest = num
  except:
    if num == 'done':
      break
    else:
      print ('Invalid Input')
      continue

print("Minimum:",smallest)
print("Maximum:",largest)