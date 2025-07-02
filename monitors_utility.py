import mss

def listar_monitores():
    with mss.mss() as sct:
        monitores = sct.monitors[1:]  # ignora [0], que representa todos os monitores
    return monitores