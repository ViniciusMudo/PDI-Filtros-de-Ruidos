import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

def main():
    directory = "imagens/ruidosas/"

    imagens = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.png', '.jpeg'))]

    while True:
        print("Escolha uma das imagens a seguir:")
        for idx, img in enumerate(imagens):
            print(f"{idx + 1}: {img}")

        escolha = input(f"Digite o número da imagem (1-{len(imagens)}) ou 0 para sair: ")
        if escolha == '0':
            print("Encerrando o programa...")
            break

        try:
            escolha = int(escolha)
            if 1 <= escolha <= len(imagens):
                file_name = imagens[escolha - 1]
                path = os.path.join(directory, file_name)
                break
            else:
                print("Escolha inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    image_before = cv2.imread(path, 0)
    image_after_mediana = filtro_mediana(image_before)
    exibe_mediana(image_before, image_after_mediana)

def filtro_mediana(image):
    [altura, largura] = image.shape
    output = np.copy(image)
    for i in range(1, altura - 1):
        for j in range(1, largura - 1):
            region = image[i - 1:i + 2, j - 1:j + 2]

            region_flat = []
            for m in range(3):
                for n in range(3):
                    region_flat.append(region[m, n])

            region_flat.sort()
            mediana = region_flat[4]
            output[i, j] = int(mediana)

    return output

def exibe_mediana(im_in, im_out):
    cv2.imshow('Imagem Original', im_in)
    cv2.imshow('Imagem Filtro Mediana 3x3', im_out)

    plt.subplot(121)
    plt.title('Histograma Original')
    plt.xlabel('niveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(im_in.ravel(), bins=256, range=[0, 255])

    plt.subplot(122)
    plt.title('Histograma Filtro Mediana 3x3')
    plt.xlabel('niveis de cinza')
    plt.ylabel('qtde de pixels')
    plt.hist(im_out.ravel(), bins=256, range=[0, 255])

    plt.show()
    cv2.waitKey(0)

main()