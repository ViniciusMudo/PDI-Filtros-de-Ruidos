import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def main():
    directory = "imagens/ruidosas/"

    imagens = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.png', '.jpeg'))]

    print("Escolha uma das imagens a seguir:")
    for idx, img in enumerate(imagens):
        print(f"{idx + 1}: {img}")

    while True:
        escolha = input(f"Digite o número da imagem (1-{len(imagens)}) ou 0 para sair: ")
        if escolha == '0':
            print("Encerrando o programa...")
            return
        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(imagens):
                file_name = imagens[escolha - 1]
                break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    image_before = cv2.imread(os.path.join(directory, file_name), 0)
    image_after_media = filtro_media(image_before)
    exibe_media(image_before, image_after_media)


def filtro_media(image):
    [altura, largura] = image.shape
    output = np.copy(image)
    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            region = image[i - 1:i + 2, j - 1:j + 2]

            soma = np.int32(0)
            for m in range(3):
                for n in range(3):
                    soma += region[m, n]


            valor_medio = soma // 9
            valor_medio = max(0, min(valor_medio, 255))
            output[i, j] = int(valor_medio)
    return output


def exibe_media(imin, imout):
    cv2.imshow('Imagem Original', imin)
    cv2.imshow('Imagem Filtro Media 3x3', imout)

    plt.subplot(121)
    plt.title('Histograma Original')
    plt.xlabel('niveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imin.ravel(), bins=256, range = [0, 255])

    plt.subplot(122)
    plt.title('Histograma Filtro Media 3x3')
    plt.xlabel('niveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(imout.ravel(), bins=256, range = [0, 255])

    plt.show()
    cv2.waitKey(0)

main()