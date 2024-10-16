class Cola:
    def __init__(self):
        self.new_cola=[]
    
    def añadir_cola(self, datoF):
        self.new_cola.append(datoF)

    def quitar_cola(self):
        if len(self.new_cola)!=0:
            return self.new_cola.pop(0)
        else: 
            return None
    def vacia(self):
        return len(self.new_cola)==0
        
def sumar_numeros_cola(colaA, colaB):
    resultado_cola=Cola()
    print("\nCola A        Cola B           Resultado")
    while not colaA.vacia() and not colaB.vacia():
        valor_colaA=colaA.quitar_cola()
        valor_colaB=colaB.quitar_cola()
        resultado_cola= valor_colaA + valor_colaB
        print(f" {valor_colaA:<7}  +     {valor_colaB:<7}   =     {resultado_cola:<5}")
    return resultado_cola

def datos_cola(nombre):
    cola=Cola()
    tamaño=int(input(f"Ingrese el tamaño de la cola {nombre}: "))
    for _ in range(tamaño):
        valor_cola=int(input(f"Ingrese los valores para la cola {nombre}: "))
        cola.añadir_cola(valor_cola)
    return cola

colaA= datos_cola("Cola A")
colaB= datos_cola("Cola B")
resultado_cola= sumar_numeros_cola(colaA, colaB)




