# Ejercicio 3 — Segmentando el Mundo (Binarización y Contornos)

**Breve explicación**

Se desarrolló un sistema en Python usando OpenCV para segmentar, detectar y clasificar figuras geométricas en imágenes. El flujo consiste en cargar una imagen, aplicar umbralización (fija y adaptativa), detectar contornos, calcular métricas (área, perímetro, centroide) y clasificar cada figura usando criterios robustos de circularidad y geometría. Los resultados se visualizan en un GIF animado que muestra cada paso del proceso y la clasificación final de las figuras.

**GIF animado**

![GIF de clasificación de figuras](shapes_result.gif)

En el GIF se observa:
- La imagen original,
- Las etapas de segmentación,
- La detección de contornos,
- La clasificación de cada figura con su nombre en inglés, área, perímetro y centroide.

**Enlace al código/notebook**

[Notebook de Colab con el código](Taller_2_Punto_3_Visual.ipynb)

**Comentarios personales**

El sistema logra distinguir figuras como cuadrados, círculos, triángulos, octágonos, etc., mostrando los resultados de forma clara y visual. El reto principal fue asegurar que los círculos no fueran confundidos con polígonos y que los cuadrados/rectángulos no se clasificaran incorrectamente por ruido o forma. Los criterios de circularidad y ángulos internos fueron clave para mejorar la precisión. Como mejora futura, se puede ajustar más la circularidad ya que hay casos en los que sigue clasificando de manera erronea la figura.

**Dependencias y cómo ejecutar**

**Ambiente: Python (Colab/Jupyter)**
- Instalar dependencias:
  ```bash
  pip install opencv-python numpy pillow
  ```
- Ejecutar el notebook y subir la imagen cuando se solicita.
- El código está optimizado para Colab y Jupyter, mostrando el GIF de todo el flujo y permitiendo descargarlo como evidencia.
