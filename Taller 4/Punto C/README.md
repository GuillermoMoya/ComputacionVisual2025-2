# 🧪 Punto C – Visualización 3D Interactiva (Unity + Python)

Este módulo corresponde al **Punto C: Visualización 3D** del **Taller Integral de Computación Visual Avanzada**.  
Implementa una experiencia en la que una escena 3D en Unity **reacciona dinámicamente** a los datos generados por un sistema de visión por computador construido en Python.

La integración se realiza mediante un archivo JSON compartido en tiempo real, donde Python envía información de detección (personas y manos), y Unity actualiza objetos 3D según esos datos.

---

# 🎯 Objetivo del Subsistema (Punto C)

Diseñar una **escena 3D reactiva en Unity** que:

- Cambie **color**, **escala** o **animaciones** de objetos según datos externos.
- Reciba información procesada por Python utilizando **YOLOv8** y **MediaPipe**.
- Mantenga comunicación continua mediante archivos JSON o rutas compartidas.
- Sirva como demostración del módulo de **visualización 3D** dentro del taller integral.

Este subsistema opera como parte del ecosistema del taller o como módulo independiente.

---

# 🧩 Arquitectura General del Módulo

```
Python (detección de personas y manos)
        ↓ JSON en tiempo real
Unity (visualización 3D reactiva)
```

### 🔵 Python
- Captura la webcam.
- Detecta personas con **YOLOv8**.
- Cuenta dedos con **MediaPipe Hands**.
- Exporta continuamente un archivo:
  ```
  person_data.json
  ```
- Contiene campos: personas detectadas, dedos levantados, resolución del frame.

### 🟣 Unity
- Lee el JSON generado por Python usando lectura compartida.
- Modifica:
  - **Color de dos esferas** según número de personas.
  - **Escala de dos cubos** según número de dedos levantados.
- Lanza automáticamente el script de Python al presionar *Play*.
- Detiene el proceso de Python al cerrar el proyecto.

---

# 📂 Estructura del Repositorio

```
PuntoC/
├── python/
│   └── generar_json.py
├── unity/
│   ├── Assets/
│   │   └── MonitorVisual.cs
│   └── ProjectSettings/
└── README.md
```

---

# 🖥️ Python – Detección en Tiempo Real

### Tecnologías utilizadas

- `opencv-python`
- `ultralytics` (YOLOv8)
- `mediapipe`
- `json`, `os`, `time`

### Funcionalidad

- Abre la webcam usando OpenCV.
- Detecta personas (bounding boxes + conteo).
- Detecta manos y calcula dedos levantados.
- Actualiza el archivo `person_data.json` ~10–20 veces por segundo.
- Renderiza texto en la imagen mostrando:
  ```
  Personas detectadas: X
  Dedos levantados: Y
  ```

---

# 🎮 Unity – Visualización 3D Reactiva

### Herramientas usadas

- Unity 2022 LTS  
- C#  
- Lectura de JSON con acceso compartido  
- Modificación en tiempo real de materiales y escalas  

### Lógica del script `MonitorVisual.cs`

- Abre automáticamente el script Python al presionar *Play*.
- Lee continuamente el archivo JSON:
  ```json
  {
    "person_count": 1,
    "finger_count": 4,
    "frame_width": 1280,
    "frame_height": 720
  }
  ```
- Modifica la escena:

#### 🎨 Cambios de color por detección de personas

| Personas | Color |
|---------|--------|
| 0       | blanco |
| 1       | verde  |
| 2       | rojo   |
| ≥3      | amarillo |

#### 📏 Cambios de escala por cantidad de dedos

```
escala = 1 + (dedos * 0.8)
```

Dos cubos aumentan o disminuyen de tamaño según la detección.

---

# 🟢 Resultados del Subsistema

- Integración funcional entre Python y Unity.
- Escena 3D que responde en ~1 segundo a los cambios detectados.
- Uso de `FileShare.ReadWrite` para evitar bloqueos del JSON.
- Comunicación totalmente automatizada: Unity inicia y detiene Python.
- Ejemplo completo de módulo para el Punto C (visualización 3D).

GIF de demostración incluida en el repositorio.

![Detección ejemplo](./GifUnity.gif?raw=true)

---

# 🌟 Mejoras Opcionales (no implementadas pero sugeridas)

- Reemplazar archivo JSON por WebSockets (menor latencia).
- Activar animaciones, físicas o partículas según gestos.
- Conectar con otros puntos del taller (voz, EEG, CNN, AR.js).
- Migrar escena hacia Three.js para modalidad web.


## 👥 Integrantes

- Guillermo Moya Romero

-	Maria Paula Roman Arevalo

-	Samuel Reyes Benavides

-	Santiago Garcia Rodriguez