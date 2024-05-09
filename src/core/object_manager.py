from typing import Dict
from src.core.game_object import GameObject


class ObjectManager:
    def __init__(self):
        self.game_objects: Dict[int, GameObject] = {}  # Changed to a dictionary

    def add_object(self, game_object: GameObject):
        self.game_objects[id(game_object)] = game_object  # Use object's ID as the key

    def start(self):
        for obj in self.game_objects.values():
            obj.start()

    def handle_event(self, event):
        for obj in self.game_objects.values():
            obj.handle_event(event)

    def update(self):
        for obj in self.game_objects.values():
            obj.update()

    def destroy(self):
        for obj in self.game_objects.values():
            obj.destroy()

    def render(self, screen):
        for obj in self.game_objects.values():
            obj.render(screen)
