# Place menu options on the window
def place_menu():
    global menu_buttons
    menu_buttons.clear()
    menu_options = ['New Game', 'Load Game', 'Options', 'Exit']
    button_width = 200
    button_height = 40
    x_position = (root.winfo_width() - button_width) // 2
    y_start_position = (root.winfo_height() - len(menu_options) * (button_height + 10)) // 2
    for index, option in enumerate(menu_options):
        btn = Button(root, text=option, font=("Helvetica", 16, "bold"), fg="white",
                     image=button_photo, compound="center", borderwidth=0,
                     activebackground="gray", command=lambda opt=option: menu_action(opt))
        btn.place(x=x_position, y=y_start_position + index * (button_height + 10), width=button_width, height=button_height)
        menu_buttons.append(btn)

# Define actions for menu options
def menu_action(option):
    if option == "Exit":
        stop_music_and_exit()
    elif option == "Options":
        toggle_options_menu(True)

def toggle_options_menu(show):
    if show:
        for widget in menu_buttons:
            widget.place_forget()
        create_options_menu()
    else:
        volume_slider.place_forget()
        slider_label.place_forget()
        back_btn.place_forget()
        root.update()  # Update the main window to ensure correct dimensions
        place_menu()  # Re-display the main menu buttons

def create_options_menu():
    global volume_slider, back_btn, slider_label
    # Label for the volume slider
    slider_label = Label(root, text="Volume", font=("Helvetica", 14), fg="white", bg="black")
    slider_label.place(relx=0.5, rely=0.4, anchor='center')

    # Volume slider
    volume_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, command=adjust_volume)
    volume_slider.set(pygame.mixer.music.get_volume() * 100)  # Sync slider with current volume
    volume_slider.place(relx=0.5, rely=0.5, anchor='center', width=300)

    # Back button to return to the main menu
    back_btn = Button(root, text="Back", font=("Helvetica", 16), fg="white",
                      bg="black", relief=FLAT, activebackground="gray",
                      command=lambda: toggle_options_menu(False))
    back_btn.place(relx=0.5, rely=0.6, anchor='center', width=200)

def adjust_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)