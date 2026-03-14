from utils import *
mensaje = input("Please type your message\n")
mensaje_invertido = flip(mensaje)
cantidad_a = count_letters(mensaje, "a")
mensaje_codificado = mensaje_invertido + ("a" * cantidad_a)
print("Your ecoded message is:", mensaje_codificado)