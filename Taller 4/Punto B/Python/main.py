import cv2
import mediapipe as mp
import speech_recognition as sr
import threading
import pygame
import numpy as np

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Estado compartido
estado_gesto = {"mano_abierta": False, "dos_dedos": False}
ultimo_comando = ""
x = 100
color = (255, 255, 255)
mostrar = True

# Función para detectar gestos
def detectar_gestos():
    global estado_gesto
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        estado_gesto = {"mano_abierta": False, "dos_dedos": False}
        # Detección simple basada en landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                dedos_arriba = 0
                if hand_landmarks.landmark[8].y < hand_landmarks.landmark[6].y:
                    dedos_arriba += 1  # Índice
                if hand_landmarks.landmark[12].y < hand_landmarks.landmark[10].y:
                    dedos_arriba += 1  # Medio
                if hand_landmarks.landmark[16].y < hand_landmarks.landmark[14].y:
                    dedos_arriba += 1  # Anular
                if hand_landmarks.landmark[20].y < hand_landmarks.landmark[18].y:
                    dedos_arriba += 1  # Meñique
                if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
                    dedos_arriba += 1  # Pulgar (posición relativa)

                estado_gesto["mano_abierta"] = dedos_arriba >= 4
                estado_gesto["dos_dedos"] = dedos_arriba == 2

        cv2.imshow("Camara - Gesto", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Función para reconocimiento de voz
def reconocer_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            print("Escuchando comando...")
            audio = r.listen(source, timeout=3)
            texto = r.recognize_google(audio, language="es-ES")
            print("Comando reconocido:", texto)
            return texto.lower()
        except:
            return ""

def escuchar_voz():
    global ultimo_comando
    while True:
        comando = reconocer_comando()
        if comando:
            ultimo_comando = comando

pygame.init()
pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Interfaz Multimodal")
font = pygame.font.SysFont("Arial", 30)
reloj = pygame.time.Clock()

threading.Thread(target=detectar_gestos, daemon=True).start()
threading.Thread(target=escuchar_voz, daemon=True).start()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if estado_gesto["mano_abierta"]:
        if "cambiar" in ultimo_comando:
            color = (0, 0, 255)
        elif "rojo" in ultimo_comando:
            color = (255, 0, 0)
        elif "verde" in ultimo_comando:
            color = (0, 255, 0)

    if estado_gesto["dos_dedos"]:
        if "mover" in ultimo_comando:
            x = (x + 5) % 800
        elif "ocultar" in ultimo_comando:
            mostrar = False
        elif "mostrar" in ultimo_comando:
            mostrar = True

    # Renderizar escena
    pantalla.fill((0, 0, 0))
    if mostrar:
        pygame.draw.circle(pantalla, color, (x, 300), 50)
    texto = font.render(f"Comando: {ultimo_comando}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    reloj.tick(30)