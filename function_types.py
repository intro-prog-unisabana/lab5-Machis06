def list_shift (datos, shift):
    for i in range(len(datos)):
        datos[i] = datos[i]+shift 

def calc_avg (datos):
    return sum(datos)/len(datos)

def print_normalized (datos):
    print(datos)
