"""
    github: Null-byte-00
    Copyright (C)   Soroush(Amirali) Rafie

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import pygame
import os
from create_dataset import ConvertDir
from model import Model
import torch

pygame.init()
screen = pygame.display.set_mode((500,500))

loop = True
drawing = False
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                pygame.image.save(screen, 'cache/last.png')
                loop = False
    if drawing:
        pygame.draw.circle(screen, (255,255,255), pygame.mouse.get_pos(), 5)
    pygame.display.update()

m = Model()
m.load()
m.eval()

c = ConvertDir("cache", "cache")
inp = torch.tensor(c.image_arrays[0], dtype=torch.float32).unsqueeze(0)
output = m(inp)
print("house:",output[0] * 100)
print("smilingface:",output[1] * 100)
print("fish:",output[2] * 100)