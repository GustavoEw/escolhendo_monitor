import 0 # type: ignore
def screenshot(monitors,indice):
    with mss.mss() as sct:
        imagem=sct.grab(monitors[indice-1])
        
        return imagem