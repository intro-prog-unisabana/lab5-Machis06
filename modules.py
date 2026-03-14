import os
import math 
directorio = os.getcwd()
print("Current working directory:", directorio)

num = int(input("Enter an integer:"))
valor_log = math.log2(num)
print("Log base 2 of", num, "is:", valor_log)

floor = math.floor(valor_log)
ceil = math.ceil(valor_log)

print("Floor:", floor)
print("Ceiling:", ceil)


