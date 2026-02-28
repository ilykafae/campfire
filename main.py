import pygame, asyncio, entity

DISPLAY_W = 720
DISPLAY_H = 480

pygame.init()

screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
clock = pygame.time.Clock()

entity_manager = entity.EntityManager()

# systems
def velocity_sys():
    return

def render_sys():
    return

# main entry point
async def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
    
    screen.fill("black")

    # draw begin



    # draw end

    pygame.display.flip();

    clock.tick(60)
    await asyncio.sleep(0) 

asyncio.run(main())