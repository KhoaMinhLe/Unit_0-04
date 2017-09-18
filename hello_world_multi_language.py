# Created by: Khoa Le
# Created on September 15 2017
# Created for ICS3U
# This program is the "Hello, World!", but with GUI, buttons and other languages.

import ui

def english_touch_up_inside(sender):
	view['hello_world_label'].text = ("Hello, World!")
	
def french_touch_up_inside(sender):
	view['hello_world_label'].text = ("Bonjour le monde!")
	
def spanish_touch_up_inside(sender):
	view['hello_world_label'].text = ("Hola Mundo!")

view = ui.load_view()
view.present('sheet')
