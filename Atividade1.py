# -*- coding: utf-8 -*-

import cv2

def onChange(value):
    #print('valor alterado', value)
    pass

#Carregar a imagem
image = cv2.imread('imagem.png', 0)

#Cria uma janela
cv2.namedWindow('image')

#Criaando Trackbar para os valores do threshold
cv2.createTrackbar('threshold', 'image', 255, 255, onChange)
cv2.createTrackbar('threshold2', 'image',0,255, onChange)

while True:
    
    #Obtendo os valores do trackbar
    thresholdValue = cv2.getTrackbarPos('threshold', 'image')
    thresholdValue2 = cv2.getTrackbarPos('threshold2', 'image')
    
    #Aplicando a limiarização
    _,imageThreshold = cv2.threshold(image, int(thresholdValue2), int(thresholdValue), cv2.THRESH_BINARY)
    
    #Mostrando a imagem    
    cv2.imshow('image',imageThreshold)
    
    #Sair do loop precionando a tecla (Esc)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()


