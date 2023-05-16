from tkinter import *
from PIL import ImageTk, Image
from io import BytesIO
from help_and_approve import *


def update_window():
    new_pokemon = give_new_pokemon()
    new_name_pokemon = new_pokemon['name']
    t.configure(text=new_name_pokemon)
    new_pokemon_spite_response = requests.get(sprite_url(new_pokemon))
    new_img_data = new_pokemon_spite_response.content
    new_img = ImageTk.PhotoImage(Image.open(BytesIO(new_img_data)))
    panel.configure(image=new_img)
    panel.image = new_img
    new_fun_fact_response = requests.get(description())
    new_fun_fact = new_fun_fact_response.json()
    new_short = new_fun_fact['flavor_text_entries']
    new_very = new_short[0]
    text3.config(text=new_very['flavor_text'])


root = Tk()
root.title("your pokemon!")
root.configure(background="pink")
root.minsize(500, 500)

# label of the pokemon
text = Label(root, text="congratulations!! you got...", font=('Montserrat', 15), foreground="black", background="pink")
pokemon = give_new_pokemon()
name_pokemon = pokemon['name']
t = Label(root, text=name_pokemon, font=('Montserrat', 25), foreground="black", background="pink")

# image of pokemon
pokemon_spite_response = requests.get(sprite_url(pokemon))
img_data = pokemon_spite_response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel = Label(root, image=img, background="pink")

# stats of pokemon
fun_fact_response = requests.get(description())
fun_fact = fun_fact_response.json()
short = fun_fact['flavor_text_entries']
very = short[0]
text3 = Label(root, text=very['flavor_text'], font=('Montserrat', 15), foreground="black", background="pink", justify=LEFT)

# button
buttonOK = Button(text="okay", font=('Montserrat', 15), width=1, height=1, command=root.destroy, bd=0)
buttonNext = Button(text="next", font=('Montserrat', 15), width=1, height=1, command=update_window, bd=0)
buttonOK.place(x=310, y=300)
buttonNext.place(x=130, y=300)

panel.pack()
text.pack()
t.pack()
text3.pack()

root.update()
root.mainloop()
