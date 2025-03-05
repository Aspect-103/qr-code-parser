import pygame
import os

pygame.font.init()
FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")

# ----------------- FONT DETAILS -----------------
TITLE_FONT = pygame.font.Font(os.path.join(FONT_DIR, "Diavlo_BOLD_II_37.otf"), 32) # Title-size font
NORMAL_FONT = pygame.font.Font(os.path.join(FONT_DIR, "ChakraPetch-Bold.ttf"), 22) # normal text size font
SMALL_FONT = pygame.font.Font(os.path.join(FONT_DIR, "Sintony-Bold.ttf"), 13) # small text size font
FONT_COLOR = pygame.Color((255,150,0))