import pygame
import math
import random

pygame.init()
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
FPS = 60
DARK_BG = (15, 15, 35)
DARKER_BG = (10, 20, 45)
CYAN = (0, 200, 255)
BRIGHT_CYAN = (100, 255, 255)
GRID_COLOR = (40, 100, 150, 40)
PARTICLE_COLOR = (0, 200, 255)
BALL_COLOR = (255, 80, 80)
OBSTACLE_COLOR = (200, 80, 255)
BATTERY_GREEN = (50, 255, 100)
BATTERY_YELLOW = (255, 220, 0)
BATTERY_RED = (255, 60, 60)
WALL_COLOR = (120, 60, 180)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.vx = random.uniform(-3, 3)
        self.vy = random.uniform(-3, 3)
        self.life = 1.0
        self.color = color
        self.size = random.uniform(2, 5)
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= 0.02
        self.vx *= 0.96
        self.vy *= 0.96
    def draw(self, screen):
        if self.life > 0:
            alpha = int(255 * self.life)
            color_with_alpha = (self.color[0], self.color[1], self.color[2], alpha)
            s = pygame.Surface((int(self.size * 3), int(self.size * 3)), pygame.SRCALPHA)
            pygame.draw.circle(s, color_with_alpha, (int(self.size * 1.5), int(self.size * 1.5)), int(self.size))
            screen.blit(s, (int(self.x - self.size * 1.5), int(self.y - self.size * 1.5)))

class Trail:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 1.0
    def update(self):
        self.life -= 0.1
    def draw(self, screen):
        if self.life > 0:
            alpha = int(120 * self.life)
            size = int(10 * self.life)
            s = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
            trail_color = (CYAN[0], CYAN[1], CYAN[2], alpha)
            pygame.draw.circle(s, trail_color, (size, size), size)
            screen.blit(s, (int(self.x - size), int(self.y - size)))

class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.glow_phase = random.uniform(0, math.pi * 2)
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    def draw(self, screen):
        self.glow_phase += 0.05
        glow_intensity = int(60 + 40 * math.sin(self.glow_phase))
        glow_size = 8
        glow_surface = pygame.Surface((self.width + glow_size * 2, self.height + glow_size * 2), pygame.SRCALPHA)
        glow_color = (WALL_COLOR[0], WALL_COLOR[1], WALL_COLOR[2], glow_intensity)
        pygame.draw.rect(glow_surface, glow_color, glow_surface.get_rect(), border_radius=8)
        screen.blit(glow_surface, (self.x - glow_size, self.y - glow_size))
        rect = self.get_rect()
        pygame.draw.rect(screen, WALL_COLOR, rect, border_radius=6)
        inner_rect = pygame.Rect(rect.x + 3, rect.y + 3, rect.width - 6, rect.height - 6)
        if inner_rect.width > 0 and inner_rect.height > 0:
            inner_surface = pygame.Surface((inner_rect.width, inner_rect.height), pygame.SRCALPHA)
            inner_color = (200, 140, 255, 40)
            pygame.draw.rect(inner_surface, inner_color, inner_surface.get_rect(), border_radius=4)
            screen.blit(inner_surface, (inner_rect.x, inner_rect.y))
        pygame.draw.rect(screen, (180, 140, 220), rect, 2, border_radius=6)
