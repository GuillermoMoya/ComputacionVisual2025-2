# Taller Integral de Computación Visual Avanzada — Resultados (Punto G)

**Autores:** Guillermo Moya Romero, Maria Paula Román Arévalo, Samuel Reyes Benavides, Santiago García Rodríguez  
**Fecha:** yyyy-mm-dd

---

## 1. Resumen / Objetivo (Punto G)
Este README consolida las evidencias, resultados y pasos para ejecutar los módulos entregados en el taller y presenta las capturas, GIFs y videos generados.  
El objetivo de este punto G es **documentar y publicar** los resultados para subir al repositorio del proyecto.

---

## 2. Estructura del repositorio (sugerida)
```

yyyy-mm-dd_super_taller_cv/
├── PuntoA/
├── PuntoB/
├── PuntoC/
├── PuntoD/
├── PuntoE/
├── PuntoF/
└── README.md                 # <- este archivo

````

---

# 3. Índice
- [4. Instalación y ejecución rápida](#4-instalación-y-ejecución-rápida)  
- [5. Punto A — Percepción y Visión](#5-punto-a--percepción-y-visión)  
- [6. Punto B — Interacción Multimodal](#6-punto-b--interacción-multimodal)  
- [7. Punto C — Visualización 3D (Unity + Python)](#7-punto-c--visualización-3d-unity--python)  
- [8. Punto D — Backend y Comunicación](#8-punto-d--backend-y-comunicación)  
- [9. Punto E — Deep Learning](#9-punto-e--deep-learning)  
- [10. Punto F — Optimización Visual](#10-punto-f--optimización-visual)    
- [11. Integrantes](#13-integrantes)

---

# 4. Instalación y ejecución rápida

> **Requisitos generales**  
> - Python 3.9+  
> - Git  
> - Unity 2021/2022 LTS (Punto C)  
> - Webcam y micrófono (si se requiere interacción en tiempo real)

### 4.1 Clonar el repositorio
```bash
git clone https://github.com/<usuario>/<repo>.git
cd yyyy-mm-dd_super_taller_cv
````

### 4.2 Crear entorno Python (recomendado)

```bash
python -m venv venv
source venv/bin/activate     # Linux / macOS
venv\Scripts\activate        # Windows
```

### 4.3 Instalar dependencias (ejemplo)

Cada submódulo incluye su `requirements.txt`.
Ejemplo para Punto A:

```bash
pip install -r PuntoA/requirements.txt
```

---

# 5. Punto A — Percepción y Visión

## 5.1 Objetivo

Implementar detección en tiempo real con YOLOv8, visualización de bounding boxes, filtros por clase y cálculo de FPS.

## 5.2 Ejecución

```bash
cd PuntoA
python detect_realtime.py
```

Funcionalidades del archivo:

* Captura frames desde webcam.
* Ejecuta `model.predict()` usando YOLOv8.
* Dibuja cajas, muestra FPS, aplica filtros (`f`) y finaliza (`q`).

## 5.3 Dependencias principales

* ultralytics
* opencv-python
* torch

## 5.4 Evidencias

![Resultado A1](./Punto%20A/a1.png)
![Resultado A2](./Punto%20A/a2.png)


---

# 6. Punto B — Interacción Multimodal

## 6.1 Objetivo

Fusionar gestos con MediaPipe + comandos de voz para activar acciones visuales en tiempo real (Pygame), con simulación de EEG.

## 6.2 Ejecución

```bash
cd PuntoB
pip install -r requirements.txt
python multimodal_main.py
```

`multimodal_main.py` contiene:

* Detección de manos con MediaPipe.
* Reconocimiento de voz en hilo independiente.
* Interacción voz + gestos.
* Visualización del estado en Pygame.

## 6.3 Tabla de combinaciones (ejemplo)

| Gesto        | Comando voz | Acción                    |
| ------------ | ----------- | ------------------------- |
| Mano abierta | "rojo"      | Cambiar color a rojo      |
| Dos dedos    | "mover"     | Mover objeto a la derecha |

## 6.4 Evidencias

![Resultado B1](./Punto%20B/a1.png)
![Resultado B2](./Punto%20B/a2.png)
![Resultado B3](./Punto%20B/a3.png)
![Resultado B4](./Punto%20B/a4.png)

---

# 7. Punto C — Visualización 3D (Unity + Python)

## 7.1 Objetivo

Integrar detecciones de Python (YOLO/MediaPipe) con una escena 3D en Unity usando archivos JSON.

## 7.2 Flujo de arquitectura

```
Python -> JSON (person_data.json) -> Unity -> Cambios en escena
```

## 7.3 Ejecución

### **Python**

```bash
cd PuntoC/python
pip install -r requirements.txt
python generar_json.py
```

### **Unity**

* Abrir proyecto en `PuntoC/unity`.
* Escena contiene el script `MonitorVisual.cs`.
* Unity lee continuamente el JSON y actualiza:

  * Color de esferas (según cantidad de personas detectadas).
  * Escala de cubos (según número de dedos detectados).

## 7.4 Evidencias

![Resultado C1](./Punto%20C/GifUnity.gif?raw=true)

# 8. Punto D — Backend y Comunicación

## 🎯 Objetivo
Implementar un sistema de comunicación capaz de:
- Transmitir detecciones, métricas y eventos entre subsistemas.
- Serializar información en JSON.
- Registrar métricas en CSV.
- Mostrar un dashboard en tiempo real (FPS, uso de CPU/GPU).
- Visualizar estados del sistema en una interfaz continua.

