from pygame import Surface

from src.core.game_state import NEW_GAME_EVENT, ID_MAIN_MENU, ID_NEW_GAME_MENU, ID_LOAD_GAME_MENU, ID_OPTIONS_MENU, \
    MAIN_MENU_EVENT
from src.core.object_manager import ObjectManager
from src.menu.base_menu_controller import BaseMenuController
from src.menu.main.main_menu_presenter import MainMenuController
from src.menu.main.new_game_presenter import NewGameController


class MenuManager(ObjectManager):
    def __init__(self, screen: Surface):
        super().__init__()
        self.screen = screen
        self.active_menu = None  # Tracks the currently active menu
        self.presenter: BaseMenuController = None

    def activate_menu(self, menu_id):
        """ Activate a specific menu by ID """
        self.active_menu = menu_id
        self.start()  # Start or restart the menu

    def deactivate_current_menu(self):
        """ Deactivate the currently active menu """
        if self.active_menu:
            self.active_menu = None

    """This function is executed when menu_manager calls activate_menu, which specifies which menu
        this function should build. Each menu should have it's own Controller class
        (e.g NewGameController, etc.)"""
    def start(self):
        if self.active_menu == ID_MAIN_MENU:
            self.presenter = MainMenuController(self.screen)
        elif self.active_menu == ID_NEW_GAME_MENU:
            self.presenter = NewGameController(self.screen)
        elif self.active_menu == ID_LOAD_GAME_MENU:
            pass
        elif self.active_menu == ID_OPTIONS_MENU:
            pass

        self.presenter.build_menu()

    def handle_event(self, event):
        self.presenter.handle_event(event)
        if event.type == MAIN_MENU_EVENT:
            self.destroy()
            self.activate_menu(ID_MAIN_MENU)
        elif event.type == NEW_GAME_EVENT:
            self.destroy()
            self.activate_menu(ID_NEW_GAME_MENU)

    def update(self):
        self.presenter.update()

    def destroy(self):
        self.active_menu = None
        self.presenter.destroy()

    def render(self, screen):
        self.presenter.render(screen)
