import pygame, asyncio, entity, component

DISPLAY_W = 720
DISPLAY_H = 480

pygame.init()

screen = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
clock = pygame.time.Clock()

entity_manager = entity.EntityManager()

# systems

def velocity_sys(manager: entity.EntityManager, dt: float) -> None:
    if dt <= 0:
        return

    for entity_id, comps in manager.entities.items():
        pos = comps.get(component.Position)
        vel = comps.get(component.Velocity)
        if pos is None or vel is None:
            continue

        pos.x += vel.dx * dt
        pos.y += vel.dy * dt


def render_sys(manager: entity.EntityManager, surface: pygame.Surface) -> None:
    for entity_id, comps in manager.entities.items():
        pos = comps.get(component.Position)
        spr = comps.get(component.Sprite)
        if pos is None or spr is None:
            continue

        rect = spr.image_surface.get_rect(center=(int(pos.x), int(pos.y)))
        surface.blit(spr.image_surface, rect)

# main entry point
async def main():
    running = True

    while running:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        velocity_sys(entity_manager, dt)

        screen.fill("black")

        render_sys(entity_manager, screen)

        pygame.display.flip()
        await asyncio.sleep(0)

asyncio.run(main())