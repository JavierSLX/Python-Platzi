# -*- coding: utf-8 -*-

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
