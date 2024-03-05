import tkinter
import customtkinter
from model.home import Home

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
#app.geometry("800x800")
app.title("Une histoire dont vous êtes le héros!")

home = Home(app)
home.pack()


app.mainloop()

