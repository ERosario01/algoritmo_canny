import pydicom
import cv2

# Cargar la imagen DICOM
ds = pydicom.dcmread('0009.DCM')

# Convertir la imagen DICOM a una matriz de numpy
img = ds.pixel_array[0]

# Mostrar la imagen original
cv2.imshow('Imagen original', img)

# Aplicar el algoritmo de Canny
edges = cv2.Canny(img, 100, 200)

# Mostrar la imagen después de aplicar el algoritmo de Canny
cv2.imshow('Imagen con algoritmo de Canny', edges)

# Esperar a que se presione una tecla para cerrar las ventanas
cv2.waitKey(0)
cv2.destroyAllWindows()