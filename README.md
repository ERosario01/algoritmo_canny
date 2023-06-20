#Algoritmo Canny

El algoritmo de Canny es un algoritmo de detección de bordes automatizado que ha sido desarrollado para detectar los bordes de una imagen. El algoritmo trata de encontrar los bordes de los objetos en una imagen usando la variación de intensidad de los pixeles. El algoritmo consta de cinco pasos principales: limpieza de la imagen, aplicación del filtro de umbral, aplicación del filtro gradiente, aplicación del umbral y finalmente identificación de los bordes. El umbral se utiliza para determinar qué borde debe ser marcado y cuáles no, el filtro de gradiente se aplica para medir la pendiente de cada punto y determinar si está en el borde.
1. Convertir la imagen a escala de grises: El algoritmo de Canny funciona mejor en imágenes en escala de grises, por lo que el primer paso es convertir la imagen a escala de grises.
2. Aplicar un filtro gaussiano: El filtro gaussiano se utiliza para reducir el ruido en la imagen. El ruido puede afectar negativamente la detección de bordes.
3. Calcular los gradientes de la imagen en las direcciones x e y: Los gradientes de la imagen se calculan utilizando el operador Sobel. El operador Sobel es un filtro que se utiliza para detectar bordes en una imagen.
4. Calcular la magnitud del gradiente y la dirección del gradiente: La magnitud del gradiente se calcula utilizando la fórmula matemática para calcular la magnitud de un vector. La dirección del gradiente se calcula utilizando la fórmula matemática para calcular la dirección de un vector.
5. Aplicar la supresión no máxima: La supresión no máxima se utiliza para eliminar los píxeles que no son bordes. Esto se hace comparando la magnitud del gradiente en la dirección del gradiente con la magnitud del gradiente en la dirección perpendicular al gradiente. Si la magnitud del gradiente en la dirección del gradiente es mayor que la magnitud del gradiente en la dirección perpendicular al gradiente, el píxel se mantiene. De lo contrario, el píxel se elimina.
6. Aplicar la histéresis: La histéresis se utiliza para unir los bordes y eliminar los bordes débiles. La histéresis se realiza utilizando dos umbrales: un umbral alto y un umbral bajo. Los píxeles con una magnitud de gradiente mayor que el umbral alto se consideran bordes fuertes. Los píxeles con una magnitud de gradiente menor que el umbral bajo se consideran no bordes. Los píxeles con una magnitud de gradiente entre el umbral alto y el umbral bajo se consideran bordes débiles. Los bordes débiles se unen a los bordes fuertes si están conectados. Los bordes débiles que no están conectados a los bordes fuertes se eliminan.


##Artículo

https://www.revistas.uancv.edu.pe/index.php/RCIA/article/viewFile/865/741


###Resumen

Una potencialidad del Perú es la industria alimentaria, esto por la calidad y diversidad de sus insumos, se propone la detección de bordes mediante Canny para la estimación del tamaño de productos en una faja transportadora, esto para garantizar un tamaño mínimo del producto. Una aplicación evalúa continuamente imágenes de una cámara y al estímulo de un sensor de varilla o similar hace el cálculo de área. Se concluye que Canny, con una debida configuración puede realizar el trabajo adecuadamente.


####Referencias

1. Canny John (1986), A Computational Approach to Edge Detection, IEEE TRANSACTIONS ON PATTERN ANALYSIS AND MACHINE INTELLIGENCE, VOL. PAMI-8, NO. 6, NOVEMBER 1986
2. Redmon Joseph, Farhadi Ali (2018), YOLOv3: An Incremental Improvement, arXiv:1804.02767v1 [cs.CV] 8 Apr 2018
3. Himani Singh Rana, Himanshu Sirohia (2018), Comparative Study Between Canny and Sobel Edge Detection Techniques, EIJO Journal of Engineering, Technology And Innovative Research (EIJO–JETIR) (2018)
4. Ehsan Akbari Sekehravani, Eduard Babulak, Mehdi Masoodi (2020), Implementing canny edge detection algorithm for noisy image, Bulletin of Electrical Engineering and Informatics Vol. 9, No. 4, August 2020, pp. 1404~1410
