# El nombre del archivo donde contiene la clase
from lamp import Lamp

def run():
   lamp = Lamp(False)

   while True:
      command = str(input('''
         ¿Que desea hacer?
         
         [p]render
         [a]pagar
         [s]alir
         '''))

      if command == 'p':
         lamp.turnOn()
      elif command == 'a':
         lamp.turnOff()
      else:
         break

if __name__ == '__main__':
   run()