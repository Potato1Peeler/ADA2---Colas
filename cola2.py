class Cola:
    def __init__(self):
        self.cola={}
    
    def entrada_clientes(self, serv ,num_identificador):
        if serv not in self.cola:
            self.cola[serv] = []

        self.cola[serv].append(num_identificador)
        print(f"Cola {serv}: {self.cola[serv]}")
        return num_identificador
    
    def atender_clientes(self, serv):
        if serv not in self.cola or len(self.cola[serv]) == 0:
            print("No hay clientes en la cola de este servicio ")
        else:
            cliente_atendido=self.cola[serv].pop(0)
            print(f"Atendiendo al cliente c{cliente_atendido} del servicio {serv}")
            print(f"Cola {serv}: {self.cola[serv]}")
            return cliente_atendido


def sistema():
    cola_servicio=Cola()
    generar_codigo=0
    while True:
        cliente= input("Elija una opcion C (Registrar clientes) o A (Antender clientes) o 'salir': ")
        if cliente.lower() == "salir":
            break
        eleccion, serv = cliente.split()
        serv=int(serv)
        
        if eleccion.upper() == "C":
            generar_codigo+=1
            cola_servicio.entrada_clientes(serv, generar_codigo)
            print(f"Cliente c{generar_codigo} agregado al servicio {serv} ")
            

        elif eleccion.upper()== "A":
            cola_servicio.atender_clientes(serv)
        else:
            print("Opcion invalida")

print("Servicios: 1, 2, 3")
sistema()
