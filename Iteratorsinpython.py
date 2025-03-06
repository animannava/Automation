class MyNumbers:

  def forloop(self):
      for a in (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24):
          print(a)
  def whileloop(self):
      i=0
      while i<20:
          i=i+1
          print(i)

myclass = MyNumbers()
#myiter = iter(myclass)
myclass.forloop()
myclass.whileloop()
#for x in myiter:
#  print(x)