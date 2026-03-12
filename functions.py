a = float(input(f"ingrese nota:"))
b = float(input(f"ingrese nota:"))
c = float(input(f"ingrese nota:"))

def promedio_estudiante (a, b, c):
    suma = a+b+c
    promedio = suma/3
    return promedio
resultado = promedio_estudiante(a,b,c)
print(f"promedio: {resultado:.2f}")




