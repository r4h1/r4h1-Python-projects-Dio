# Código para transformar uma imagem colorida em tons de cinza e binaria

import cv2
from google.colab.patches import cv2_imshow

# Carrega a imagem
image = cv2.imread('image_test1.jpg')  # Substitua pelo caminho da sua imagem

# Verifica se a imagem foi carregada corretamente
if image is None:
    print("Erro: Não foi possível ler a imagem.")
else:
    # Converte para escala de cinza (0 a 255)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Converte para imagem binária (0 e 255)
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

    # Exibe as imagens
    print("Imagem Original:")
    cv2_imshow(image)

    print("Imagem em Tons de Cinza:")
    cv2_imshow(gray_image)

    print("Imagem Binarizada (Preto e Branco):")
    cv2_imshow(binary_image)
