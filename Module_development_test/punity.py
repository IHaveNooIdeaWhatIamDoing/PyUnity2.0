from dataclasses import dataclass

import pygame
from pygame.transform import scale

from First_test.test_script import delta_time

###------------ CONSTANTS ------------------ ###
global const_earth_acceleration
const_earth_acceleration = 9.81

### Settings ###
global refresh_rate
refresh_rate = 120

###------------ CLASSES ------------------ ###

### CALCULATION CLASSES ###
@dataclass
class Vector2D:
        x: float
        y: float
        def __add__(self, other):
            # Vector + Vector
            if isinstance(other, Vector2D):
                return Vector2D(self.x + other.x, self.y + other.y)
        def __sub__(self, other):
            # Vector - Vector
            if isinstance(other, Vector2D):
                return Vector2D(self.x - other.x, self.y - other.y)
        def __mul__(self, other):
            if isinstance(other, (int, float)):
                # Vector * Number
                return Vector2D(self.x * other, self.y * other)
        def __truediv__(self, other):
            # Vector / Number
            if isinstance(other, (int, float)):
                return Vector2D(self.x / other, self.y / other)



### GAMEOBJECT AND COMPONENTS ###

# Vector Class
class Transform2D:
    def __init__(self, position : Vector2D = Vector2D(0,0),
                 rotation: float = 0, x_scale: float = 1, y_scale: float = 1 ):
        self.position = position
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

# Ridigbody
class Ridigbody:
    def __init__(self, mass : float = 10, gravity: bool = False):
        self.mass = mass
        self.acceleration = Vector2D(0,0)
        self.velocity = Vector2D(0,0)
        self.force = Vector2D(0,0)

    def add_force(self, force_direction : Vector2D) -> None:
        """Apply force to along the direction of force_direction """
        self.force += force_direction

    def gravity(self):
        self.add_force(Vector2D(0,const_earth_acceleration*self.mass * DeltaTime.get_delta_time()))


    def update(self):
        if self.gravity:
            self.gravity()
        # a = F/m
        self.acceleration = self.force / self.mass
        self.velocity += self.acceleration

        #Reset force
        self.force = Vector2D(0,0)

# Collider
    class Collider:
        class BoxCollider:
            def __init__(self, offset: Vector2D, scale: Vector2D):
                self.offset = offset
                self.scale = scale
            def check_for_collision(self,type ):


# GameObject Class
class GameObject:
    def __init__(self, transform: "Transform2D", sprite: "Sprite" = None, ridigbody : Ridigbody = None):

        print("GameObject has been created")

        self.transform = transform
        self.sprite = sprite
        self.ridigbody = ridigbody

    def physics_update(self):
        self.transform.position += self.ridigbody.velocity
        self.ridigbody.update()


### MANAGER CLASSES ###

class Input_Manger:
    @staticmethod
    def get_key_down( key : int) -> bool:
        """
        returns True if a key is pressed.

        Args:
            key: the key that should be checked if pressed -> int or pygame.K_[keycode]
        """
        return pygame.key.get_pressed()[key]

class DeltaTime:
    @staticmethod
    def get_delta_time() -> float:
        """Returns the delta_time depending on the refresh_rate"""
        clock = pygame.time.Clock()
        delta_time = clock.tick(refresh_rate)
        delta_time = max(0.001,min(0.1,delta_time))
        return delta_time



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
        screen.blit(obj.sprite.surface, (obj.transform.position.x, obj.transform.position.y))

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
    player.transform.position.x += 10
    print_object_position(player, "player")



def print_object_position(obj : GameObject, name: str):
    print(f"{name} | pos: {obj.transform.position.x, obj.transform.position.y} ")

def main(screen: pygame.surface.Surface):
    rendering(screen)

def rendering(screen: pygame.surface.Surface, background_color: pygame.color.Color = (0,0,0)):
    """Renders everything"""
    screen.fill(background_color)
    render_objects(objects_in_scene, screen)
    pygame.display.update()



### Start Test

### End Test