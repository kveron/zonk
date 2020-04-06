import random
import pygame
import cube
import counterofpoints

FPS = 60
GAME_NAME = "Zonk"
WIN_WIDTH = 400
WIN_HEIGHT = 600
BACKGROUND_COLOR = [0, 75, 0]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

pygame.init()
background = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption(GAME_NAME)
background.fill(BACKGROUND_COLOR)

pygame.draw.line(background, BLACK, (0, 500), (400, 500), 3)
pygame.draw.line(background, BLACK, (200, 500), (200, 600), 3)

throw_photo = pygame.image.load('buttons_PNG21.bmp')
throw_photo.set_colorkey((255, 255, 255))
throw_rect = throw_photo.get_rect(bottomright=(360, 580))
background.blit(throw_photo, throw_rect)

result = pygame.font.SysFont('arial', 36)

throw = result.render('Throw', 1, WHITE)
background.blit(throw, (250, 525))

your_result = result.render('Your result', 1, WHITE)
background.blit(your_result, (10, 500))

pygame.mixer.music.load('sellamusicnet_Lena_Raine_-_wavedashppt_66490751.mp3')
pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.play(-1)

throw_sound = pygame.mixer.Sound('04525 (online-audio-converter.com).ogg')

field_photo = pygame.image.load('24c77c08-87cd-4afd-b12c-6f763fb938ac_1.4595f416417015cb25ea56e9987254c7.jpg')
field_rect = field_photo.get_rect(bottomright=(400, 500))
background.blit(field_photo, field_rect)

pygame.draw.rect(background, (255, 0, 0), (350, 0, 50, 20))
close_text_size = pygame.font.SysFont('arial', 10)
close = close_text_size.render('Закрыть', 1, BLACK)
background.blit(close, (355, 0))

pygame.display.update()


class Zonk:
    @staticmethod
    def main():
        while True:
            clock.tick(FPS)

            cube_value = cube.Cube()

            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    exit()

                elif i.type == pygame.MOUSEBUTTONDOWN:
                    if i.button == 1:
                        if 350 <= i.pos[0] <= 400 and 0 <= i.pos[1] <= 20:
                            exit()

                        elif 240 <= i.pos[0] <= 360 and 520 <= i.pos[1] <= 580:
                            values = [0, 0, 0, 0, 0, 0]
                            background.blit(field_photo, field_rect)
                            pygame.draw.rect(background, (255, 0, 0), (350, 0, 50, 20))
                            background.blit(close, (355, 0))
                            throw_sound.play()
                            pygame.time.delay(3000)
                            quantity_of_cubes = random.randint(1, 6)

                            for j in range(quantity_of_cubes):
                                values[j] = random.randint(1, 6)

                            value = counterofpoints.CounterOfPoints.max_points(values)
                            pygame.draw.rect(background, BACKGROUND_COLOR, (50, 550, 100, 50))

                            x_random = [random.randint(50, 100), random.randint(200, 240), random.randint(300, 350),
                                        random.randint(50, 100), random.randint(200, 240), random.randint(300, 350)]
                            y_random = [random.randint(60, 100), random.randint(60, 100), random.randint(60, 100),
                                        random.randint(250, 300), random.randint(250, 300), random.randint(250, 300)]
                            alfa_random = [random.randint(0, 360), random.randint(0, 360), random.randint(0, 360),
                                           random.randint(0, 360), random.randint(0, 360), random.randint(0, 360)]

                            count = 0

                            for number in values:
                                if number == 1:
                                    cube_value.cube_with_value_one(x_random[count], y_random[count], alfa_random[count])
                                    count += 1

                                elif number == 2:
                                    cube_value.cube_with_value_two(x_random[count], y_random[count], alfa_random[count])
                                    count += 1

                                elif number == 3:
                                    cube_value.cube_with_value_three(x_random[count], y_random[count],
                                                                     alfa_random[count])
                                    count += 1

                                elif number == 4:
                                    cube_value.cube_with_value_four(x_random[count], y_random[count],
                                                                    alfa_random[count])
                                    count += 1

                                elif number == 5:
                                    cube_value.cube_with_value_five(x_random[count], y_random[count],
                                                                    alfa_random[count])
                                    count += 1

                                elif number == 6:
                                    cube_value.cube_with_value_six(x_random[count], y_random[count], alfa_random[count])
                                    count += 1
                            view_result = result.render(value.__str__(), 1, WHITE)
                            background.blit(view_result, (50, 550))
                            pygame.display.update()


obj = Zonk()
obj.main()
