

import pygame
from pygame.transform import scale


### CLASSES ###

# GameObject Class
class GameObject:
    def __init__(self, transform: "Transform2D", sprite: "Sprite" = None):

        print("GameObject has been created")

        self.transform = transform
        self.sprite = sprite

# Vector Class
class Transform2D:
    def __init__(self,x_position : float = 0 ,y_position: float = 0,
                 rotation: float = 0, x_scale: float = 1, y_scale: float = 1 ):
        self.x_position = x_position
        self.y_position = y_position
        self.rotation = rotation
        self.x_scale = x_scale
        self.y_scale = y_scale

# Sprite Renderer
class Sprite:
    def __init__(self, image_path : str,  layer : int = 0, convertion : bool = False ):
        self.image_path = image_path
        self.layer = layer
        self.convertion = convertion
        # Load the image as the surface
        if image_path:
            if self.convertion:
                self.surface = pygame.image.load(self.image_path).convert_alpha()
            else:
                self.surface = pygame.image.load(self.image_path)
        self.original_surface = self.surface


# Object in a Scene List
objects_in_scene = [] # List of all GameObject that exist in the Scene

# instantiate a new Gameobject
def add_to_rendering(game_object : GameObject):
    """Adds a GameObject to the rendering que. GameObject must have Sprite-Class"""
    objects_in_scene.append(game_object)


def render_objects(objects : list, screen: pygame.surface.Surface):
    """Renders all the objects in the scene"""
    render_que_list = sorted(objects, key=lambda obj: obj.sprite.layer)
    for obj in render_que_list:
        # Scale the object
        obj = scale_obj(obj)
        # Draw the Object on the screen
        screen.blit(obj.sprite.surface, (obj.transform.x_position, obj.transform.y_position))

def scale_obj(obj: GameObject):
    """Scales the Object by the scale of the transform-scale variables"""
    if obj.sprite:
        width = obj.sprite.original_surface.get_width()* obj.transform.x_scale
        height = obj.sprite.original_surface.get_height()* obj.transform.y_scale
        new_surface = pygame.transform.scale(obj.sprite.surface, (width, height))
        obj.sprite.surface = new_surface
        return obj
    else:
        raise TypeError("tries to scale an object that has no sprite")




### Testing Code ###


def test_object_in_scene():
    player = GameObject(Transform2D(0, 0), Sprite("assets/player.png"))
    add_to_rendering(player)
    print(f"First objects in a scene: {objects_in_scene}")
    print_object_position(player, "player")
    player.transform = Transform2D(10, 10)
    print_object_position(objects_in_scene[0], "player")

def test_transform():
    print("Start Test:")
    player = GameObject(Transform2D(0,0), Sprite("assets/player.png"))
    print_object_position(player, "player")
    player.transform.x_position += 10
    print_object_position(player, "player")



def print_object_position(obj : GameObject, name: str):
    print(f"{name} | pos: {obj.transform.x_position, obj.transform.y_position} ")

def main(screen: pygame.surface.Surface):
    rendering(screen)

def rendering(screen: pygame.surface.Surface, background_color: pygame.color.Color = (0,0,0)):
    """Renders everything"""
    screen.fill(background_color)
    render_objects(objects_in_scene, screen)
    pygame.display.update()



### Start Test

### End Test