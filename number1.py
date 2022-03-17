# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 11:07:23 2022

@author: user
"""
55
total=0
count=0
average=0

while True:

  try:
     num = input("Enter a number: ")

     num2 = float(num)

     count=count+1

     total=total+num2

  except:

    if num == 'done':


       break

    else:

      print ('Invalid Input')

  average = total/count

print(total)
print(count)
print(average)