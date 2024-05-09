import pygame
import sys

from pygame import Surface

from src.core.game_state import NEW_GAME_EVENT, ID_MAIN_MENU, ID_NEW_GAME_MENU
from src.menu.menu_manager import MenuManager

""" 
This is the main Game Loop - it is the central component of every game,
It is responsible for updating the game logic every frame, controlling the frame rate, and rendering
graphics accordingly. 
"""


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Krigenheim")
        pygame.mixer.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.running = True
        self.game_state = GameState(self.screen)
        self.game_state.start()  # Perform the startup tasks

    """ This function is where everything happens.
     All roads lead back to our loop here."""

    def run(self):
        while self.running:
            self.handle_event()
            self.update()
            self.render()
            # self.print_fps()
            self.clock.tick(60)

    def handle_event(self):
        self.game_state.handle_events(self.quit)

    def update(self):
        self.game_state.update()

    def render(self):
        self.screen.fill((0, 0, 0))
        self.game_state.render()
        pygame.display.set_caption("Krigenheim / " + f"Current FPS: {self.clock.get_fps():.2f}")
        pygame.display.flip()

    def print_fps(self):
        print(f"Current FPS: {self.clock.get_fps():.2f}")  # Print the current FPS rounded to two decimal places

    def quit(self):
        pygame.quit()
        sys.exit()


class GameState:
    MENU_ACTIVE = 1
    GAME_RESUMED = 2
    GAME_PAUSED = 3

    def __init__(self, screen: Surface):
        self.current_state = None
        self.screen = screen
        self.menu_manager = MenuManager(self.screen)

    def start(self):
        print("GameState initialized...")
        self.menu_manager.activate_menu(ID_MAIN_MENU)
        self.current_state = self.MENU_ACTIVE

    def update(self):
        if self.current_state == self.MENU_ACTIVE:
            # Delegate the logic to menu_manager (which keeps track of menus and issues their state changes)
            self.menu_manager.update()
            pass
        elif self.current_state == self.GAME_RESUMED:
            # Logic for game state changes goes here
            pass
        elif self.current_state == self.GAME_PAUSED:
            # Logic for freezing the game state goes here
            pass
        else:
            # Default case
            pass
        pass

    def render(self):
        self.menu_manager.render(self.screen)

    def handle_events(self, quit_callback):
        for event in pygame.event.get():
            self.menu_manager.handle_event(event)
            if event.type == pygame.QUIT:
                quit_callback()