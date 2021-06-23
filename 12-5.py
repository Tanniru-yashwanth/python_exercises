"""Make a Pygame file that creates an empty screen. In the event
loop, print the event.key attribute whenever a pygame.KEYDOWN event is detected.
Run the program and press various keys to see how Pygame responds."""

import pygame


class EmptyScreen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Printing the keys")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print(event.key)

            pygame.display.flip()


ei = EmptyScreen()
ei.run()