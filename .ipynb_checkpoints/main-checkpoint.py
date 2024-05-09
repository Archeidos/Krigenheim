import os
import tkinter as tk
from tkinter import ttk, StringVar
from tkinter import *
from PIL import Image, ImageTk
import pygame
import random

root = Tk()
root.title("Krigenheim")
root.geometry("800x600")
root.config(background="black")
root.resizable(0,0)

def update_title(event):
    # Update the window title with mouse position
    root.title(f"Mouse Position - x: {event.x}, y: {event.y}")
root.bind('<Motion>', update_title)

# Initialize Pygame for audio
pygame.init()
pygame.mixer.init()

# Determine the path to the directory where this script is running
base_dir = os.path.dirname(os.path.abspath(__file__))

# Build paths to the assets
assets_path = os.path.join(base_dir, 'Assets')
bg_image_path = os.path.join(assets_path, 'krigenheimposter.png')
menu_image_path = os.path.join(assets_path, 'krigenheimmenu.png')
button_image_path = os.path.join(assets_path, 'krigenheimbutton.png')
button2_image_path = os.path.join(assets_path, 'krigenheimbuttonsm.png')
right_image_path = os.path.join(assets_path, 'krigenheimupsm.png')
left_image_path = os.path.join(assets_path, 'krigenheimdownsm.png')
speech_image_path = os.path.join(assets_path, 'speechmed.png')
music_path = os.path.join(assets_path, 'title.mp3')

# Load and play background music
pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)  # Loop indefinitely
pygame.mixer.music.set_volume(0.1)  # Set initial volume to 10%

