from collections import Counter
#list1 = [1,1,2,3,4,4,5]
#reversed = list1[:-1][::-1]
#print(reversed)
#list1.sort(reverse=True)
#print(list1[:-1])
#print(min(list1))

#frequency_counter=Counter(list1)
#print(frequency_counter)

#print(max(list1)-1)
array1=['anitha','srikanth']
array2=['dharvi','aaryan']
array3=array1+array2
print(array3)

str="MalayalaM"
i,j=0,len(str)-1
is_palen=1
while i< j:
    if str[i] != str[j]:
        print(str[i],str[j])
        is_palen=0
        break
    print(str[i],str[j])
    i=i+1
    j=j-1
if(is_palen):
    print("True")
else:
    print("False")






"""
for x in list1:
    if a/2 in list1:
        print(f"{a} 'is Even Number'")
    else:
        print(f"{a}  'is Odd Number'")
"""
