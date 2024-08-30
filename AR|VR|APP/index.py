import cv2
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
clock = pygame.time.Clock()

# Setup OpenGL
glEnable(GL_TEXTURE_2D)
glMatrixMode(GL_PROJECTION)
gluPerspective(45, (800 / 600), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glTranslatef(0.0, 0.0, -5)

# Load Video
video_path = 'path_to_your_video.mp4'
cap = cv2.VideoCapture(video_path)

def get_video_frame(cap):
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 0)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
    else:
        return None

def render_frame(frame, mode='vr'):
    frame = np.array(frame)
    frame_height, frame_width, _ = frame.shape
    texture_id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, frame_width, frame_height, 0, GL_RGB, GL_UNSIGNED_BYTE, frame)

    glBegin(GL_QUADS)
    
    if mode == 'vr':
        # VR Mode: Render as a large screen in front
        glVertex3f(-2, -2, 0)
        glVertex3f(2, -2, 0)
        glVertex3f(2, 2, 0)
        glVertex3f(-2, 2, 0)
    elif mode == 'ar':
        # AR Mode: Render as a small screen on a virtual surface
        glVertex3f(-1, -1, -2)
        glVertex3f(1, -1, -2)
        glVertex3f(1, 1, -2)
        glVertex3f(-1, 1, -2)
    
    glEnd()

    glDeleteTextures(1)

def select_mode():
    print("Select Mode:")
    print("1. VR Mode")
    print("2. AR Mode")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        return 'vr'
    elif choice == '2':
        return 'ar'
    else:
        print("Invalid choice, defaulting to VR mode.")
        return 'vr'

# Main loop
mode = select_mode()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    frame = get_video_frame(cap)
    if frame is not None:
        render_frame(frame, mode=mode)

    pygame.display.flip()
    clock.tick(30)

cap.release()
pygame.quit()
