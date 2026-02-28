import pygame
from dataclasses import dataclass

@dataclass
class Position:
    x: float
    y: float

@dataclass
class Velocity:
    dx: float
    dy: float

@dataclass
class Sprite:
    image_surface: pygame.Surface