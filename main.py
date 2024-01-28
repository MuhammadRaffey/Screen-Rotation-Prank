import tkinter as tk
from PIL import Image, ImageTk
import pygame
import rotatescreen
import time
import os

class Prank:
    def __init__(self):
        self.screen = rotatescreen.get_primary_display()

    def rotate_screen(self):
        for i in range(2):
            time.sleep(0.25)
            self.screen.set_portrait_flipped()
            time.sleep(0.25)
            self.screen.set_landscape_flipped()
            time.sleep(0.25)
            self.screen.set_portrait()
            time.sleep(0.25)
            self.screen.set_landscape()
            pygame.mixer.init()
            pygame.mixer.music.load(os.path.join('assets', 'sound.mp3'))



    def prank(self):
        
        pygame.mixer.music.play()
        sc = tk.Tk()
        sc.geometry('1000x600')
        sc.title("Prank ho gya jani")

        logo = Image.open(os.path.join('assets', 'images.jpg'))
        res_logo = logo.resize((1000, 600))
        new_logo = ImageTk.PhotoImage(res_logo)
        image_label = tk.Label(sc, image=new_logo)
        image_label.pack(pady=0, padx=0)

        sc.mainloop()

Raffey = Prank()
Raffey.rotate_screen()  
Raffey.prank()  
