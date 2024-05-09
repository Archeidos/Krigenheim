import os
from typing import Dict

import pygame.event

from src.core.game_object import GameObject
from src.core.game_state import MAIN_MENU_EVENT
from src.main import base_dir
from src.menu.base_menu_controller import BaseMenuController
from src.menu.menu_layouts import RelativeLayout
from src.menu.menu_widgets import ImageLabel, ImageButton, TextInput, ImageDisplay


class NewGameController(BaseMenuController):
    def __init__(self, screen):
        super().__init__(screen)

    def build_menu(self):
        assets_path = os.path.join(base_dir, '../Assets')
        bg_image_path = os.path.join(assets_path, 'krigenheimposter.png')
        menu_image_path = os.path.join(assets_path, 'krigenheimmenu.png')
        button_image_path = os.path.join(assets_path, 'krigenheimbutton.png')
        button2_image_path = os.path.join(assets_path, 'krigenheimbuttonsm.png')
        right_image_path = os.path.join(assets_path, 'krigenheimupsm.png')
        left_image_path = os.path.join(assets_path, 'krigenheimdownsm.png')
        speech_image_path = os.path.join(assets_path, 'speechmed.png')
        music_path = os.path.join(assets_path, 'title.mp3')

        # Load the background image using Pillow and set it
        # speech_image = pygame.image.load(speech_image_path)
        menu_layout = RelativeLayout((0, 0), background=ImageDisplay(menu_image_path, self.screen), screen=self.screen)
        title_label = menu_layout.add_component(ImageLabel(button_image_path,
                                                           text="New Game",
                                                           position=(
                                                               self.screen.get_width() / 2,
                                                               self.screen.get_height() - self.screen.get_height() + 45),
                                                           font_size=34),
                                                # anchor_component='screen_top',
                                                # offset=(self.screen.get_width() / 2 , 0)
                                                )
        back_button = menu_layout.add_component(ImageButton(button_image_path,
                                                            text="Back",
                                                            font_size=28,
                                                            callback=self.back_pressed),
                                                position="left",
                                                anchor_component=title_label,
                                                offset=(240, 0))
        name_input = menu_layout.add_component(TextInput(
            font_size=24),
            position="below",
            anchor_component=title_label,
            offset=(0, 50))
        name_label = menu_layout.add_component(ImageLabel(image_path=button_image_path,
                                                          text="Name:",
                                                          font_size=24),
                                               position="left",
                                               anchor_component=name_input,
                                               offset=(5, -2))
        class_title = menu_layout.add_component(ImageLabel(image_path=button_image_path,
                                                           text="Adventurer",
                                                           font_size=28),
                                                position="below",
                                                anchor_component=name_input,
                                                offset=(10, 50))
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

    def back_pressed(self):
        pygame.event.post(pygame.event.Event(MAIN_MENU_EVENT))