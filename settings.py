import math

res = width, height = 1400, 800
half_width = width // 2
half_height = height // 2
fps = 0

player_pos = 1.5, 5 #mini map
player_angle = 0
player_speed = 0.004
player_rotation_speed = 0.002

fov = math.pi / 3
half_fov = fov / 2
num_rays = width // 2
delta_angle = fov / num_rays
max_depth = 20

screen_dist = half_width / math.tan(half_fov)
scale = width // num_rays

texture_size = 256
half_texture = texture_size // 2
