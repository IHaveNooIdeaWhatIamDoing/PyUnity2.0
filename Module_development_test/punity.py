
# GameObject Class
class GameObject:
    def __init__(self, transform: "Transform2D", sprite: "Sprite"):
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
    def __init__(self, image_path : str):
        self.image_path = image_path





def testing():
    print("Start Test:")
    player = GameObject(Transform2D(0,0), Sprite("assets/player.png"))
    print_object_position(player, "player")
    player.transform.x_position += 10
    print_object_position(player, "player")



def print_object_position(obj : GameObject, name: str):
    print(f"{name} | pos: {obj.transform.x_position, obj.transform.y_position} ")

