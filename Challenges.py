import re
import heapq
str="str1025rts"
num=str.split()
print(num)
number=re.findall(r'\d+',str)
for i in number:
    print(max(i)) # To display highest number
list=[1,2,5,6,10,15,25]
top_two=heapq.nlargest(5,list)
print(top_two)


