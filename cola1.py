class Cola:
    def __init__(self):
        self.new_cola = []
    
    def añadir_cola(self, datoF):
        self.new_cola.append(datoF)

    def quitar_cola(self):
        if len(self.new_cola) != 0:
            return self.new_cola.pop(0)
        else: 
            return None
    
    def vacia(self):
        return len(self.new_cola) == 0

    def mostrar(self):
        return self.new_cola

def sumar_numeros_cola(colaA, colaB):
    resultado_cola = Cola() 
    
    print(f"\nCola A original: {colaA.mostrar()}")
    print(f"Cola B original: {colaB.mostrar()}")
    
    while not colaA.vacia() and not colaB.vacia():
        valor_colaA = colaA.quitar_cola()
        valor_colaB = colaB.quitar_cola()
        suma = valor_colaA + valor_colaB
        
        resultado_cola.añadir_cola(suma)
        
        print(f"\nSuma de {valor_colaA} + {valor_colaB} = {suma}")
        print(f"Cola A después de la suma: {colaA.mostrar()}")
        print(f"Cola B después de la suma: {colaB.mostrar()}")
        print(f"Cola resultante hasta el momento: {resultado_cola.mostrar()}")
    
    return resultado_cola

def datos_cola(nombre):
    cola = Cola()
    tamaño = int(input(f"Ingrese el tamaño de la cola {nombre}: "))
    for _ in range(tamaño):
        valor_cola = int(input(f"Ingrese los valores para la cola {nombre}: "))
        cola.añadir_cola(valor_cola)
    return cola

colaA = datos_cola("Cola A")
colaB = datos_cola("Cola B")

resultado_cola = sumar_numeros_cola(colaA, colaB)
print(f"\nCola resultante final: {resultado_cola.mostrar()}")

