import math as math1
import arcade

class AnimatedSprite(arcade.Sprite):
    def __init__(self, image, scale=1.0):
        super().__init__(image, scale=scale)
        self.base_scale = scale
        self.anim_time = 0.0
        self.anim_speed = 6.0
        self.anim_amplitude = 0.1

    def update_animation(self, delta_time: float = 1/60):
        self.anim_time += delta_time * self.anim_speed
        oscillation = math1.sin(self.anim_time)
        stretch_x = 1.0 + (oscillation * self.anim_amplitude)
        stretch_y = 1.0 - (oscillation * self.anim_amplitude)
        if self.texture:
            self.width = self.texture.width * self.base_scale * stretch_x
            self.height = self.texture.height * self.base_scale * stretch_y
        pass