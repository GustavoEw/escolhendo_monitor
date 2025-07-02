import mss
import mss.tools as save # type: ignore
import os



def screeshot_save(imagem):
    name =input("digite o nome do arquivo(sem extensão): ").strip()
    if not name:
        print("nome invalido! 'screeshot.png'")
        name="screenshot"

    os.makedirs("prints",exist_ok=True)

    name = tratamento(name)

    caminho = os.path.join("prints", name)
    save.to_png(imagem.rgb, imagem.size, output=caminho)
    print(f"Screanshot salvo como: {caminho}")

def tratamento(name):
    if not name.lower().endswith(".png"):
        name += ".png"
    return name
