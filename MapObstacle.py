import math

import pygame
from ROBOT import Graphics,Robot,Ultrasonic

MAP_DIMENSIONS =(600 ,1200)


# The Envirnment Graphs

gfx = Graphics(MAP_DIMENSIONS,"ROBO.png","MAP.png")

 # robot
start = (200,200)
robot=Robot(start,0.01*3779.52)

# the sensors 
sensors_range = 200 ,math.radians(40)
ultra_sonic = Ultrasonic(sensors_range,gfx.map)

dt=0
last_time =pygame.time.get_ticks()

running = True

# SIMULATION LOOP 
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False
    
    dt =(pygame.time.get_ticks()-last_time)/1000      
    last_time = pygame.time.get_ticks()
    
    gfx.map.blit(gfx.map_img,(0,0))
    
    robot.kinematics(dt)
    gfx.draw_robot(robot.x, robot.y, robot.heading)
    point_cloud =ultra_sonic.sence_obstacles(robot.x, robot.y, robot.heading)
    robot.avoid_abstacles(point_cloud, dt)
    gfx.draw_sensors_data(point_cloud)
    pygame.display.update()