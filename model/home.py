import customtkinter
import pygame
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class Home(customtkinter.CTkFrame):
    def __init__(self, master) -> None:
        
        self.color1 = "#F2DBAE"
        self.color2 = "#D9AB73"
        self.color3 = "#A68358"
        self.color4 = "#594731"
        self.color5 = "#0D0D0D"
        self.text = "L'aventure à portée de main. Voici l'occasion de devenir un puissant guerrier ou un magicien redouté... Vous seul déciderez de la route à suivre, des risques à courir et des créatures à combattre. Bonne chance..."
        
        super().__init__(master, fg_color=self.color5, )
        
        #Background music
        pygame.mixer.init()
        
        self.paused = False
        
        pygame.mixer.music.load("media/background_music.mp3")
        pygame.mixer.music.play(loops=-1)
        
        def play_pause():
            if self.paused:
                pygame.mixer.music.unpause()
                self.paused = False
            else:
                pygame.mixer.music.pause()
                self.paused = True
               
        button = customtkinter.CTkButton(master=self, text="")
        button.configure(fg_color=self.color3, hover_color=self.color2, font=("Webdings", 20), command=play_pause)
        button.grid(
            row=3,
            column=1,
            padx=15,
            pady=15
            )
        
        #Collection title
        collection = customtkinter.CTkLabel(
            master=self,
            text="Dragon d'or",
            font=("Brush Script MT", 50),
            ).grid(
                row=0,
                columnspan=2,
                pady=10) 
        
        #Dragon image
        my_image = customtkinter.CTkImage(
            light_image=Image.open("media/dragon.png"),
            size=(365, 242),
            )
        
        image_label = customtkinter.CTkLabel(
            master=self,
            image=my_image,
            text=""
            ).grid(
                row=1,
                columnspan=2,
                padx=20,
                pady=20)  # display image with a CTkLabel
        
        #Intro Text 
        textbox = customtkinter.CTkTextbox(
            master=self,
            fg_color="transparent",
            font=("Brush Script MT", 30),
            width=600,
            height=250,
            corner_radius=10,
            wrap="word"
            )
        textbox.grid(
            row=2,
            columnspan=2,
            padx=15,
            pady=0
            )
        textbox.insert("0.0", self.text)
        
        #Continue button
        def button_event():
            print("button pressed")

        button = customtkinter.CTkButton(master=self, text="Continuer", command=button_event)
        button.configure(fg_color=self.color3, hover_color=self.color2)
        button.grid(
            row=3,
            column=0,
            padx=15,
            pady=15
            )