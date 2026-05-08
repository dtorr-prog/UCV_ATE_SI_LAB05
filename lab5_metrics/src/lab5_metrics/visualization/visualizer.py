
import cv2
import matplotlib.pyplot as plt

def generar_histograma(path: str):

    imagen = cv2.imread(path, 0)

    plt.hist(imagen.flatten(), bins=50)

    plt.title("Histograma")

    plt.show()

generar_histograma("data/2222.png")