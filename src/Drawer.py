import random

import pygame_gui
from pygame.time import Clock

from GraphInterface import GraphInterface

import pygame


class Drawer:
    def __init__(self,g: GraphInterface):
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')
        self.graph = g
        self.UI = None

    def main(self):
        g = self.graph
        # initialize the pygame module
        pygame.init()
        # load and set the logo

        # create a surface on screen that has the size of 240 x 180
        screen = pygame.display.set_mode((800, 800),pygame.RESIZABLE)
        # define a variable to control the main loop
        running = True

        nodes = g.get_all_v().values()
        for n in nodes:
            if n.loc is not None:
                self.min_x = min(self.min_x,float(n.loc[0]))
                self.max_x = max(self.max_x,float(n.loc[0]))
                self.min_y = min(self.min_y,float(n.loc[1]))
                self.max_y = max(self.max_y,float(n.loc[1]))

        if self.max_x == self.min_x:
            self.max_x +=0.001
            self.min_x -=0.001

        if self.max_y == self.min_y:
            self.max_y += 0.001
            self.min_y -= 0.001

        self.UI = pygame_gui.UIManager((800, 800))

        hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((700, 50), (100, 50)),
                                                    text='Say Hello',
                                                    manager=self.UI)

        input = pygame_gui.elements.UIWindow(,)

        clock = Clock()
        while running:
            time_delta = clock.tick(60) / 1000.0
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False

                if event.type == pygame.USEREVENT:
                    if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element == hello_button:
                            print('Hello World!')

                self.UI.process_events(event)

            screen.fill((255,255,255),pygame.display.get_surface().get_rect())
            for n in nodes:
                if n.loc is not None:
                    pfrom = self.point_to_screen_cord(float(n.loc[0]), float(n.loc[1]))
                    pygame.draw.circle(screen,pygame.Color(0,0,0),pfrom,5,1)
                    for e in g.all_out_edges_of_node(n.id):
                        pto = self.point_to_screen_cord(float(g.get_all_v()[e].loc[0]),float(g.get_all_v()[e].loc[1]))
                        pygame.draw.line(screen,(0,0,0),pfrom,pto)



            self.UI.update(time_delta)

            self.UI.draw_ui(screen)

            pygame.display.update()

    def point_to_screen_cord(self,px,py):
        width = pygame.display.get_surface().get_rect().width
        height = pygame.display.get_surface().get_rect().height
        x = (((self.max_x - px) / (self.max_x - self.min_x))*width*0.9 + width*0.05)
        y = (((self.max_y - py) / (self.max_y - self.min_y))*height*0.9 + height*0.05)

        return x,y

