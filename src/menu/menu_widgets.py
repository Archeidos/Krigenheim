import time

import pygame

from src.core.game_object import GameObject


# Object used for creating an image (pngs, jpg, etc.)
class ImageDisplay(GameObject):
    def __init__(self, image_path, screen, fit=True):
        self.screen = screen  # Assume screen dimensions are passed to the constructor
        original_image = pygame.image.load(image_path)
        # Resize image to match the screen dimensions
        if fit is True:
            self.image = pygame.transform.scale(original_image, self.screen.get_size())
        else:
            self.image = original_image
        self.position = (0, 0)  # Position will always be (0,0) for a full-screen image
        self.rect = self.image.get_rect(topleft=self.position)  # Update the rect attribute

    def start(self):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.blit(self.image, self.position)


# Object to be used as a button. image_path is the button background.
# You can specify a text parameter, and a callback (you can pass a function to be executed when clicked)
class ImageButton(GameObject):
    def __init__(self, image_path, position=(0, 0), text="", callback=None, font_type="Helvetica", font_size=18, size=None):
        original_image = pygame.image.load(image_path)
        self.font = pygame.font.SysFont(font_type, font_size)
        self.text_surface = self.font.render(text, True, (255, 255, 255))
        text_width, text_height = self.text_surface.get_size()
        padding = 10

        # Determine the dimensions for the image
        if size:
            self.image = pygame.transform.scale(original_image, size)
        else:
            # Scale image to better fit the text dimensions + padding
            desired_width = text_width + 2 * padding
            desired_height = text_height + 2 * padding
            self.image = pygame.transform.scale(original_image, (desired_width, desired_height))

        # Recalculate the center position of the image to truly center it at 'position'
        self.position = position
        offset_x = position[0] - self.image.get_width() // 2
        offset_y = position[1] - self.image.get_height() // 2
        self.rect = self.image.get_rect(topleft=(offset_x, offset_y))

        # Recalculate the text position to be centered on the resized image
        text_x = offset_x + (self.image.get_width() - text_width) // 2
        text_y = offset_y + (self.image.get_height() - text_height) // 2
        self.text_position = (text_x, text_y)

        self.callback = callback
        self.is_hovered = False

    def start(self):
        self.rect = self.image.get_rect(topleft=self.position)

        text_x = self.position[0] + (self.image.get_width() - self.text_surface.get_width()) // 2
        text_y = self.position[1] + (self.image.get_height() - self.text_surface.get_height()) // 2
        self.text_position = (text_x, text_y)

    def update(self):
        self.handle_mouse_events()

    def handle_mouse_events(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                if self.callback:
                    self.callback()  # Execute the callback function
            self.is_hovered = True
        else:
            self.is_hovered = False

    def render(self, screen):
        # Apply hover effect if hovered
        if self.is_hovered:
            hovered_image = self.image.copy()
            hovered_image.fill((100, 100, 100, 50), None, pygame.BLEND_RGBA_ADD)
            screen.blit(hovered_image, self.position)
        else:
            screen.blit(self.image, self.position)
        screen.blit(self.text_surface, self.text_position)

    def destroy(self):
        # Clear resources and references
        self.image = None
        self.text_surface = None
        self.callback = None


class ImageLabel(GameObject):
    def __init__(self, image_path, position=(0, 0), text="", font_type="Helvetica", font_size=20, size=None,
                 font_color=(255, 255, 255)):
        # Load the image and create a font object
        original_image = pygame.image.load(image_path)
        self.position = position
        self.font = pygame.font.SysFont(font_type, font_size)

        # Render the text onto a surface with the specified font color
        self.text_surface = self.font.render(text, True, font_color)
        text_width, text_height = self.text_surface.get_size()  # Define text dimensions here

        if size:
            # If size is specified, scale the image to these dimensions
            self.image = pygame.transform.scale(original_image, size)
        else:
            # If no size is specified, adjust the size to fit the text
            padding = 10  # Add some padding around the text
            self.image = pygame.transform.scale(original_image, (text_width + 2 * padding, text_height + 2 * padding))

        # Calculate the position based on the centering logic
        offset_x = position[0] - self.image.get_width() / 2
        offset_y = position[1] - self.image.get_height() / 2
        self.position = (offset_x, offset_y)
        self.rect = self.image.get_rect(topleft=self.position)

        # Calculate the position to center the text on the resized image
        text_x = self.position[0] + (self.image.get_width() - text_width) // 2
        text_y = self.position[1] + (self.image.get_height() - text_height) // 2
        self.text_position = (text_x, text_y)

    def start(self):
        text_x = self.position[0] + (self.image.get_width() - self.text_surface.get_width()) // 2
        text_y = self.position[1] + (self.image.get_height() - self.text_surface.get_height()) // 2
        self.text_position = (text_x, text_y)
        pass

    def update(self):
        pass

    def render(self, screen):
        # Draw the image and the text
        screen.blit(self.image, self.position)
        screen.blit(self.text_surface, self.text_position)

    def destroy(self):
        # Optionally clean up resources
        pass


class TextInput(GameObject):
    def __init__(self, position=(0, 0), font_type=None, font_size=24, size=(200, 30),
                 color_inactive=(100, 100, 100), color_active=(0, 0, 0), background_color='white'):
        pygame.font.init()
        self.font = pygame.font.Font(font_type, font_size)
        self.position = position
        self.size = size  # Size now a tuple (width, height)
        self.width, self.height = self.size  # Unpack the size tuple
        self.active = False
        self.text = ""
        self.rect = pygame.Rect(position[0], position[1], self.width, self.height)
        self.color_inactive = pygame.Color(color_inactive)
        self.color_active = pygame.Color(color_active)
        self.background_color = pygame.Color(background_color)  # Background color of the text box
        self.color = self.color_inactive
        self.last_blink = time.time()
        self.cursor_visible = True
        self.cursor_position = 0

    def start(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], self.width, self.height)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
                self.color = self.color_active if self.active else self.color_inactive
            else:
                self.active = False
                self.color = self.color_inactive

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                pass  # You might want to handle return key if needed
            else:
                self.text += event.unicode

    def update(self):
        if time.time() - self.last_blink > 0.5:
            self.cursor_visible = not self.cursor_visible
            self.last_blink = time.time()

    def destroy(self):
        pass

    def render(self, screen):
        # Render the background first
        pygame.draw.rect(screen, self.background_color, self.rect)

        # Render the current text.
        txt_surface = self.font.render(self.text, True, self.color)
        # Adjust the width of the box if the text is too long.
        width = max(self.width, txt_surface.get_width() + 10)
        self.rect.w = width  # Update rect width to new width if it has changed

        # Blit the text.
        screen.blit(txt_surface, (self.rect.x + 5, self.rect.y + 5))
        # Draw the input box.
        pygame.draw.rect(screen, self.color, self.rect, 2)

        # Draw the cursor if the input box is active
        if self.active and self.cursor_visible:
            cursor_x = self.rect.x + txt_surface.get_width() + 5
            cursor_y = self.rect.y + 5
            cursor_rect = pygame.Rect(cursor_x, cursor_y, 2, self.font.get_height())
            pygame.draw.rect(screen, self.color, cursor_rect)
