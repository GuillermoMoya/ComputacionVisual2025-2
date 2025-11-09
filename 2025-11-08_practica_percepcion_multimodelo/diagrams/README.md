# Diagramas del Pipeline

## Contenido Requerido

### pipeline.drawio.png
Diagrama del flujo completo mostrando:
- Input: imagen o frame de video
- Etapa 1: YOLO (detección → bbox)
- Etapa 2: SAM (bbox → máscara)
- Etapa 3: MiDaS (profundidad relativa del objeto)
- Etapa 4: MediaPipe (control gestual)
- Output: overlay con bbox, máscara y etiqueta de distancia

## Herramientas Sugeridas
- Draw.io (https://app.diagrams.net/)
- Lucidchart
- Microsoft Visio
- O cualquier herramienta de diagramación

## Instrucciones
1. Crear el diagrama mostrando el flujo de datos
2. Incluir tiempos aproximados por etapa
3. Exportar como .png
4. Opcionalmente guardar también el archivo .drawio fuente
