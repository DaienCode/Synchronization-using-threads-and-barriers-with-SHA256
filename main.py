#Author: Jesus David Nieves Hernandez - T00058742
import threading
import hashlib
import time

class Runner(threading.Thread):
    def __init__(self, name, barrier):
        super().__init__()
        self.name = name
        self.barrier = barrier

    def run(self):
        start_time = time.time()
        print(f'{self.name} comienza a correr.')
        i = 0
        while True:
            text = self.name + str(i)
            sha256 = hashlib.sha256(text.encode()).hexdigest()
            if sha256[:4] == '0000':
                end_time = time.time()
                print(f'{self.name} ha encontrado una cadena: {text}')
                print(f'{self.name} tomó {end_time - start_time:.2f} segundos')
                break
            i += 1
        self.barrier.wait()
        print(f'{self.name} ha cruzado la barrera y ha terminado la carrera.')

def execute_code():
    barrier = threading.Barrier(3)
    runners = [
        Runner('Hugo', barrier),
        Runner('Paco', barrier),
        Runner('Luis', barrier)
    ]
    for runner in runners:
        runner.start()

    while threading.active_count() > 1:
      time.sleep(0.1)

    print('La carrera ha terminado')

def validate_code():
    print("Validando...")
    
    pass

if __name__ == '__main__':
    while True:
        print("1. Ejecutar código")
        print("2. Validar código")
        print("3. Salir")
        
        option = input("Elige una opción: ")
        
        if option == "1":
            execute_code()
            
        elif option == "2":
            validate_code()
            
        elif option == "3":
            break