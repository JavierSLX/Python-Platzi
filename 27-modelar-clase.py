# -- coding: utf-8 --

class Lamp:

   LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

   # Constructor
   def __init__(self, isTurnedOn):
      self.isTurnedOn = isTurnedOn

   def turnOn(self):
      self.isTurnedOn = True
      self._displayImage()

   def turnOff(self):
      self.isTurnedOn = False
      self._displayImage()
   
   def _displayImage(self):
      if self.isTurnedOn:
         print(self.LAMPS[0])
      else:
         print(self.LAMPS[1])


def run():
   lamp = Lamp(False)

   while True:
      command = str(raw_input('''
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