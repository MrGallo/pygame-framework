from typing import Optional

import pygame

from game.base_view import BaseView
from game.play_view import PlayView
from game.my_game import MyGame


class TitleView(BaseView):
    def __init__(self):
        title_font = pygame.font.SysFont("Arial", 40)
        self.title_text = title_font.render("Title Screen", True, (255, 255, 255))

        self.info_font = pygame.font.SysFont("Arial", 25)
        self.info_text = self.info_font.render("Click to play", True, (175, 175, 175))

        self.previous_score_text: Optional[pygame.Surface] = None
    
    def set_previous_score(self, score: int) -> None:
        self.previous_score_text = self.info_font.render(f"Previous score: {score}", True, (255, 255, 255))

    def event_loop(self, events):
        for event in events:
            if event.type == pygame.locals.MOUSEBUTTONDOWN:
                MyGame.set_current_view(PlayView())

    def update(self):
        pass

    def draw(self, surface: pygame.Surface):
        surface.fill((0, 0, 128))
        surf_center = surface.get_rect().center
        text_rect = self.title_text.get_rect()
        text_rect.center = surf_center
        text_rect.y = surface.get_height() * 0.33
        surface.blit(self.title_text, text_rect.topleft)

        text_rect = self.info_text.get_rect()
        text_rect.center = surf_center
        text_rect.y = surface.get_height() * 0.67
        surface.blit(self.info_text, text_rect.topleft)

        # score, if available
        if self.previous_score_text is not None:
            text_rect = self.previous_score_text.get_rect()
            text_rect.center = surf_center
            text_rect.y = surface.get_height() * 0.80
            surface.blit(self.previous_score_text, (text_rect.topleft))
