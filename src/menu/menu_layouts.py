from abc import ABC, abstractmethod

import pygame
from pygame import Surface

from src.core.game_object import GameObject


"""This is an abstract class which can be inherited by other layouts.
 It serves as a 'skeleton' for all menus."""
class MenuLayout(GameObject):
    def __init__(self, position, spacing=10, orientation='vertical', background=None):
        super().__init__()
        self.components = []
        self.position = position
        self.spacing = spacing
        self.orientation = orientation
        self.background = background

    def add_component(self, component):
        pass

    def start(self):
        if self.background is not None and hasattr(self.background, 'start'):
            self.background.start()
        for component in self.components:
            component.start()

    def handle_event(self, event):
        for component in self.components:
            component.handle_event(event)

    def update(self):
        for component in self.components:
            component.update()

    def render(self, screen):
        if self.background is not None:
            if isinstance(self.background, pygame.Color):
                # Fill the background with a solid color
                screen.fill(self.background)
            else:
                # Assume the background object has its own render method
                self.background.render(screen)
        for component in self.components:
            component.render(screen)

    def destroy(self):
        for component in list(self.components):
            component.destroy()
            del component


""" Needs further development and testing to get this working ideally."""


class StackLayout(MenuLayout):
    def __init__(self, position, orientation='vertical', spacing=10, background=None):
        super().__init__(position, background=background)
        self.orientation = orientation
        self.spacing = spacing
        self.components = []
        self.last_position = position  # Tracks the position of the last component

    def add_component(self, component):
        if self.orientation == 'vertical':
            if self.components:  # If there are already components, stack below the last one
                last_component = self.components[-1]
                new_y = last_component.position[1] + last_component.rect.height + self.spacing
                component.position = (self.position[0], new_y)
            else:  # If no components, place the first one at the initial position
                component.position = self.position
            self.last_position = component.position  # Update the position of the last component
        else:  # Horizontal orientation
            if self.components:
                last_component = self.components[-1]
                new_x = last_component.position[0] + last_component.rect.width + self.spacing
                component.position = (new_x, self.position[1])
            else:
                component.position = self.position
            self.last_position = component.position

        self.components.append(component)



class GridLayout(MenuLayout):
    def __init__(self, position, size, columns, row_height, column_width, background=None):
        """
        Initialize the GridLayout with fixed number of columns and dimensions for each cell.
        :param position: Top-left position of the grid layout on the screen.
        :param size: Tuple (width, height) defining the size of the grid area.
        :param columns: Number of columns in the grid.
        :param row_height: Height of each row.
        :param column_width: Width of each column.
        :param background: Optional background color or image.
        """
        super().__init__(position, background)
        self.position = position
        self.size = size
        self.width, self.height = self.size
        self.rect = pygame.Rect(position[0], position[1], self.width, self.height)
        self.columns = columns
        self.row_height = row_height
        self.column_width = column_width
        self.background = background
        self.components = []
        self.screen_size = pygame.display.get_surface().get_size()

    def add_component(self, component, row=None, column=None):
        """
        Add a component to the GridLayout at the specified row and column.
        :param component: The component to be added.
        :param row: The row index where the component should be placed.
        :param column: The column index where the component should be placed.
        :return: The added component.
        """
        if row is None or column is None:
            raise ValueError("Row and column indices must be provided")
        if row * column >= self.columns:
            raise ValueError("Row or column index exceeds grid dimensions")

        # Calculate the position based on the grid
        x = self.position[0] + column * self.column_width
        y = self.position[1] + row * self.row_height

        # Set the component's position
        component.position = (x, y)
        self.components.append(component)
        return component

    def render(self, screen):
        for component in self.components:
            component.render(screen)


""" This widget is a container for other widgets (menu components). It allows you to position
    any widget based upon the position of any other widget that was already
    added to the RelativeLayout."""


class RelativeLayout(MenuLayout):
    def __init__(self, position, screen: Surface, background=None):
        super().__init__(position, background=background)
        self.position = position
        self.screen_size = screen.get_size()  # New attribute to store screen dimensions
        self.components = []

    def add_component(self, component, anchor_component=None, position='below', offset=(0, 0)):
        """
        Add a component to the RelativeLayout and position it based on the anchor_component's position.
        :param component: The component to be added.
        :param anchor_component: The anchor component to position relative to. Can be another component or one of the following strings: 'screen_top', 'screen_bottom', 'screen_left', 'screen_right'.
        :param position: The position relative to the anchor_component. Can be 'below', 'above', 'right', or 'left'.
        :param offset: The offset from the anchor_component's position.
        :return: The added component.
        """
        if isinstance(anchor_component, str):
            # Handle screen-based anchoring
            if anchor_component == 'screen_top':
                new_position = (self.position[0] + offset[0], offset[1])
            elif anchor_component == 'screen_bottom':
                new_position = (self.position[0] + offset[0], self.screen_size[1] - component.rect.height + offset[1])
            elif anchor_component == 'screen_left':
                new_position = (offset[0], self.position[1] + offset[1])
            elif anchor_component == 'screen_right':
                new_position = (self.screen_size[0] - component.rect.width + offset[0], self.position[1] + offset[1])
            else:
                print("Invalid anchor_component argument for " + self.__str__())
        elif anchor_component:
            # Calculate position based on the anchor component's position
            ref_position = anchor_component.position
            ref_size = anchor_component.rect.size  # Assuming 'rect' with 'width' and 'height'
            if position == 'below':
                new_position = (ref_position[0] + offset[0], ref_position[1] + ref_size[1] + offset[1])
            elif position == 'above':
                new_position = (ref_position[0] + offset[0], ref_position[1] - component.rect.height - offset[1])
            elif position == 'right':
                new_position = (ref_position[0] + ref_size[0] + offset[0], ref_position[1] + offset[1])
            elif position == 'left':
                new_position = (ref_position[0] - component.rect.width - offset[0], ref_position[1] + offset[1])
        else:
            # Check if the component already has a defined position
            if hasattr(component, 'position') and component.position:
                # Adjust based on offset if needed
                new_position = (component.position[0] + offset[0], component.position[1] + offset[1])
            else:
                # Use the RelativeLayout's position with any specified offset
                new_position = (self.position[0] + offset[0], self.position[1] + offset[1])

        component.position = new_position
        self.components.append(component)
        return component
