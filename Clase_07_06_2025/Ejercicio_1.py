class Persona:
    def __init__(self,nombre,ci,genero,edad):
        self.nombre = nombre
        self.ci = ci
        self.genero = genero
        self.edad = edad
        
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, CI: {self.ci} Genero: {self.genero} Edad: {self.edad}")
        
    def jugar(self):
        print(f" Esta jugando {self.nombre}")
    def comer(self):
        print(f" Esta comer {self.nombre}")
    def hablar(self):
        print(f" Esta hablar {self.nombre}")
    def andar(self):
        print(f" Esta andar {self.nombre}")


maria = Persona("Maria","999333","Mujer",19)
jose = Persona("Jose","555333","Masculino",32)
maria.mostrar_info()
jose.mostrar_info()
maria.jugar()
maria.comer()
jose.hablar()
jose.andar()
jose.comer()
        