# Load the background image using Pillow and set it
speech_image = Image.open(speech_image_path)
menu_bg_image = Image.open(menu_image_path)
bg_image = Image.open(bg_image_path)
right_image = Image.open(right_image_path)
left_image = Image.open(left_image_path)
speech_photo_image = ImageTk.PhotoImage(speech_image)
right_photo_image = ImageTk.PhotoImage(right_image)
left_photo_image = ImageTk.PhotoImage(left_image)
menu_photo_image = ImageTk.PhotoImage(menu_bg_image)
bg_photo_image = ImageTk.PhotoImage(bg_image)
background_label = Label(root, image=bg_photo_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Replace cursor
root.config(cursor="cross")

# Load item images

# Blank item frame small
item_blanksm_path = os.path.join(assets_path, 'blankitemsm.png')
item_blanksm_image = Image.open(item_blanksm_path)
item_blanksm_photo_image = ImageTk.PhotoImage(item_blanksm_image)

# Gold
item_gold_path = os.path.join(assets_path, 'item_gold.png')
item_gold_image = Image.open(item_gold_path)
item_gold_photo_image = ImageTk.PhotoImage(item_gold_image)

# Abilities
item_abilities_path = os.path.join(assets_path, 'icons_abilities.png')
item_abilities_image = Image.open(item_abilities_path)
item_abilities_photo_image = ImageTk.PhotoImage(item_abilities_image)

# Abilities Small
item_abilitiessm_path = os.path.join(assets_path, 'icons_abilitiessm.png')
item_abilitiessm_image = Image.open(item_abilitiessm_path)
item_abilitiessm_photo_image = ImageTk.PhotoImage(item_abilitiessm_image)

# Agility
item_agility_path = os.path.join(assets_path, 'icons_agility.png')
item_agility_image = Image.open(item_agility_path)
item_agility_photo_image = ImageTk.PhotoImage(item_agility_image)

# Agility Small
item_agilitysm_path = os.path.join(assets_path, 'icons_agilitysm.png')
item_agilitysm_image = Image.open(item_agilitysm_path)
item_agilitysm_photo_image = ImageTk.PhotoImage(item_agilitysm_image)

# Charisma
item_charisma_path = os.path.join(assets_path, 'icons_charisma.png')
item_charisma_image = Image.open(item_charisma_path)
item_charisma_photo_image = ImageTk.PhotoImage(item_charisma_image)

# Charisma Small
item_charismasm_path = os.path.join(assets_path, 'icons_charismasm.png')
item_charismasm_image = Image.open(item_charismasm_path)
item_charismasm_photo_image = ImageTk.PhotoImage(item_charismasm_image)

# Disposition
item_disposition_path = os.path.join(assets_path, 'icons_disposition.png')
item_disposition_image = Image.open(item_disposition_path)
item_disposition_photo_image = ImageTk.PhotoImage(item_disposition_image)

# Disposition Small
item_dispositionsm_path = os.path.join(assets_path, 'icons_dispositionsm.png')
item_dispositionsm_image = Image.open(item_dispositionsm_path)
item_dispositionsm_photo_image = ImageTk.PhotoImage(item_dispositionsm_image)

# Fortitude
item_fortitude_path = os.path.join(assets_path, 'icons_fortitude.png')
item_fortitude_image = Image.open(item_fortitude_path)
item_fortitude_photo_image = ImageTk.PhotoImage(item_fortitude_image)

# Fortitude Small
item_fortitudesm_path = os.path.join(assets_path, 'icons_fortitudesm.png')
item_fortitudesm_image = Image.open(item_fortitudesm_path)
item_fortitudesm_photo_image = ImageTk.PhotoImage(item_fortitudesm_image)

# Gear
item_gear_path = os.path.join(assets_path, 'icons_gear.png')
item_gear_image = Image.open(item_gear_path)
item_gear_photo_image = ImageTk.PhotoImage(item_gear_image)

# Gear Small
item_gearsm_path = os.path.join(assets_path, 'icons_gearsm.png')
item_gearsm_image = Image.open(item_gearsm_path)
item_gearsm_photo_image = ImageTk.PhotoImage(item_gearsm_image)

# Intelligence
item_intelligence_path = os.path.join(assets_path, 'icons_intelligence.png')
item_intelligence_image = Image.open(item_intelligence_path)
item_intelligence_photo_image = ImageTk.PhotoImage(item_intelligence_image)

# Intelligence Small
item_intelligencesm_path = os.path.join(assets_path, 'icons_intelligencesm.png')
item_intelligencesm_image = Image.open(item_intelligencesm_path)
item_intelligencesm_photo_image = ImageTk.PhotoImage(item_intelligencesm_image)

# Map Large
item_maplg_path = os.path.join(assets_path, 'icons_maplg.png')
item_maplg_image = Image.open(item_maplg_path)
item_maplg_photo_image = ImageTk.PhotoImage(item_maplg_image)

# Map Small
item_mapsm_path = os.path.join(assets_path, 'icons_mapsm.png')
item_mapsm_image = Image.open(item_mapsm_path)
item_mapsm_photo_image = ImageTk.PhotoImage(item_mapsm_image)

# Party
item_party_path = os.path.join(assets_path, 'icons_party.png')
item_party_image = Image.open(item_party_path)
item_party_photo_image = ImageTk.PhotoImage(item_party_image)

# Party Small
item_partysm_path = os.path.join(assets_path, 'icons_partysm.png')
item_partysm_image = Image.open(item_partysm_path)
item_partysm_photo_image = ImageTk.PhotoImage(item_partysm_image)

# Prestige
item_prestige_path = os.path.join(assets_path, 'icons_prestige.png')
item_prestige_image = Image.open(item_prestige_path)
item_prestige_photo_image = ImageTk.PhotoImage(item_prestige_image)

# Prestige Small
item_prestigesm_path = os.path.join(assets_path, 'icons_prestigesm.png')
item_prestigesm_image = Image.open(item_prestigesm_path)
item_prestigesm_photo_image = ImageTk.PhotoImage(item_prestigesm_image)

# Quests
item_quests_path = os.path.join(assets_path, 'icons_quests.png')
item_quests_image = Image.open(item_quests_path)
item_quests_photo_image = ImageTk.PhotoImage(item_quests_image)

# Quests Small
item_questssm_path = os.path.join(assets_path, 'icons_questssm.png')
item_questssm_image = Image.open(item_questssm_path)
item_questssm_photo_image = ImageTk.PhotoImage(item_questssm_image)

# Real Estate
item_realestate_path = os.path.join(assets_path, 'icons_realestate.png')
item_realestate_image = Image.open(item_realestate_path)
item_realestate_photo_image = ImageTk.PhotoImage(item_realestate_image)

# Real Estate Small
item_realestatesm_path = os.path.join(assets_path, 'icons_realestatesm.png')
item_realestatesm_image = Image.open(item_realestatesm_path)
item_realestatesm_photo_image = ImageTk.PhotoImage(item_realestatesm_image)

# Skills
item_skills_path = os.path.join(assets_path, 'icons_skills.png')
item_skills_image = Image.open(item_skills_path)
item_skills_photo_image = ImageTk.PhotoImage(item_skills_image)

# Skills Small
item_skillssm_path = os.path.join(assets_path, 'icons_skillssm.png')
item_skillssm_image = Image.open(item_skillssm_path)
item_skillssm_photo_image = ImageTk.PhotoImage(item_skillssm_image)

# Strength
item_strength_path = os.path.join(assets_path, 'icons_strength.png')
item_strength_image = Image.open(item_strength_path)
item_strength_photo_image = ImageTk.PhotoImage(item_strength_image)

# Strength Small
item_strengthsm_path = os.path.join(assets_path, 'icons_strengthsm.png')
item_strengthsm_image = Image.open(item_strengthsm_path)
item_strengthsm_photo_image = ImageTk.PhotoImage(item_strengthsm_image)

# Wisdom
item_wisdom_path = os.path.join(assets_path, 'icons_wisdom.png')
item_wisdom_image = Image.open(item_wisdom_path)
item_wisdom_photo_image = ImageTk.PhotoImage(item_wisdom_image)

# Wisdom Small
item_wisdomsm_path = os.path.join(assets_path, 'icons_wisdomsm.png')
item_wisdomsm_image = Image.open(item_wisdomsm_path)
item_wisdomsm_photo_image = ImageTk.PhotoImage(item_wisdomsm_image)

# Load class images

# Fighter
class_fighter_path = os.path.join(assets_path, 'class_fighter.png')
class_fighter_image = Image.open(class_fighter_path)
class_fighter_photo_image = ImageTk.PhotoImage(class_fighter_image)
# Engineer
class_engineer_path = os.path.join(assets_path, 'class_engineer.png')
class_engineer_image = Image.open(class_engineer_path)
class_engineer_photo_image = ImageTk.PhotoImage(class_engineer_image)
# Freelancer
class_freelancer_path = os.path.join(assets_path, 'class_freelancer.png')
class_freelancer_image = Image.open(class_freelancer_path)
class_freelancer_photo_image = ImageTk.PhotoImage(class_freelancer_image)
# Marine
class_marine_path = os.path.join(assets_path, 'class_marine.png')
class_marine_image = Image.open(class_marine_path)
class_marine_photo_image = ImageTk.PhotoImage(class_marine_image)
# Adventurer
class_adventurer_path = os.path.join(assets_path, 'class_adventurer.png')
class_adventurer_image = Image.open(class_adventurer_path)
class_adventurer_photo_image = ImageTk.PhotoImage(class_adventurer_image)
# Aristocrat
class_aristocrat_path = os.path.join(assets_path, 'class_aristocrat.png')
class_aristocrat_image = Image.open(class_aristocrat_path)
class_aristocrat_photo_image = ImageTk.PhotoImage(class_aristocrat_image)
# Artificer
class_artificer_path = os.path.join(assets_path, 'class_artificer.png')
class_artificer_image = Image.open(class_artificer_path)
class_artificer_photo_image = ImageTk.PhotoImage(class_artificer_image)
# Charlatan
class_charlatan_path = os.path.join(assets_path, 'class_charlatan.png')
class_charlatan_image = Image.open(class_charlatan_path)
class_charlatan_photo_image = ImageTk.PhotoImage(class_charlatan_image)
# Cleric
class_cleric_path = os.path.join(assets_path, 'class_cleric.png')
class_cleric_image = Image.open(class_cleric_path)
class_cleric_photo_image = ImageTk.PhotoImage(class_cleric_image)
# Druid
class_druid_path = os.path.join(assets_path, 'class_druid.png')
class_druid_image = Image.open(class_druid_path)
class_druid_photo_image = ImageTk.PhotoImage(class_druid_image)
# Knight
class_knight_path = os.path.join(assets_path, 'class_knight.png')
class_knight_image = Image.open(class_knight_path)
class_knight_photo_image = ImageTk.PhotoImage(class_knight_image)
# Lord
class_lord_path = os.path.join(assets_path, 'class_lord.png')
class_lord_image = Image.open(class_lord_path)
class_lord_photo_image = ImageTk.PhotoImage(class_lord_image)
# Merchant
class_merchant_path = os.path.join(assets_path, 'class_merchant.png')
class_merchant_image = Image.open(class_merchant_path)
class_merchant_photo_image = ImageTk.PhotoImage(class_merchant_image)
# Philosopher
class_philosopher_path = os.path.join(assets_path, 'class_philosopher.png')
class_philosopher_image = Image.open(class_philosopher_path)
class_philosopher_photo_image = ImageTk.PhotoImage(class_philosopher_image)
# Ranger
class_ranger_path = os.path.join(assets_path, 'class_ranger.png')
class_ranger_image = Image.open(class_ranger_path)
class_ranger_photo_image = ImageTk.PhotoImage(class_ranger_image)
# Rogue
class_rogue_path = os.path.join(assets_path, 'class_rogue.png')
class_rogue_image = Image.open(class_rogue_path)
class_rogue_photo_image = ImageTk.PhotoImage(class_rogue_image)
# Shaman
class_shaman_path = os.path.join(assets_path, 'class_shaman.png')
class_shaman_image = Image.open(class_shaman_path)
class_shaman_photo_image = ImageTk.PhotoImage(class_shaman_image)
# Sorcerer
class_sorcerer_path = os.path.join(assets_path, 'class_sorcerer.png')
class_sorcerer_image = Image.open(class_sorcerer_path)
class_sorcerer_photo_image = ImageTk.PhotoImage(class_sorcerer_image)
# Summoner
class_summoner_path = os.path.join(assets_path, 'class_summoner.png')
class_summoner_image = Image.open(class_summoner_path)
class_summoner_photo_image = ImageTk.PhotoImage(class_summoner_image)
# Wizard
class_wizard_path = os.path.join(assets_path, 'class_wizard.png')
class_wizard_image = Image.open(class_wizard_path)
class_wizard_photo_image = ImageTk.PhotoImage(class_wizard_image)

# Load button background image
button_image = Image.open(button_image_path)
button_photo = ImageTk.PhotoImage(button_image)
button2_image = Image.open(button2_image_path)
button2_photo = ImageTk.PhotoImage(button2_image)

# Tooltip functionality

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack(ipadx=1)

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

menu_buttons = []  # List to hold menu buttons for toggling visibility

# Place menu options on the window
def place_menu():
    clear_existing_widgets()
    background_label = Label(root, image=bg_photo_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    title_label = Label(root, text="KRIGENHEIM", font=("Helvetica", 20), fg="white", bg="black", image=button_photo, compound="center", borderwidth=0)
    title_label.pack(pady=20)
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
    elif option == "New Game":
        start_new_game()

def start_new_game():
    for widget in menu_buttons:
        widget.place_forget()  # Hide the main menu buttons
    root.config(background="grey")  # Change background color to grey
    create_character_creation_menu()
    create_save_game()  # Initialize save game functionality

def clear_existing_widgets():
    for widget in root.winfo_children():
        widget.destroy()

def create_character_creation_menu():
    clear_existing_widgets()

    adventurer_desc = "The adventurer is a versatile explorer, skilled in various tasks and adaptable to different situations. \nBase Stats: STR 12, CON 12, AGI 12, INT 12, WIS 12, CHA 12"
    aristocrat_desc = "The aristocrat is a refined noble, skilled in diplomacy and etiquette, often wielding influence and wealth. \nBase Stats: STR 10, CON 10, AGI 10, INT 14, WIS 12, CHA 16"
    artificer_desc = "The artificer is a master of crafting and invention, creating magical devices and constructs to aid in their endeavors. \nBase Stats: STR 10, CON 12, AGI 10, INT 16, WIS 14, CHA 10"
    charlatan_desc = "The charlatan is a cunning trickster, adept at deception and manipulation, often using their charisma to sway others. \nBase Stats: STR 10, CON 10, AGI 14, INT 14, WIS 12, CHA 14"
    cleric_desc = "The cleric is a devout follower of a deity, wielding divine magic to heal allies and smite enemies. \nBase Stats: STR 12, CON 14, AGI 10, INT 12, WIS 16, CHA 10"
    druid_desc = "The druid is a guardian of nature, harnessing primal magic to commune with animals, shape-shift, and command the elements. \nBase Stats: STR 12, CON 14, AGI 12, INT 14, WIS 16, CHA 10"
    engineer_desc = "The engineer is a master of machines and technology, inventing gadgets and constructs to solve problems and overcome obstacles. \nBase Stats: STR 12, CON 14, AGI 12, INT 16, WIS 12, CHA 10"
    fighter_desc = "The fighter is a powerful offensive fighter with good damage, high health, but low defense. \nBase Stats: STR 16, CON 14, AGI 12, INT 10, WIS 10, CHA 10"
    freelancer_desc = "The freelancer is a versatile mercenary, skilled in various weapons and tactics, often working for hire. \nBase Stats: STR 14, CON 14, AGI 14, INT 12, WIS 12, CHA 12"
    knight_desc = "The knight is a noble warrior, sworn to protect their lord and uphold chivalry, often clad in heavy armor and wielding a sword. \nBase Stats: STR 14, CON 16, AGI 10, INT 10, WIS 12, CHA 14"
    lord_desc = "The lord is a powerful ruler, commanding authority and leading armies, often possessing vast wealth and resources. \nBase Stats: STR 14, CON 14, AGI 10, INT 14, WIS 14, CHA 16"
    marine_desc = "The marine is a skilled sailor and fighter, adept at naval combat and exploration, often serving in maritime forces. \nBase Stats: STR 14, CON 14, AGI 12, INT 10, WIS 12, CHA 12"
    merchant_desc = "The merchant is a savvy trader, skilled in negotiation and commerce, often amassing wealth and establishing trade routes. \nBase Stats: STR 10, CON 12, AGI 12, INT 14, WIS 12, CHA 14"
    philosopher_desc = "The philosopher is a deep thinker, pondering the mysteries of the universe and seeking knowledge and enlightenment. \nBase Stats: STR 10, CON 12, AGI 10, INT 16, WIS 16, CHA 12"
    ranger_desc = "The ranger is a skilled tracker and survivalist, at home in the wilderness and adept at ranged combat and stealth. \nBase Stats: STR 12, CON 14, AGI 14, INT 12, WIS 14, CHA 10"
    rogue_desc = "The rogue is a cunning thief and infiltrator, skilled in deception and subterfuge, often operating in the shadows. \nBase Stats: STR 12, CON 12, AGI 16, INT 12, WIS 12, CHA 12"
    shaman_desc = "The shaman is a spiritual guide and healer, communing with spirits and wielding primal magic to protect and aid their community. \nBase Stats: STR 12, CON 14, AGI 10, INT 14, WIS 16, CHA 12"
    sorcerer_desc = "The sorcerer is a wielder of innate magic, casting spells with raw power and charisma, often with unpredictable effects. \nBase Stats: STR 10, CON 12, AGI 12, INT 14, WIS 12, CHA 16"
    summoner_desc = "The summoner is a master of conjuration, summoning creatures and entities from other realms to serve their will. \nBase Stats: STR 10, CON 12, AGI 12, INT 16, WIS 14, CHA 12"
    wizard_desc = "The wizard is a scholarly mage, wielding arcane magic with precision and knowledge, often studying ancient tomes and spells. \nBase Stats: STR 10, CON 12, AGI 12, INT 16, WIS 14, CHA 12"

    class_info = {
        "Adventurer": adventurer_desc,
        "Aristocrat": aristocrat_desc,
        "Artificer": artificer_desc,
        "Charlatan": charlatan_desc,
        "Cleric": cleric_desc,
        "Druid": druid_desc,
        "Engineer": engineer_desc,
        "Fighter": fighter_desc,
        "Freelancer": freelancer_desc,
        "Knight": knight_desc,
        "Lord": lord_desc,
        "Marine": marine_desc,
        "Merchant": merchant_desc,
        "Philosopher": philosopher_desc,
        "Ranger": ranger_desc,
        "Rogue": rogue_desc,
        "Shaman": shaman_desc,
        "Sorcerer": sorcerer_desc,
        "Summoner": summoner_desc,
        "Wizard": wizard_desc
    }

    class_names = {
        "0": "Adventurer",
        "1": "Aristocrat",
        "2": "Artificer",
        "3": "Charlatan",
        "4": "Cleric",
        "5": "Druid",
        "6": "Engineer",
        "7": "Fighter",
        "8": "Freelancer",
        "9": "Knight",
        "10": "Lord",
        "11": "Marine",
        "12": "Merchant",
        "13": "Philosopher",
        "14": "Ranger",
        "15": "Rogue",
        "16": "Shaman",
        "17": "Sorcerer",
        "18": "Summoner",
        "19": "Wizard"
    }

    suggested_names = {
        "0": "Johnny Rebel",
        "1": "Seth McFarlane",
        "2": "Christopher Eccleston",
        "3": "Eichiiro Oda",
        "4": "Vin Diesel",
        "5": "Matthew Mercer",
        "6": "Gilbert Gottfried",
        "7": "George Carlin",
        "8": "Piers Morgan",
        "9": "Johnny Depp",
        "10": "Seth Rogen",
        "11": "Chris Hemsworth",
        "12": "Masashi Kishimoto",
        "13": "Dwayne Johnson",
        "14": "Mark Hamill",
        "15": "Robin Williams",
        "16": "John Oliver",
        "17": "Jimmy Fallon",
        "18": "Stephen Colbert",
        "19": "David Letterman",
        "20": "Conan O'Brien",
        "21": "Will Ferrell",
        "22": "Leonardo DiCaprio",
        "23": "Hugh Jackman",
        "24": "Ryan Reynolds",
        "25": "Tom Hanks",
        "26": "Brad Pitt",
        "27": "Johnny Knoxville",
        "28": "Russell Crowe",
        "29": "Tom Cruise",
        "30": "Keanu Reeves",
    }

    class_images = {
        "0": class_adventurer_photo_image,
        "1": class_aristocrat_photo_image,
        "2": class_artificer_photo_image,
        "3": class_charlatan_photo_image,
        "4": class_cleric_photo_image,
        "5": class_druid_photo_image,
        "6": class_engineer_photo_image,
        "7": class_fighter_photo_image,
        "8": class_freelancer_photo_image,
        "9": class_knight_photo_image,
        "10": class_lord_photo_image,
        "11": class_marine_photo_image,
        "12": class_merchant_photo_image,
        "13": class_philosopher_photo_image,
        "14": class_ranger_photo_image,
        "15": class_rogue_photo_image,
        "16": class_shaman_photo_image,
        "17": class_sorcerer_photo_image,
        "18": class_summoner_photo_image,
        "19": class_wizard_photo_image
    }

    class_image_iter = 0
    class_iter = 0
    name_iter = 0
    
    cl_name = ""
    selected_class = tk.StringVar(value=class_names[str(class_iter)])
    
    def update_class_info():
        nonlocal cl_name, class_iter, class_names, class_image_iter, class_images # Accessing outer variables
        class_name = class_names[str(class_iter)]
        class_info_text.config(text=class_info[class_name])
        class_display.config(text=class_names[str(class_iter)])
        class_image.config(image=class_images[str(class_image_iter)])    

    def next_class():
        nonlocal class_iter, class_image_iter
        if class_iter >= 19:
            class_iter = 0
            class_image_iter = 0
        else:
            class_iter = class_iter + 1
            class_image_iter = class_image_iter + 1
        update_class_info()

    def previous_class():
        nonlocal class_iter, class_image_iter
        if class_iter <= 0:
            class_iter = 19
            class_image_iter = 19
        else:
            class_iter = class_iter - 1
            class_image_iter = class_image_iter - 1
        update_class_info()

    # Background for the entire window
    background_label = Label(root, image=menu_photo_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Set the title
    title_label = Label(background_label, text="New Game", font=("Helvetica", 20), fg="white", bg="black", image=button_photo, compound="center", borderwidth=0)
    title_label.pack(pady=15)

    # Back button to return to the main menu
    back_btn = Button(background_label, image=button2_photo, text="Back", font=("Helvetica", 16), fg="white", bg="black", borderwidth=0, relief=FLAT, command=return_to_main_menu, compound="center", activebackground="black")
    back_btn.place(x=20,y=18)

    # Start game button, functionality to be implemented
    start_btn = Button(background_label, image=button2_photo, text="Begin", font=("Helvetica", 16), fg="white", bg="black", borderwidth=0, relief=FLAT, command=return_to_main_menu, compound="center", activebackground="black")
    start_btn.place(x=690,y=18)

    # Character Name Entry with background image
    name_label = Label(image=button2_photo, text=" Name: ", font=("Helvetica", 16), fg="white", bg="black", compound="center", borderwidth=0)
    name_label.place(x=220,y=80)
    name_iter = random.randint(0,30)
    name_entry = Entry(font=("Helvetica", 14), borderwidth=0,fg="white",bg="black")
    name_entry.insert(0, suggested_names[str(name_iter)])
    name_entry.place(x=305,y=90)

    # Class Selection with background images
    class_image = Label(image=class_fighter_photo_image, fg="white", bg="Black", borderwidth=0)
    class_image.place(x=323,y=203)
    left_button = Button(image=left_photo_image, text="", command=previous_class, font=("Helvetica", 14), fg="white", bg="black", borderwidth=0, activebackground="black")
    left_button.place(x=267,y=150)
    class_display = Label(text=class_names[str(class_iter)], font=("Helvetica", 14), image=button_photo, fg="white", bg="black", borderwidth=0, compound="center")
    class_display.place(x=325,y=157,width=150)
    right_button = Button(image=right_photo_image, text="", command=next_class, font=("Helvetica", 14), fg="white", bg="black", borderwidth=0, activebackground="black")
    right_button.place(x=480,y=150)

    # Wealth title
    wealth_display = Label(text="Wealth", font=("Helvetica", 16), fg="white", bg="black", borderwidth=0, image=button2_photo, compound="center")
    wealth_display.place(x=112,y=130)

    # Starting gold displayed for player to see
    gold_image = Label(image=item_gold_photo_image, fg="white", bg="black", borderwidth=0)
    gold_image.place(x=50, y=175)
    gold_display = Label(text="100", font=("Helvetica", 14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    gold_display.place(x=100,y=175,width=50,height=50)
    gold_tooltip = Tooltip(gold_image, "Gold")

    # Starting prestige displayed for player to see
    prestige_image = Label(image=item_prestigesm_photo_image, fg="white", bg="black", borderwidth=0)
    prestige_image.place(x=50, y=225)
    prestige_display = Label(text="10", font=("Helvetica",14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    prestige_display.place(x=100,y=225,width=50,height=50)
    prestige_tooltip = Tooltip(prestige_image, "Prestige")

    # Starting real estate displayed for player to see
    property_image = Label(image=item_realestatesm_photo_image, fg="white", bg="black", borderwidth=0)
    property_image.place(x=50, y=275)
    property_display = Label(text="0", font=("Helvetica",14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    property_display.place(x=100,y=275,width=50,height=50)
    property_tooltip = Tooltip(property_image, "Property")

    # Starting skills displayed for player to see
    skills_image = Label(image=item_skillssm_photo_image, fg="white", bg="black", borderwidth=0)
    skills_image.place(x=150, y=175)
    skills_display = Label(text="3", font=("Helvetica",14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    skills_display.place(x=200,y=175,width=50,height=50)
    skills_tooltip = Tooltip(skills_image, "Skills")

    # Starting abilities displayed for player to see
    abilities_image = Label(image=item_abilitiessm_photo_image, fg="white", bg="black", borderwidth=0)
    abilities_image.place(x=150, y=225)
    abilities_display = Label(text="1", font=("Helvetica",14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    abilities_display.place(x=200,y=225,width=50,height=50)
    abilities_tooltip = Tooltip(abilities_image, "Abilities")

    # Starting party displayed for player to see
    party_image = Label(image=item_partysm_photo_image, fg="white", bg="black", borderwidth=0)
    party_image.place(x=150, y=275)
    party_display = Label(text="1", font=("Helvetica",14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    party_display.place(x=200,y=275,width=50,height=50)
    party_tooltip = Tooltip(party_image, "Party Size")
    
    # Display Area for Class Information
    class_info_text = Label(background_label, image=speech_photo_image, text="", font=("Helvetica", 12), fg="black", bg="black", compound="center", borderwidth=0, justify=tk.LEFT, wraplength=750)
    class_info_text.place(x=18,y=328,width=758)
    update_class_info()  # Update class information initially

    # Starting stats displayed for player to see
    stats_label = Label(image=button2_photo, fg="white", bg="black", borderwidth=0, compound="center", text="Stats", font=("Helvetica",16))
    stats_label.place(x=607,y=130)

    health_label = Label(image=item_blanksm_photo_image,fg="red",bg="red",borderwidth=0,compound="center",text="HP",font=("Helvetica",16))
    health_label.place(x=267,y=210)
    health_display = Label(image=item_blanksm_photo_image,fg="black",bg="red",borderwidth=0,compound="center",text="100",font=("Helvetica",16))
    health_display.place(x=267,y=260)

    mana_label = Label(image=item_blanksm_photo_image,fg="blue",bg="blue",borderwidth=0,compound="center",text="MP",font=("Helvetica",16))
    mana_label.place(x=480,y=210)
    mana_display = Label(image=item_blanksm_photo_image,fg="black",bg="blue",borderwidth=0,compound="center",text="50",font=("Helvetica",16))
    mana_display.place(x=480,y=260)
    
    strength_image = Label(image=item_strengthsm_photo_image, fg="white", bg="black", borderwidth=0)
    strength_image.place(x=547, y=175)
    strength_display = Label(text="12", font=("Helvetica", 14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    strength_display.place(x=597,y=175,width=50,height=50)
    strength_tooltip = Tooltip(strength_image, "Strength")

    fortitude_image = Label(image=item_fortitudesm_photo_image, fg="white", bg="black", borderwidth=0)
    fortitude_image.place(x=547, y=225)
    fortitude_display = Label(text="14", font=("Helvetica", 14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    fortitude_display.place(x=597,y=225,width=50,height=50)
    fortitude_tooltip = Tooltip(fortitude_image, "Fortitude")

    agility_image = Label(image=item_agilitysm_photo_image, fg="white", bg="black", borderwidth=0)
    agility_image.place(x=547, y=275)
    agility_display = Label(text="12", font=("Helvetica", 14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    agility_display.place(x=597,y=275,width=50,height=50)
    agility_tooltip = Tooltip(agility_image, "Agility")

    intelligence_image = Label(image=item_intelligencesm_photo_image, fg="white", bg="black", borderwidth=0)
    intelligence_image.place(x=647, y=175)
    intelligence_display = Label(text="10", font=("Helvetica", 14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    intelligence_display.place(x=697,y=175,width=50,height=50)
    intelligence_tooltip = Tooltip(intelligence_image, "Intelligence")

    wisdom_image = Label(image=item_wisdomsm_photo_image, fg="white", bg="black", borderwidth=0)
    wisdom_image.place(x=647, y=225)
    wisdom_display = Label(text="12", font=("Helvetica", 14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    wisdom_display.place(x=697,y=225,width=50,height=50)
    wisdom_tooltip = Tooltip(wisdom_image, "Wisdom")

    charisma_image = Label(image=item_charismasm_photo_image, fg="white", bg="black", borderwidth=0)
    charisma_image.place(x=647, y=275)
    charisma_display = Label(text="11", font=("Helvetica", 14), fg="black", bg="black", borderwidth=0, image=item_blanksm_photo_image, compound="center")
    charisma_display.place(x=697,y=275,width=50,height=50)
    charisma_tooltip = Tooltip(charisma_image, "Charisma")

def return_to_main_menu():
    clear_existing_widgets()
    title_label = Label(root, text="KRIGENHEIM", font=("Helvetica", 20), fg="white", bg="black", image=button_photo, compound="center", borderwidth=0)
    title_label.pack(pady=20)
    background_label = Label(root, image=bg_photo_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    place_menu()  # Assuming place_menu() is the function to recreate the main menu

def create_save_game():
    save_path = os.path.join(base_dir, 'Saved Games', 'save_game.txt')
    with open(save_path, 'w') as file:
        file.write("New game started with default settings.\n")
        # Add more game state information as needed

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

    # Set the background
    background_label = Label(root, image=menu_photo_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    title2_label = Label(root, text="OPTIONS", font=("Helvetica", 20), fg="white", bg="black", image=button_photo, compound="center", borderwidth=0)
    title2_label.pack(pady=10)
    
    # Label for the volume slider
    slider_label = Label(root, image=button_photo, text="Volume", font=("Helvetica", 14), fg="white", bg="black", compound="center")
    slider_label.place(relx=0.5, rely=0.4, anchor='center', width=200, height=40)

    # Volume slider
    volume_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, command=adjust_volume)
    volume_slider.set(pygame.mixer.music.get_volume() * 100)  # Sync slider with current volume
    volume_slider.place(relx=0.5, rely=0.5, anchor='center', width=300)

    # Back button to return to the main menu
    back_btn = Button(root, image=button_photo, text="Back", font=("Helvetica", 16), fg="white",
                      relief=FLAT, activebackground="black", compound="center",
                      command=lambda: toggle_options_menu(False))
    back_btn.place(relx=0.5, rely=0.6, anchor='center', width=200, height=40)

def adjust_volume(val):
    volume = float(val) / 100
    pygame.mixer.music.set_volume(volume)

# Function to fade in the background
def fade_in(step=0):
    alpha = step / 10  # Adjust steps for a 4-second fade-in (40 steps total)
    bg_photo = ImageTk.PhotoImage(bg_image.point(lambda p: p * alpha))
    background_label.config(image=bg_photo)
    background_label.image = bg_photo  # Keep a reference
    if step < 10:
        fade_task = lambda: fade_in(step + 1)
        root.after(100, fade_task)  # 100 ms interval
    else:
        place_menu()  # Place menu after fade-in complete

# Make sure music stops playing and resources are cleaned up properly when the window is closed
def stop_music_and_exit():
    pygame.mixer.music.stop()
    pygame.quit()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", stop_music_and_exit)

# Initialize fading and window focusing
root.after(100, fade_in)  # Start fade in after focusing

root.mainloop()
