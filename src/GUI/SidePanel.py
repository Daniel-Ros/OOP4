import json
import os

import pygame
import pygame_gui


class SidePanel:
    def __init__(self, screen, graph):
        self.ga = graph
        self.screen = screen
        self.UI = pygame_gui.UIManager((800, 800))
        self.load = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 50), (100, 50)),
                                                 text='load',
                                                 manager=self.UI)
        self.save = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 100), (100, 50)),
                                                 text='save',
                                                 manager=self.UI)
        self.short = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 150), (100, 50)),
                                                  text='shortest path',
                                                  manager=self.UI)
        self.tsp = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 200), (100, 50)),
                                                text='tsp',
                                                manager=self.UI)
        self.center = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 250), (100, 50)),
                                                   text='Center',
                                                   manager=self.UI)
        self.choser = None

        self.src_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((700, 300), (100, 50)),
                                                             manager=self.UI,
                                                             visible=False)
        self.dst_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((700, 325), (100, 50)),
                                                             manager=self.UI,
                                                             visible=False)
        self.src_input.set_text('Src Input')
        self.dst_input.set_text('Dest Input')

        self.ok = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 350), (100, 25)),
                                               text='OK',
                                               manager=self.UI
                                               , visible=False)
        self.func_ans = pygame_gui.elements.UILabel(relative_rect=pygame.Rect((700, 375), (100, 50)),
                                                    text='',
                                                    manager=self.UI,
                                                    visible=False)

        self.last_event = None

    def handle_input(self, event):
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.load:
                    self.choser = pygame_gui.windows.UIFileDialog(pygame.Rect(160, 50, 440, 500),
                                                                  self.UI,
                                                                  window_title='Load Json...',
                                                                  initial_file_path=os.getcwd(),
                                                                  allow_existing_files_only=True)
                    self.load.disable()
                if event.ui_element == self.save:
                    self.choser = pygame_gui.windows.UIFileDialog(pygame.Rect(160, 50, 440, 500),
                                                                  self.UI,
                                                                  window_title='Save Json...',
                                                                  initial_file_path=os.getcwd(),
                                                                  allow_existing_files_only=True)
                    self.save.disable()
                if event.ui_element == self.short:
                    self.src_input.visible = True
                    self.dst_input.visible = True
                    self.func_ans.visible = True
                    self.ok.visible = True
                    self.last_event = self.short
                    self.src_input.redraw_cursor()
                    self.dst_input.redraw_cursor()
                    self.src_input.update(0.1)
                    self.dst_input.update(0.1)
                    pass
                if event.ui_element == self.tsp:
                    pass
                if event.ui_element == self.center:
                    c = self.ga.centerPoint()
                    if c in self.ga.get_graph().get_all_v():
                        self.ga.get_graph().get_all_v()[c].tag = (255, 0, 0)

                if event.ui_element == self.ok:
                    user_src = int(self.src_input.get_text())
                    user_dst = int(self.dst_input.get_text())
                    if self.last_event == self.short:
                        shortest = self.ga.shortest_path(user_src, user_dst)
                        self.func_ans.set_text(shortest[0])
                        print(shortest[0])

            if event.user_type == pygame_gui.UI_FILE_DIALOG_PATH_PICKED:
                if self.load.is_enabled is False:
                    try:
                        self.ga.load_from_json(event.text)
                        self.choser = None
                        self.load.enable()
                    except json.decoder.JSONDecodeError:
                        print("json is not readable")

                else:
                    self.ga.save_to_file(event.text)
                    self.choser = None
                    self.load.enable()

            if event.user_type == pygame_gui.UI_WINDOW_CLOSE:
                if event.ui_element == self.choser:
                    if self.load.is_enabled is False:
                        self.choser = None
                        self.load.enable()
                    else:
                        self.choser = None
                        self.save.enable()

        self.UI.process_events(event)

    def handle_drawing(self, time_delta):
        self.UI.update(time_delta)
        self.UI.draw_ui(self.screen)
