**Ejercicio 4 — Imagen = Matriz (Canales, Slicing, Histogramas)**

**Breve explicación**

Se realizó una exploración práctica sobre la manipulación de imágenes como matrices utilizando Python y OpenCV. Se separaron los canales de color (RGB y HSV), se editaron regiones mediante slicing, se generaron histogramas de intensidad y se ajustó brillo/contraste de forma manual e interactiva. El objetivo fue comprender cómo los datos de una imagen pueden tratarse como arrays y modificarse directamente, visualizando los efectos en tiempo real.

**GIF animado**

![GIF de procesamiento y edición de imagen](04_imagen_matriz_pixeles/Ejecucion.gif)

En el GIF se observa la imagen original, la edición de regiones, y la comparación de histogramas antes y después de los cambios.

**Enlace al código/notebook**

[Notebook de Colab con el código](04_imagen_matriz_pixeles/04_imagen_matriz_pixeles.ipynb)

**Comentarios personales**

Se aprendió que trabajar con imágenes como matrices facilita la manipulación directa de píxeles y regiones. El mayor reto fue adaptar el código para que funcione con imágenes de cualquier tamaño y asegurar que los cambios visuales fueran claros. Como mejora futura, se podrian agregar opciones para seleccionar regiones mediante interfaz gráfica y aplicar operaciones más avanzadas (como máscaras o blending entre zonas).

**Dependencias y cómo ejecutar** 
 
**Ambiente: Python (Colab/Jupyter)**
- Instalar dependencias:  
  ```bash
  pip install opencv-python numpy matplotlib ipywidgets
  ```
- Ejecutar el notebook y subir la imagen cuando se solicita.  
- El código es compatible con Colab y Jupyter; permite edición interactiva de brillo/contraste y descarga de resultados.