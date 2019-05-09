from abc import ABC, abstractmethod
import pygame


class Renderable(ABC):
    @abstractmethod
    def on_render(self, screen, screenshot_resolution, screenshot_x_offset):
        pass

    @staticmethod
    def to_screen_rect(rect_to_transform, screen_rect, screenshot_resolution, screenshot_x_offset):
        """Transforms scene-sized rect to screen-sized rect"""
        return pygame.Rect(screen_rect.width * (rect_to_transform.x - screenshot_x_offset) / screenshot_resolution[0],
                           screen_rect.height * rect_to_transform.y / screenshot_resolution[1],
                           screen_rect.width * rect_to_transform.width / screenshot_resolution[0],
                           screen_rect.height * rect_to_transform.height / screenshot_resolution[1])
