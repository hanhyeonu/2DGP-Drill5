from pico2d import *

open_canvas()
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running, dir_x, dir_y, face_dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                face_dir = 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                face_dir = -1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


running = True
x, y = 400, 90
dir_x, dir_y = 0, 0
face_dir = 1
frame = 0

while running:
    clear_canvas()
    TUK_ground.draw(400, 300)

    if dir_x != 0 or dir_y != 0:
        if dir_x > 0:
            character.clip_draw(frame * 100, 100, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 0, 100, 100, x, y)
    else:  # 정지 상태
        if face_dir == 1:
            character.clip_draw(frame * 100, 300, 100, 100, x, y)
        else:
            character.clip_draw(frame * 100, 200, 100, 100, x, y)

    update_canvas()
    handle_events()

    x += dir_x * 5
    y += dir_y * 5

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
