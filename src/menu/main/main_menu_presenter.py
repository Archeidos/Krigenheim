import os
import sys
from typing import Dict

import pygame

from src.core.game_state import NEW_GAME_EVENT
from src.main import base_dir
from src.menu.base_menu_controller import BaseMenuController
from src.menu.menu_layouts import RelativeLayout
from src.menu.menu_widgets import ImageDisplay, ImageLabel, ImageButton


class MainMenuController(BaseMenuController):
    def __init__(self, screen):
        super().__init__(screen)

    def build_menu(self):
        assets_path = os.path.join(base_dir, '../Assets')
        bg_image_path = os.path.join(assets_path, 'krigenheimposter.png')
        button_image_path = os.path.join(assets_path, 'krigenheimbutton.png')
        music_path = os.path.join(assets_path, 'title.mp3')

        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # Loop indefinitely
        pygame.mixer.music.set_volume(0.1)  # Set initial volume to 10%

        # Load the background image using Pillow and set it
        # speech_image = pygame.image.load(speech_image_path)
        menu_layout = RelativeLayout((0, 0), background=ImageDisplay(bg_image_path, self.screen), screen=self.screen)
        title_label = menu_layout.add_component(ImageLabel(button_image_path,
                                                           text="KRIGENHEIM",
                                                           position=(
                                                               self.screen.get_width() / 2,
                                                               self.screen.get_height() - self.screen.get_height() + 30),
                                                           font_size=24,
                                                           size=(175, 50)))
        new_game_button = menu_layout.add_component(
            ImageButton(button_image_path, text="New Game", callback=self._open_new_game, size=(120, 40)),
            anchor_component=title_label,
            offset=(30, 150),
            position='below')
        load_game_button = menu_layout.add_component(
            ImageButton(button_image_path, text="Load Game", callback=self._open_load_game, size=(120, 40)),
            anchor_component=new_game_button,
            offset=(0, 15),
            position='below')
        options_button = menu_layout.add_component(
            ImageButton(button_image_path, text="Options", callback=self._open_options, size=(120, 40)),
            anchor_component=load_game_button,
            offset=(0, 15),
            position='below')
        quit_button = menu_layout.add_component(
            ImageButton(button_image_path, text="Quit", callback=self._quit_game, size=(120, 40)),
            anchor_component=options_button,
            offset=(0, 15),
            position='below')

        self.add_object(menu_layout)
        for obj in self.menu_objects.values():
            obj.start()

    def handle_event(self, event):
        for obj in self.menu_objects.values():
            obj.handle_event(event)

    def update(self):
        for obj in self.menu_objects.values():
            obj.update()

    def destroy(self):
        for key in list(self.menu_objects.keys()):
            obj = self.menu_objects.pop(key)
            obj.destroy()
            del obj

    def render(self, screen):
        for obj in self.menu_objects.values():
            obj.render(screen)

    def _open_new_game(self):
        pygame.event.post(pygame.event.Event(NEW_GAME_EVENT))
        print("New Game clicked")

    def _open_load_game(self):
        print("Load Game clicked")

    def _open_options(self):
        print("Options clicked")

    def _quit_game(self):
        print("Game quit")
        pygame.quit()
        sys.exit()
