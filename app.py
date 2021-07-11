from pprint import pprint
import sys
from cursesmenu import *
from cursesmenu.items import *
from yaml import load
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader

menu = CursesMenu("Menu", show_exit_option=True)

# Read in config
with open('menu.yml', 'r') as file:
    menu_config = load(file, Loader=Loader)

# Add item to menu
for entry in menu_config:
    menu.append_item(CommandItem(entry["name"], entry["command"]))

menu.show()
