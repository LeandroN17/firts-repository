import random

name = "leandro"
lastname = "Navarrete"

intentos = 0
minn = 1
maxn = 20
pc = random.randint(minn, maxn)
print(f"Hello! {name} {lastname}")
print("run game")
print(f"{name} estoy pensando en un numero")

while intentos < 5:
    print("Ingresa tu numero")
    minumero = input("$ ")
    minumero = int(minumero)

    intentos += 1
    if minumero < pc:
        print("tu numero es muy bajo")
    if minumero > pc:
        print("mmm es muy alto")
    if minumero == pc:
        break
if minumero == pc:
    print("Ganaste!!!")
else:
    print("Perdites")
