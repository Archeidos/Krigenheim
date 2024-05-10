import os
from typing import Dict

import pygame.event

from src.core.game_object import GameObject
from src.core.game_state import MAIN_MENU_EVENT
from src.main import base_dir
from src.menu.base_menu_controller import BaseMenuController
from src.menu.menu_layouts import RelativeLayout, GridLayout
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
                                                               self.screen.get_height() - self.screen.get_height() + 50),
                                                           font_size=28),
                                                # anchor_component='screen_top',
                                                # offset=(self.screen.get_width() / 2 , 0)
                                                )
        back_button = menu_layout.add_component(ImageButton(button_image_path,
                                                            text="Back",
                                                            font_size=24,
                                                            callback=self.back_pressed),
                                                position="left",
                                                anchor_component=title_label,
                                                offset=(225, 0))
        name_input = menu_layout.add_component(TextInput(
            font_size=20),
            position="below",
            anchor_component=title_label,
            offset=(15, 40))
        name_label = menu_layout.add_component(ImageLabel(image_path=button_image_path,
                                                          text="Name:",
                                                          font_size=24),
                                               position="left",
                                               anchor_component=name_input,
                                               offset=(5, -8))
        class_title = menu_layout.add_component(ImageLabel(image_path=button_image_path,
                                                           text="Adventurer",
                                                           font_size=22),
                                                position="below",
                                                anchor_component=name_input,
                                                offset=(-6, 50))
        right_button = menu_layout.add_component(ImageButton(os.path.join(assets_path, 'krigenheimupsm.png'),
                                                             font_size=24,
                                                             callback=self.back_pressed,
                                                             size=(50, 50)),
                                                 position="right",
                                                 anchor_component=class_title,
                                                 offset=(5, -3))
        left_button = menu_layout.add_component(ImageButton(os.path.join(assets_path, 'krigenheimdownsm.png'),
                                                            font_size=24,
                                                            callback=self.back_pressed,
                                                            size=(50, 50)),
                                                position="left",
                                                anchor_component=class_title,
                                                offset=(5, -3))
        hp_grid_layout = menu_layout.add_component(
            GridLayout(position=(0, 0), size=(100, 100), columns=12, row_height=50, column_width=50,
                       background=pygame.Color(0, 0, 0)),
            position="below",
            anchor_component=left_button,
            offset=(0, 10))
        hp_title = hp_grid_layout.add_component(ImageLabel(os.path.join(assets_path, 'blankitemsm.png'),
                                                           text="HP",
                                                           font_size=24,
                                                           font_color=(255, 0, 0),
                                                           size=(50, 50)), row=0, column=0)
        hp_value = hp_grid_layout.add_component(ImageLabel(os.path.join(assets_path, 'blankitemsm.png'),
                                                           font_size=24,
                                                           size=(50, 50)), row=1, column=0)
        mp_grid_layout = menu_layout.add_component(
            GridLayout(position=(0, 0), size=(100, 100), columns=12, row_height=50, column_width=50,
                       background=pygame.Color(0, 0, 0)),
            position="below",
            anchor_component=right_button,
            offset=(0, 10))
        mp_title = mp_grid_layout.add_component(ImageLabel(os.path.join(assets_path, 'blankitemsm.png'),
                                                           text="MP",
                                                           font_size=24,
                                                           font_color=(0, 0, 255),
                                                           size=(50, 50)), row=0, column=0)
        mp_value = mp_grid_layout.add_component(ImageLabel(os.path.join(assets_path, 'blankitemsm.png'),
                                                           font_size=24,
                                                           size=(50, 50)), row=1, column=0)
        stat_grid_one = menu_layout.add_component(
            GridLayout(position=(0, 0), size=(300, 300), columns=12, row_height=50, column_width=50,
                       background=pygame.Color(0, 0, 0)),
            position="left",
            anchor_component=class_title,
            offset=(-10, -0))
        # Row 0 components
        top_left_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=0, column=0)
        top_second_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=0, column=1)
        top_third_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=0, column=2)
        top_fourth_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=0, column=3)

        # Row 1 components
        second_row_first_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=1, column=0)
        second_row_second_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=1, column=1)
        second_row_third_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=1, column=2)
        second_row_fourth_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=1, column=3)

        # Row 2 components
        third_row_first_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=2, column=0)
        third_row_second_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=2, column=1)
        third_row_third_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=2, column=2)
        third_row_fourth_label = stat_grid_one.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=2, column=3)
        stat_grid_two = menu_layout.add_component(
            GridLayout(position=(0, 0), size=(300, 300), columns=12, row_height=50, column_width=50,
                       background=pygame.Color(0, 0, 0)),
            position="right",
            anchor_component=class_title,
            offset=(100, -0))
        # Row 0 components
        top_left_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=0, column=0)
        top_second_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=0, column=1)
        top_third_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=0, column=2)
        top_fourth_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=0, column=3)

        # Row 1 components
        second_row_first_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=1, column=0)
        second_row_second_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=1, column=1)
        second_row_third_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=1, column=2)
        second_row_fourth_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=1, column=3)

        # Row 2 components
        third_row_first_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=2, column=0)
        third_row_second_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=2, column=1)
        third_row_third_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=2, column=2)
        third_row_fourth_label = stat_grid_two.add_component(
            ImageLabel(os.path.join(assets_path, 'blankitemsm.png'), font_size=24, size=(50, 50)), row=2, column=3)
        # left_button3 = stat_grid_one.add_component(ImageButton(os.path.join(assets_path, 'krigenheimdownsm.png'),
        #                                                     font_size=24,
        #                                                     callback=self.back_pressed,
        #                                                     size=(50, 50)), row=1, column=-0)
        # left_button4 = stat_grid_one.add_component(ImageButton(os.path.join(assets_path, 'krigenheimdownsm.png'),
        #                                                     font_size=24,
        #                                                     callback=self.back_pressed,
        #                                                     size=(50, 50)), row=2, column=-1)
        # left_button5 = stat_grid_one.add_component(ImageButton(os.path.join(assets_path, 'krigenheimdownsm.png'),
        #                                                     font_size=24,
        #                                                     callback=self.back_pressed,
        #                                                     size=(50, 50)), row=3, column=-0)
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
