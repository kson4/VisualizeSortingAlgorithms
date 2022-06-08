import pygame
import random

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TOP_PADDING = 300
SIDE_PADDING = 100

NUM_BLOCKS = 50
MIN_VAL = 100
MAX_VAL = 500


class Info:
    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    def __init__(self, lst):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.lst = lst
        self.block_width = round((self.width - SIDE_PADDING) / len(lst))


def generate_list():
    lst = []
    for _ in range(NUM_BLOCKS):
        val = random.randint(MIN_VAL, MAX_VAL)
        lst.append(val)
    return lst


def draw_list(info, n1, n2):
    info.window.fill("WHITE")
    lst = info.lst

    for i, val in enumerate(lst):
        x = SIDE_PADDING // 2 + i * info.block_width
        y = SCREEN_HEIGHT - val

        if i != n1 or i != n2:
            color = info.GRADIENTS[i % 3]

        if i == n1:
            color = (255, 0, 0)
        if i == n2:
            color = (0, 128, 0)
        pygame.draw.rect(info.window, color, (x, y, info.block_width, info.height))


def bubble_sort(info):
    lst = info.lst
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            n1 = lst[j]
            n2 = lst[j + 1]

            if n1 > n2:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(info, j, j + 1)
                yield True

    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    lst = generate_list()
    info = Info(lst)
    generator = None
    sorting = True

    while run:
        clock.tick(10)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        generator = bubble_sort(info)
        if sorting:
            try:
                next(generator)
            except StopIteration:
                sorting = False

        bubble_sort(info)

    pygame.quit()


if __name__ == "__main__":
    main()
