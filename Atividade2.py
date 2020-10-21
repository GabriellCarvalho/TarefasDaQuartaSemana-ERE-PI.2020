# -*- coding: utf-8 -*-

import cv2
from matplotlib import pyplot as plt

#Função para mostrar imagem 
def showImg(img, blur):
   plt.subplot(121),plt.imshow(img),plt.title('Original')
   plt.xticks([]), plt.yticks([])
   plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
   plt.xticks([]), plt.yticks([])
   plt.show()
   

#Filtro da Média (Averaging)
def blur(img):
    x = int(input('Valor X: '))
    y = int(input('Valor Y: '))
    blur = cv2.blur(img, (x,y))
    return blur

#Filtro Gaussiano (Gaussian Filtering)
def gaussianBlur(img):
    x = int(input('Valor X: '))
    y = int(input('Valor Y: '))
    gaussianBlur = cv2.GaussianBlur(img, (x,y), cv2.BORDER_DEFAULT)
    return gaussianBlur    

#Filtro da Mediana (Median Filtering)
def medianBlur(img):
    a = int(input('Valor: '))
    medianBlur = cv2.medianBlur(img, a)
    return medianBlur

#Filtro Sobel (Sobel Derivatives)
def sobel(img):
    sobel = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=5)
    return sobel
    
#Filtro Laplaciano (Laplacian Derivatives)
def laplacian(img):
    laplacian = cv2.Laplacian(img,cv2.CV_64F)
    return laplacian


#Carrega a imagem
image = cv2.imread("imagem2.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) 

print('Filtro da Média(1)\nFiltro Gaussiano(2)\nFiltro da Mediana(3)\nFiltro Sobel(4)\nFiltro Laplaciano(5)')

while True:
    i = int(input('Escolha um filtro: '))
    if i == 1:
        newImage = blur(image)
        break
    elif i == 2:
        newImage = gaussianBlur(image)
        break
    elif i == 3:
        newImage = medianBlur(image)
        break
    elif i == 4:
        newImage = sobel(image)
        break
    elif i == 5:
        newImage = laplacian(image)
        break
    else: print('Invalido')
   
showImg(image, newImage)
cv2.destroyAllWindows()
