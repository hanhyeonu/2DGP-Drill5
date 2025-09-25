from pico2d import *

open_canvas()
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
x, y = 400, 90
frame = 0

while running:
    clear_canvas()
    TUK_ground.draw(400, 300)
    character.clip_draw(frame * 100, 300, 100, 100, x, y)
    update_canvas()

    handle_events()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()
