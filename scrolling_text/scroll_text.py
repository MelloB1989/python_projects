import sys
import os
import time
#x = "This is a scrolling text example, there's more text and more text and 10 times more text just to make this string longer for the text some more some more and then done"
x = input("Enter the sentence: ")
limit = int(input("Enter the limit of text to be displayed: "))
delay = float(input("Enter the delay: "))
def scrollTxt(text, limit, delay):
   i = 0
   while (i != len(text)):
       os.system("clear")
       sys.stdout.write(text[i : (i+limit)])
       sys.stdout.flush()
       i = i + 1
       time.sleep(delay)

scrollTxt(x, limit, delay)
