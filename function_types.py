def list_shift (valores, shift):
    for i in range(len(valores)):
        valores[i] = valores[i]+shift 

def calc_avg (valores):
    return sum(valores)/len(valores)

def print_normalized (valores):
    print(valores)
