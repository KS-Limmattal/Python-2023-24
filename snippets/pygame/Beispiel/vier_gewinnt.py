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
from playground import Stein, Playground, WINDOW_HEIGHT, WINDOW_WIDTH, BLACK, WHITE

# Variablen/KONSTANTEN setzen
FPS = 60  # angepeilt werden ebenso viele Bildschirmaktualisierungen pro Sekunde.

class Game:
    def __init__(self):
        # pygame Modul initialisieren
        pygame.init()

       # einen neues Fenster öffnen und mit Titel versehen
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Vier Gewinnt!")

        # Uhr wird zum regelmässigen Updaten der Graphik verwendet
        self.clock = pygame.time.Clock()

        # Spielobjekte (Instanzen) erzeugen. Gleichartige Spielobjekte können in Listen abgelegt werden.
        self.playground = Playground(num_rows = 5, num_cols=7, size=160)

        # Weitere Eigenschaften initialisieren
        self.turn = Stein.FIRST

    # Spielschleife
    def run_game_loop(self):
        while True:
            # Überprüfen, ob Benutzer eine Aktion durchgeführt hat. Dazu werden die Ereignisse (events) abgefragt:
            for event in pygame.event.get():
                # Beenden bei [ESC] oder [X]
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
                ):
                    return

                # Weitere Reaktionen auf Benutzereingaben
                if event.type == pygame.KEYDOWN and (
                    pygame.K_1 <= event.key <= pygame.K_1 + self.playground.num_cols - 1
                ):
                    col = event.key - pygame.K_1
                    if self.playground.is_full(col):
                        print(f"Column {col} is already full")
                    else:
                        self.playground.add(col, self.turn)
                        print(self.playground)
                        indices = self.playground.check_finish()
                        if len(indices) > 0:
                            self.screen.fill(WHITE)
                            self.playground.draw(self.screen)
                            self.playground.highlight(self.screen, indices)
                            return self.turn
                        self.turn = -self.turn

            # Spiellogik (z.B. Bewegungen der Spieler)

            # Spielplayground löschen (mit weissem oder schwarzem Hintergrund)
            self.screen.fill(WHITE)

            # Aktualisiertes Spielfeld/Figuren zeichnen
            self.playground.draw(self.screen)

            # Bildschirminhalt aktualisieren
            pygame.display.flip()
            self.clock.tick(FPS)


    # Ausstiegschleife
    def run_exit_loop(self):
        while True:
            event = pygame.event.wait()
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                pygame.quit()
                sys.exit()

    def get_screen(self):
        return self.screen


if __name__ == "__main__":
    game = Game()
    result = game.run_game_loop()
    if result:
        player = "Der Anziehende" if result == Stein.FIRST else "Der Nachziehende"
        font = pygame.font.SysFont(None, 48)
        img = font.render(f"{player} gewinnt", True, BLACK)
        game.get_screen().blit(img, (20, 20))
        pygame.display.flip()
        game.run_exit_loop()
    else:
        pygame.quit()
        sys.exit()
