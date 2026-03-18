import os
import math


directorio = os.getcwd()
print("Current working directory:", directorio)

num = int(input("Enter an integer: "))

log_val = math.log2(num)
print("Log base 2 of", num, "is:", log_val)

print("Floor:", math.floor(log_val))
print("Ceiling:", math.ceil(log_val))