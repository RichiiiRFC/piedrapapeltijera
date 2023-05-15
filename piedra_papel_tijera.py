import random

PIEDRA = 'piedra'
PAPEL = 'papel'
TIJERA = 'tijera'
LAGARTO = 'lagarto'
opciones = [PIEDRA, PAPEL, TIJERA, LAGARTO]
primeroGana = [[PAPEL, PIEDRA], [TIJERA, PAPEL], [PIEDRA, TIJERA], [LAGARTO, PAPEL]]
primeroPierde = [[PIEDRA, PAPEL], [PAPEL, TIJERA], [TIJERA, PIEDRA], [LAGARTO, PIEDRA], [LAGARTO, TIJERA]]


def GenerarMovimientoOrdenador():
    """
    Esta función genera el movimiento del ordenador y lo devuelve
    :return:Str
    """
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
    nombre = input("Selecciona el nombre del jugador: ")
    intentos = int(input("Selecciona el numero de intetos: "))
    contador_ordenador = 0
    contador_usuario = 0
    usuarioMovimiento = ""
    if 's' in comenzar.lower():
        movimientoOrdenador = GenerarMovimientoOrdenador()
        for i in range(intentos):
            i += 1

            movimiento = input(
                "Selecciona un movimiento ('p' para piedra / 'a' para papel / 't' para tijeras / 'l' para lagarto) o TERMINAR(terminar): ").lower()
            if movimiento == "terminar":
                print("Tienes miedo?")
                break
            print(f"Elección del ordenador: {movimientoOrdenador}")

            if 'p' in movimiento or 'a' in movimiento or 't' in movimiento or 'p' in movimiento or 'l' in movimiento:
                if 'p' in movimiento:
                    usuarioMovimiento = PIEDRA
                elif 'a' in movimiento:
                    usuarioMovimiento = PAPEL
                elif 't' in movimiento:
                    usuarioMovimiento = TIJERA
                elif 'l' in movimiento:
                    usuarioMovimiento = LAGARTO
                print(f"Elección del usuario: {usuarioMovimiento}")
                if decidirGanador(usuarioMovimiento, movimientoOrdenador) == 1:
                    contador_usuario += 1

                elif decidirGanador(usuarioMovimiento, movimientoOrdenador) == -1:
                    contador_ordenador += 1

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

    if contador_usuario < contador_ordenador:
        print("Ha ganado" + str(nombre))

    elif contador_usuario > contador_ordenador:
        print("Ha ganado el ordenador")

    else:
        print("Ha habido un empate")
