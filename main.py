import pygame
import random

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TOP_PADDING = 300
SIDE_PADDING = 100

NUM_BLOCKS = 100
MIN_VAL = 100
MAX_VAL = 500


class Info:
    FONT = pygame.font.SysFont('Arial', 50)
    SMALL_FONT = pygame.font.SysFont('Arial', 30)
    BLACK = 0, 0, 0

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


def draw_list(info, n1, n2, name, num_swaps):
    info.window.fill("WHITE")
    title = info.FONT.render(name, 1, info.BLACK)
    info.window.blit(title, (info.width / 2 - title.get_width() / 2, 10))
    if num_swaps != 0:
        num_swaps = "Number of Swaps: " + num_swaps
        swaps = info.SMALL_FONT.render(num_swaps, 1, info.BLACK)
        info.window.blit(swaps, (info.width / 2 - swaps.get_width() / 2, 60))
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
    clock = pygame.time.Clock()
    lst = info.lst
    swaps = 0
    for i in range(len(lst) - 1):
        #clock.tick(100)
        for j in range(len(lst) - i - 1):
            #clock.tick(100)
            n1 = lst[j]
            n2 = lst[j + 1]

            if n1 > n2:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swaps += 1
                draw_list(info, j, j + 1, "Bubble Sort", str(swaps))
                pygame.display.update()

    draw_list(info, -1, -1, "Bubble Sort   R: Reset", str(swaps))


def insertion_sort(info):
    clock = pygame.time.Clock()
    lst = info.lst
    swaps = 0

    for i in range(1, len(lst)):
        #clock.tick(100)
        key = lst[i]

        while i > 0 and lst[i - 1] > key:
            swaps += 1
            #clock.tick(100)
            lst[i] = lst[i - 1]
            i -= 1
            lst[i] = key
            draw_list(info, i - 1, i, "Insertion Sort", str(swaps))
            pygame.display.update()

    draw_list(info, -1, -1, "Insertion Sort   R: Reset", str(swaps))


def selection_sort(info):
    clock = pygame.time.Clock()
    lst = info.lst
    swaps = 0

    for i in range(len(lst)):
        #clock.tick(100)
        min_index = i
        for j in range(i + 1, len(lst)):
            #clock.tick(100)
            draw_list(info, i, j, "Selection Sort", str(swaps))
            pygame.display.update()
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]
        swaps += 1
        draw_list(info, i, min_index, "Selection Sort", str(swaps))
        pygame.display.update()

    draw_list(info, -1, -1, "Selection Sort   R: Reset", str(swaps))


def reset():
    lst = generate_list()
    info = Info(lst)
    draw_list(info, -1, -1, "I: Insertion   B: Bubble   S: Selection", 0)
    return info


def main():
    run = True
    clock = pygame.time.Clock()
    algorithm = ""
    info = reset()
    sorting = True

    while run:
        clock.tick(60)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    bubble_sort(info)
                if event.key == pygame.K_i:
                    insertion_sort(info)
                if event.key == pygame.K_s:
                    selection_sort(info)
                if event.key == pygame.K_r:
                    info = reset()

    pygame.quit()


if __name__ == "__main__":
    main()
