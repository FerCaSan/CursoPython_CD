import turtle


def main():
	#Abre ventana
	window = turtle.Screen()
	fer = turtle.Turtle()

	#Debe recibir la tortuga para poder ejecutarla
	make_square(fer)

	#Para que no se cierre la ventana
	turtle.mainloop()

def make_square(fer):
	#1. El programa espera hasta que yo de Enter para dibujar la línea
	#input()

	#2.El programa espera a recibir un valor
	length = int(input('Ingrese tamaño: ')) 

	#2. range genera una serie de valores, Aquí hará 4 veces lo que le indicamos 
	for i in range(4):
		#1.
		#make_line_and turn(fer, 100)

		#2.El tamaño es ingresado por el usuario
		make_line_and_turn(fer, length)
	
def make_line_and_turn(fer,length):
	fer.forward(length)
	fer.left(90)


#Si el nombre de este archivo lo llama main, ejecuta las funciones dentro primero
if __name__ == '__main__':
	main()