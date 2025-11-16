from pydoc import sort_attributes

import pygame


### CLASSES ###

# GameObject Class
class GameObject:
    def __init__(self, transform: "Transform2D", sprite: "Sprite" = None):
        if not isinstance(transform, Transform2D):
            raise TypeError("transform must be of type transform2D")
        if not isinstance(sprite, Sprite):
            raise TypeError("sprite must be of type Sprite")

        print("GameObejct has been created")

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
    def __init__(self, image_path : str, layer : int = 0, convertion : bool = False ):
        self.image_path = image_path
        self.layer = layer
        self.convertion = convertion
        # Load the image as the surface
        if image_path:
            if self.convertion:
                self.surface = pygame.image.load(self.image_path).convert_alpha()
            else:
                self.surface = pygame.image.load(self.image_path)




# Object in a Scene List
objects_in_scene = [] # List of all GameObject that exist in the Scene

# instantiate a new Gameobject
def instantiate(game_object : GameObject):
     objects_in_scene.append(game_object)

def render_objects(objects_in_scene : list, screen):
    render_que_list = sorted(objects_in_scene, key=lambda obj: obj.sprite.layer)
    for object in render_que_list:





### Testing Code ###


def test_object_in_scene():
    player = GameObject(Transform2D(0, 0), Sprite("assets/player.png"))
    instantiate(player)
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

### Start Test
test_transform()

### End Test