Este módulo sirve como puente entre:
**Visión (Python) → Visualización 3D / Dashboard → Archivos JSON/CSV**

---

## ⚙️ Arquitectura General
```

Detección (YOLO/MediaPipe)
│
├── JSON (estado actual)
├── CSV (métricas históricas)
└── WebSocket Server (flujo continuo)
↓
Dashboard en Python

````

---

## 🖥️ Implementación

### 1. **Servidor WebSocket**
Un servidor en Python que envía:
- Conteo de personas
- FPS del sistema
- Número de dedos detectados
- Tiempos de inferencia

Ejemplo simplificado:

```python
import asyncio
import websockets
import json

async def enviar_datos(websocket):
    while True:
        payload = {
            "personas": personas_detectadas,
            "dedos": dedos_arriba,
            "fps": fps_actual
        }
        await websocket.send(json.dumps(payload))
        await asyncio.sleep(0.05)

async def main():
    async with websockets.serve(enviar_datos, "localhost", 8000):
        await asyncio.Future()

asyncio.run(main())
````

---

### 2. **Serialización (JSON + CSV)**

#### JSON — estado instantáneo

Actualizado ~20 veces por segundo.

```json
{
    "personas": 2,
    "dedos": 3,
    "fps": 18.4,
    "timestamp": "2025-11-27T14:22:10"
}
```

#### CSV — historial de métricas

Ejemplo:

```
timestamp,fps,uso_cpu,uso_gpu
2025-11-27 14:22:10,17.4,32,18
2025-11-27 14:22:11,18.2,30,17
```

---

### 3. **Dashboard de Métricas**

El dashboard (en Tkinter o Matplotlib) muestra:

* Gráfica en tiempo real del FPS.
* Uso de CPU y GPU (con `psutil`).
* Estado de detecciones.

---

## 📊 **Resultados**

Se observan los siguientes resultados:

* Dashboard en tiempo real mostrando FPS dinámico.
* Gráfica del rendimiento del sistema en diferentes momentos.
* Tabla de valores de latencia e inferencia.
* Mapa de eventos enviados por WebSocket.
* JSON y CSV actualizándose correctamente durante toda la ejecución.

![Resultado D](./Punto%20D/D1.png)

---

# 9. Punto E — Deep Learning

## 🎯 Objetivo

Entrenar una red neuronal convolucional (CNN) desde cero y realizar:

* Validación cruzada.
* Análisis de métricas.
* Fine-tuning usando modelos preentrenados (ResNet/MobileNet).
* Comparación entre modelos.

---

## 🧠 Modelos Implementados

### 🔹 1. CNN desde cero (Keras)

* 3 capas convolucionales
* MaxPooling
* Dropout
* Dense final con softmax


* Gráfica de *loss* vs *val_loss*
* Matriz de confusión
* Accuracy final aproximada ~85–90%

---

### 🔹 2. Fine-Tuning con MobileNetV2

* Congelación inicial de capas base.
* Reentrenamiento del *head classifier*.
* Learning rate bajo (1e-4).

Resultados incluidos:

* Accuracy superior al modelo base.
* Mejor generalización en validación.

---

### 🔹 3. Comparación entre modelos

| Modelo         | Accuracy | Tiempo de Entrenamiento | Observaciones          |
| -------------- | -------- | ----------------------- | ---------------------- |
| CNN desde cero | ~85%     | Medio                   | Tiende a overfitting   |
| MobileNetV2    | ~92%     | Bajo                    | Buen balance           |
| ResNet50 FT    | ~94%     | Alto                    | Mejor precisión global |

## 📊 **Resultados**

![Resultado E1](./Punto%20E/E1.png)
![Resultado E2](./Punto%20E/E2.png)
![Resultado E3](./Punto%20E/E3.png)
![Resultado E4](./Punto%20E/E4.png)

---

# 10. Punto F — Optimización Visual

## 🎯 Objetivo

Aplicar técnicas de optimización para mejorar la experiencia visual en Unity/Three.js:

* Niveles de detalle (LOD)
* Compresión de texturas
* Reducción de polígonos
* Optimización de sombras y luces
* Medición de FPS y latencia general

---

## 🧩 Técnicas Aplicadas

### 🔹 1. Niveles de detalle (LOD)

Modelos con:

* LOD0 (alta resolución)
* LOD1 (media)
* LOD2 (baja)

Unity cambia automáticamente según distancia a cámara.

---

### 🔹 2. Compresión de Texturas

Formatos usados:

* ASTC (Android)
* DXT5/BC7 (PC)

Impacto observado:

* Reducción de tamaño: **30–60%**
* Carga más rápida de materiales.

---

### 🔹 3. Reducción de polígonos

Se utilizaron herramientas como Blender Decimate y Unity MeshSimplify.

Resultados:

* Modelos reducidos entre **40% y 70%** sin pérdida visible.

---

### 🔹 4. Optimización de Iluminación

* Se desactivaron sombras innecesarias.
* Se reemplazaron luces dinámicas por *baked lighting*.
* Reducción de cálculos por frame.

---

## 📊 Resultados

Incluyen:

* Gráfica de FPS antes/después.
* Comparación de tamaño de texturas.
* Perfilador de Unity marcando:

  * Tiempo de frame,
  * Batch count,
  * SetPass calls.

![Resultado F](./Punto%20F/F1.png)
![Resultado F](./Punto%20F/F2.png)
![Resultado F](./Punto%20F/F3.png)
---

### Integrantes

* **Guillermo Moya Romero**
* **Maria Paula Román Arévalo**
* **Samuel Reyes Benavides**
* **Santiago García Rodríguez**