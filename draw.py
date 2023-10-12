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

pygame.init()
screen = pygame.display.set_mode((500,500))

def get_next_name(dir, filename):
    numbers = [0]
    for file in os.listdir(dir):
        numbers.append(int(file.replace(filename, '').replace('.png', '')))
    return os.path.join(dir ,filename + str(max(numbers) + 1) + ".png")


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
            if event.key == pygame.K_h:
                pygame.image.save(screen, get_next_name('house', 'house'))
                screen.fill((0,0,0))
            if event.key == pygame.K_s:
                pygame.image.save(screen, get_next_name('smilingface', 'smilingface'))
                screen.fill((0,0,0))
            if event.key == pygame.K_f:
                pygame.image.save(screen, get_next_name('fish', 'fish'))
                screen.fill((0,0,0))
            if event.key == pygame.K_d:
                screen.fill((0,0,0))
    if drawing:
        pygame.draw.circle(screen, (255,255,255), pygame.mouse.get_pos(), 5)
    pygame.display.update()