from pygame.time import Clock

from GraphAlgoInterface import GraphAlgoInterface

import pygame

from src.GUI.SidePanel import SidePanel


class Drawer:
    def __init__(self, g: GraphAlgoInterface):
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')
        self.ga = g
        self.UI = None

    def main(self):
        g = self.ga.get_graph()
        # initialize the pygame module
        pygame.init()
        # load and set the logo

        # create a surface on screen that has the size of 240 x 180
        screen = pygame.display.set_mode((800, 800), pygame.RESIZABLE)
        # define a variable to control the main loop
        running = True

        self.calc_min_max()

        if self.max_x == self.min_x:
            self.max_x += 0.001
            self.min_x -= 0.001

        if self.max_y == self.min_y:
            self.max_y += 0.001
            self.min_y -= 0.001

        self.UI = SidePanel(screen, self.ga)

        clock = Clock()
        while running:
            g = self.ga.get_graph()
            nodes = g.get_all_v().values()
            self.calc_min_max()
            time_delta = clock.tick(60) / 1000.0
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
                self.UI.handle_input(event)

            screen.fill((255, 255, 255), pygame.display.get_surface().get_rect())
            for n in nodes:
                if n.loc is not None:
                    pfrom = self.point_to_screen_cord(float(n.loc[0]), float(n.loc[1]))
                    pygame.draw.circle(screen, pygame.Color(n.tag), pfrom, 5, 10)
                    for e in g.all_out_edges_of_node(n.id):
                        pto = self.point_to_screen_cord(float(g.get_all_v()[e].loc[0]), float(g.get_all_v()[e].loc[1]))
                        pygame.draw.line(screen, (0, 0, 0), pfrom, pto)

            self.UI.handle_drawing(time_delta)

            pygame.display.update()

    def point_to_screen_cord(self, px, py):
        width = pygame.display.get_surface().get_rect().width *0.80
        height = pygame.display.get_surface().get_rect().height *0.80
        x = (((self.max_x - px) / (self.max_x - self.min_x)) * width * 0.9 + width * 0.05)
        y = (((self.max_y - py) / (self.max_y - self.min_y)) * height * 0.9 + height * 0.05)

        return x, y

    def calc_min_max(self):
        self.min_x = float('inf')
        self.max_x = float('-inf')
        self.min_y = float('inf')
        self.max_y = float('-inf')
        g = self.ga.get_graph()
        nodes = g.get_all_v().values()
        for n in nodes:
            if n.loc is not None:
                self.min_x = min(self.min_x, float(n.loc[0]))
                self.max_x = max(self.max_x, float(n.loc[0]))
                self.min_y = min(self.min_y, float(n.loc[1]))
                self.max_y = max(self.max_y, float(n.loc[1]))