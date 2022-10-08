class Ejercicio12:

	def __init__(self, diccionario):
		self.diccionario = diccionario

	def edadDiccionario(self,nombre):
		pos=0
		for i in self.diccionario['Alumnos']:
			if i==nombre:
				edad=self.diccionario['Edad'][pos];
			pos+=1
		return edad

	def claveDiccionario(self,clave):
		for j in self.diccionario.keys():
			if j==clave:
				return True
		return False

	def tipoDiccionario(self,valor):
		lista=self.diccionario.get(valor)
		tipo=type(lista)
		longitud=len(lista)
		texto="El valor es de tipo: " +str(tipo)+" y de longitud: "+ str(longitud)
		return texto

	def setDiccionario(self):
		lista=self.diccionario["Edad"]
		s=set(lista)
		return s

	@staticmethod
	def ejecutar():
		dic_ejemplo = {
		'Alumnos': ["Carlos", "Ana", "Daniela", "Martín"],
		'Curso': "Big Data",
		'Edad': ('22', '21', '20', '22'),
		'Presencial': True
		}
		ejercicio12 = Ejercicio12(dic_ejemplo)
		edad=ejercicio12.edadDiccionario("Daniela")
		print(edad)
		esta=ejercicio12.claveDiccionario('Centro')
		print(esta)
		tipo=ejercicio12.tipoDiccionario("Curso")
		print(tipo)
		se=ejercicio12.setDiccionario()
		print(se)

if __name__=="__main__":
	Ejercicio12.run()