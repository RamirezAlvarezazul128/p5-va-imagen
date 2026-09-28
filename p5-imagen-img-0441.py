import cv2
print(cv2.__version__)
# leer la imagen con cv2 = computer vision
img = cv2.imread("jirafa azulita.jpg")
# determinar el tipo de imagen numpy.ndarray
print(type(img))
# imprimir imagen
print(img.shape)
# mostrando imagen en ventana barra de titulo
cv2.imshow('jirafa azulita 0441', img)
## tiempo de espera
cv2.waitKey(0)
# destruir todas las ventanas
cv2.destroyAllWindows()