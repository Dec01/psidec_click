import sys
from pygame import mixer
import dearpygui.dearpygui
import dearpygui.dearpygui as dpg
import clicker_window

mixer.init()
mixer.music.load('Psichotropic_Logical_Confusion.mp3')
mixer.music.play()
isMusick = True
dpg.create_context()



def btn_musik_control():
    global isMusick
    if isMusick:
        mixer.music.stop()
        isMusick = False
    else:
        mixer.music.play()
        isMusick = True


def btn_callback_clicker_open():
    clicker_window.isWindow = True
    clicker_window.clicker_winodw()


def btn_callback_start():
    clicker_window.isClicking = True
    clicker_window.set_window()
    clicker_window.clicker_tap()

def exit_program():
    dearpygui.dearpygui.stop_dearpygui()


with dpg.window(tag="PsiDec"):
    with dpg.menu_bar():
        with dpg.menu(label="Control_clicker"):
            btn_menu_start = dpg.add_menu_item(label="Run Cklicker")
            dpg.set_item_callback(btn_menu_start, btn_callback_start)

        with dpg.menu(label="Window"):
            btn_menu_open = dpg.add_menu_item(label="Open window")
            dpg.set_item_callback(btn_menu_open, btn_callback_clicker_open)



    dpg.add_text("privet privet ...")
    dpg.add_text("1. Window > Open window - proverka okna clikera")
    dpg.add_text("1.1.  press 'q' to close window")
    dpg.add_text("2. Run game")
    dpg.add_text("3. Control_clicker > Run Cklicker")
    dpg.add_text("3.1. press 'Alt + c' to stop clicker or RUN")




    btn_exit = dpg.add_button(label="exit")
    dpg.set_item_callback(btn_exit, exit_program)
    btn_music = dpg.add_button(label="music")
    dpg.set_item_callback(btn_music, btn_musik_control)

dpg.create_viewport(title='PsiDec', width=400, height=300)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("PsiDec", True)
dpg.start_dearpygui()
dpg.destroy_context()
