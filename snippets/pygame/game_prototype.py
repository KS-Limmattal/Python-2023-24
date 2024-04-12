# -*- coding: utf-8 -*-
"""
Dies ist ein Grundgerüst für Spiele, die das pygame-Modul verwenden.
Nach dem Initialiseren des Moduls wird eine Spielschleife (game loop) gestartet, 
welche nur durch Benutzer-Aktion (wie Esc, Schliessen des Fensters) beendet wird.
In der Spielschleife wird in regelmässigen zeitlichen Abständen auf die
Benutzereingaben reagiert und der Zustand der Spielobjekte sowie der
Bildschirminhalt aktualisiert.
"""

# Importieren des pygame-Moduls sowie weiterer Module und Klassen
import pygame
import sys

# Variablen/KONSTANTEN setzen
FPS = 60  # angepeilt werden ebenso viele Bildschirmaktualisierungen pro Sekunde.
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
WHITE = (255, 255, 255)
RED = (255, 0 , 0)

class Game:
    def __init__(self):
        # pygame Modul initialisieren
        pygame.init()

       # einen neues Fenster öffnen und mit Titel versehen
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Mein Titel")

        # Uhr wird zum regelmässigen Updaten der Graphik verwendet
        self.clock = pygame.time.Clock()

        # Spielobjekte (Instanzen) erzeugen. Gleichartige Spielobjekte können in Listen abgelegt werden.

        # Weitere Eigenschaften initialisieren, z.B.
        self.pos = 0  # Position einer Kugel 

    # Spielschleife
    def run_game_loop(self):
        while True:
            # Überprüfen, ob Benutzer eine Aktion durchgeführt hat. Dazu werden die Ereignisse (events) abgefragt:
            for event in pygame.event.get():
                # Beenden bei [ESC] oder [X]
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    return

                # Weitere Reaktionen auf Benutzereingaben

            # Spiellogik (z.B. Bewegungen der Spieler), z.B.
            self.pos += 5

            # Spielplayground löschen (mit weissem oder schwarzem Hintergrund)
            self.screen.fill(WHITE)

            # Aktualisiertes Spielfeld/Figuren zeichnen, z.B.
            pygame.draw.circle(self.screen, RED, (self.pos % WINDOW_WIDTH, self.pos % WINDOW_HEIGHT), 20)

            # Bildschirminhalt aktualisieren
            pygame.display.flip()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    result = game.run_game_loop()
    # Verarbeite evtl. Rückgabewert result
    pygame.quit()
    sys.exit()
