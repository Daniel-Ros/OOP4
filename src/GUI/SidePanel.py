import pygame
import pygame_gui

class SidePanel:
    def __init__(self,screen):
        self.screen = screen
        self.UI = pygame_gui.UIManager((800, 800))
        self.hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 50), (100, 50)),
                                                    text='Center',
                                                    manager=self.UI)

    def handle_input(self,event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.hello_button:
                    print('Hello World!')

        self.UI.process_events(event)

    def handle_drawing(self,time_delta):
        self.UI.update(time_delta)
        self.UI.draw_ui(self.screen)