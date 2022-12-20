#10.Keep only numbers from the following string x = “ 89e9jcd^o38829@3%3,/mkl$w1”
x = "89e9jcd^o38829@3%3,/mkl$w1"
import re
numbers=re.findall('\d+',x)
print(numbers)
