import pygame
import os
from point import Cat

pygame.init()
WIDTH = 1024
HEIGHT = 640

screen = pygame.display.set_mode((WIDTH, HEIGHT))

ASSETS_PATH = "robot"

cat_image = pygame.image.load("cat/Idle/Idle (1).png")
cat_image = pygame.transform.scale_by(cat_image, 0.2)
cat = Cat(cat_image)

cat_group = pygame.sprite.Group()
cat_group.add(cat)
score = 0
f = pygame.font.SysFont("Arial", 24)
score_text = f.render(f"score: {score}", True, "red")


def load_frames(folder_name):
    path = os.path.join(ASSETS_PATH, folder_name)
    frames = []
    files = sorted(os.listdir(path))
    for f in files:
        img = pygame.image.load(f"{ASSETS_PATH}/{folder_name}/{f}")
        img = pygame.transform.scale_by(img, 0.3)
        frames.append(img)
    return frames


idle_images = load_frames("Idle")
run_images = load_frames("Run")


bg_image = pygame.image.load("BG.png")
bg_image = pygame.transform.scale(bg_image, (WIDTH, HEIGHT))
running = True
frame_index = 0
current_animation = "Idle"
current_images_list = idle_images
player_image = idle_images[frame_index]
player_rect = player_image.get_rect(topleft=(100, 400))
last_animation_time = 0
current_direction = 1
is_idle = True


def animation(list):
    global last_animation_time, frame_index, player_image
    if pygame.time.get_ticks() - last_animation_time >= 100:

        last_animation_time = pygame.time.get_ticks()
        frame_index += 1
        if frame_index >= len(list):
            frame_index = 0
    player_image = list[frame_index]


def move():
    global current_direction, is_idle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        current_direction = -1
        is_idle = False
        player_rect.x -= 10
    if keys[pygame.K_RIGHT]:
        current_direction = 1
        is_idle = False
        player_rect.x += 10
    if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        is_idle = True


def change_animation(new_animation, new_list):
    global current_animation, frame_index, current_images_list
    if new_animation != current_animation:
        current_animation = new_animation
        frame_index = 0
        current_images_list = new_list


def check_change_animation():
    if not is_idle:
        change_animation("Run", run_images)
    else:
        change_animation("Idle", idle_images)


clock = pygame.time.Clock()
is_scored = False
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # screen.fill("lightgreen")
    score_text = f.render(f"score: {score}", True, "red")
    if not cat.alive and not is_scored:
        score += 1
        is_scored = True
    screen.blit(bg_image, (0, 0))
    cat_group.update(player_rect)
    cat_group.draw(screen)

    screen.blit(score_text, (20, 20))
    screen.blit(player_image, player_rect)
    animation(current_images_list)
    move()
    check_change_animation()
    pygame.display.update()
    clock.tick(60)
