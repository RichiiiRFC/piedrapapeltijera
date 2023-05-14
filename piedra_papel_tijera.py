import random

PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERA = 'tijera'
opciones = [PIEDRA, PAPEL, TIJERA]
primeroGana = [[PAPEL, PIEDRA], [TIJERA, PAPEL], [PIEDRA, TIJERA]]
primeroPierde = [[PIEDRA, PAPEL], [PAPEL, TIJERA], [TIJERA, PIEDRA]]


def GenerarMovimientoOrdenador():
    movimiento = random.choice(opciones)
    return movimiento


def decidirGanador(usuarioMovimiento, ordenadorMovimiento):
    if [usuarioMovimiento, ordenadorMovimiento] in primeroGana:
        return 1
    elif [usuarioMovimiento, ordenadorMovimiento] in primeroPierde:
        return -1
    return 0


print("JUEGO : Piedra, papel y tijera")
while 1:
    comenzar = input("Quieres jugar? (s/n): ")
    if 's' in comenzar.lower():
        movimientoOrdenador = GenerarMovimientoOrdenador()
        while True:
            movimiento = input(
                "Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras) o TERMINAR(terminar): ").lower()
            if movimiento == "terminar":
                print("Tienes miedo?")
                break
            print(f"Elección del ordenador: {movimientoOrdenador}")

            if 'p' in movimiento or 'a' in movimiento or 't' in movimiento or 'p' in movimiento:
                if 'p' in movimiento:
                    usuarioMovimiento = PIEDRA
                elif 'a' in movimiento:
                    usuarioMovimiento = PAPEL
                elif 't' in movimiento:
                    usuarioMovimiento = TIJERA
                print(f"Elección del usuario: {usuarioMovimiento}")
                if decidirGanador(usuarioMovimiento, movimientoOrdenador) == 1:
                    print("Gana el usuario !!!")
                elif decidirGanador(usuarioMovimiento, movimientoOrdenador) == -1:
                    print("Gana el ordenador !!!")


            elif "terminar" in movimiento:
                break
            else:
                print("Entrada incorrecta. Vuelve a intentar.")
    elif 'n' in comenzar.lower():
        break
    else:
        print('Entrada incorrecta. Vuelve a intentar.')
    print()
