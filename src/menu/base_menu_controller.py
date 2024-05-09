from typing import Dict

from src.core.game_object import GameObject


class BaseMenuController:
    def __init__(self, screen):
        self.screen = screen
        self.menu_objects: Dict[int, GameObject] = {}

    def add_object(self, game_object: GameObject):
        self.menu_objects[id(game_object)] = game_object  # Use object's ID as the key

    def build_menu(self):
        pass

    def handle_event(self, event):
        pass

    def update(self):
        pass

    def destroy(self):
        pass

    def render(self, screen):
        pass
