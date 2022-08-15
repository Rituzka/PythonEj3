Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

nombre = 'Sarah'
apellido = 'Connor'
edad = 32
telefono = 6669783838
casada = false
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    casada = false
NameError: name 'false' is not defined. Did you mean: 'False'?
casada = False
hijos = True
email = sarahConnor@skynet.org
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    email = sarahConnor@skynet.org
NameError: name 'sarahConnor' is not defined
email = 'sarahConnor@skynet.org'
amigos = ['Michael Biehn', 'Arnold', 'John Connor']
peliculas = {'peli1': 'The Terminator', 'peli2': 'Predator', 'peli3': 'Star Wars'}

print(nombre)
Sarah
print(apellido)
Connor
print(edad)
32
print(telefono)
6669783838
print(casada)
False
print(hijos)
True
print(email)
sarahConnor@skynet.org
print(amigos)
['Michael Biehn', 'Arnold', 'John Connor']
print(peliculas)
{'peli1': 'The Terminator', 'peli2': 'Predator', 'peli3': 'Star Wars'}
