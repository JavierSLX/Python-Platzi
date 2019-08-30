# -*- coding: utf-8 -*-
import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._printContact(contact)
                break
        else:
            self._noFound(name)

    def update(self, name):
        for id, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                name = str(raw_input('Agregue el nombre nuevo: '))
                phone = str(raw_input('Agregue el telefono nuevo: '))
                email = str(raw_input('Agregue el correo nuevo: '))
                self._contacts[id] = Contact(name, phone, email)
                print('Elemento actualizado correctamente!')
                self._save()

    def delete(self, name):
        # enumerate nos da el indice del elemento y el elemento como tal
        for id, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[id]
                print('Elemento {} eliminado'.format(name))
                self._save()
                break

    def showAll(self):
        for contact in self._contacts:
            self._printContact(contact)

    # Guardamos los datos en disco duro
    def _save(self):
        with open('contactos.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def _printContact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _noFound(self, name):
        print('********')
        print('Elemento {} no encontrado!'.format(name))
        print('********')

def run():

    contactBook = ContactBook()

    # Lee el archivo de datos
    with open('contactos.csv', 'r') as f:
        reader = csv.reader(f)
        
        # Accedemos a cada fila
        for id, row in enumerate(reader):
            if id == 0 or len(row) == 0:
                continue
            else:
                contactBook.add(row[0], row[1], row[2])

    while True:
        command = str(raw_input('''
            Que deseas hacer?
            
            [a]niadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
            Opcion: '''))

        if command == 'a':
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el telefono del contacto: '))
            email = str(raw_input('Escribe el email del contacto: '))
            contactBook.add(name, phone, email)

        elif command == 'ac':
            name = str(raw_input('Escriba el nombre del contacto a actualizar: '))
            contactBook.update(name)

        elif command == 'b':
            name = str(raw_input('Escriba el nombre del contacto a buscar: '))
            contactBook.search(name)

        elif command == 'e':
            name = str(raw_input('Escriba el nombre del contacto a eliminar: '))
            contactBook.delete(name)

        elif command == 'l':
            contactBook.showAll()

        elif command == 's':
            break
        else:
            print('Comando no encontrado')

if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()