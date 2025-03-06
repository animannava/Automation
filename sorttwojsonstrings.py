import json
import math

emp1='{"Name":"Anitha","age":39,"Location":"Charlotte","Salary":100000}'
emp2='{"Name":"Srikanth","age":42,"Location":"Charlotte","Salary":120000}'
sal=[json.loads(emp1).get("Salary"),json.loads(emp2).get("Salary")]
print(sal)
sal.sort(reverse=True)
print(sal)



