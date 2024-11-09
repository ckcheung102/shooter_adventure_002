from csv import reader
import pygame
import os

############################################

# This function is to chop the single animation sheet into a bunch of images and
# then create a new folder with animation name and put all these images into that folder
# or convert all these images and output as a list
############################################


animation_name ='run'
# change your target animation name here ####


TILE_SIZE = 64
state = [f"{animation_name}"]


# converting CSV file to a list
def csvLoader(path) -> list:
    tile_map = []

    with open(path) as csvfile:
        graph_map = reader(csvfile, delimiter=",")
        for row in graph_map:
            tile_map.append(list(row))
        # print(tile_map)

    return tile_map


# csvLoader("map/map_FloorBlocks.csv")

# working with spritesheet with input being path and convert the sheet to a list
def spritesheet_to_list(path, axis, row, col, x_size, y_size) -> list:
    # screen = pygame.display.set_mode((480,480))

    frames = []
    sprite_sheet = pygame.image.load(path)

    if axis == "vertical":
        for j in range(0, col):
            temp_list = []
            for i in range(0, row):
                img = sprite_sheet.subsurface(j * y_size, i * x_size,  x_size,  y_size)
                # img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                temp_list.append(img)

            frames.append(temp_list)

    else:
        for i in range(0, row):
            temp_list = []
            for j in range(0, col):
                img = sprite_sheet.subsurface(j * x_size, i * y_size,  x_size, y_size)
                # img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                temp_list.append(img)
            frames.append(temp_list)

    return frames


# working with spritesheet with input being sprite sheet
def sheet_to_list(sprite_sheet, axis, row, col, x_size, y_size) -> list:

    frames = []

    if axis == "vertical":
        for j in range(0, col):
            temp_list = []
            for i in range(0, row):
                img = sprite_sheet.subsurface(j * y_size, i * x_size, x_size, y_size)
                # img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                temp_list.append(img)

            frames.append(temp_list)

    else:
        for i in range(0, row):
            temp_list = []
            for j in range(0, col):
                img = sprite_sheet.subsurface(j * x_size, i * y_size, x_size, y_size)
                # img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
                temp_list.append(img)
            frames.append(temp_list)

    return frames


# working with spritesheet and convert the sheet to a folder of images in your directory
def spritesheet_to_folder(path, axis, row, col, x_size, y_size) -> None:
    # screen = pygame.display.set_mode((480,480))

    sprite_sheet = pygame.image.load(path)
    if axis == "vertical":
        for j in range(0, col):
            for i in range(0, row):
                img = sprite_sheet.subsurface(j * y_size, i * x_size, x_size, y_size)
                img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))

                if not os.path.exists(f"spritesheet/{state[j]}"):
                    os.mkdir(f"spritesheet/{state[j]}")

                pygame.image.save(img, f"spritesheet/{state[j]}/{i}.png")


    else:
        for i in range(0, row):
            for j in range(0, col):
                img = sprite_sheet.subsurface(j * x_size, i * y_size, x_size, y_size)
                img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))

                if not os.path.exists(f"spritesheet/{state[i]}"):
                    os.mkdir(f"spritesheet/{state[i]}")

                pygame.image.save(img, f"spritesheet/{state[i]}/{j}.png")

#### To run these functions ####

spritesheet_to_folder(f"spritesheet/{animation_name}.png", "horizontal", 1, 13, 22, 33)