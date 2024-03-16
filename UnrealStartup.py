import sys
from pathlib import Path
import os 
import unreal
def append_path():

    # Get the directory of the current script
    script_dir = Path(__file__).parent.absolute()

    # Add the script directory to sys.path if it's not already there
    if str(script_dir) not in sys.path:
        sys.path.append(str(script_dir))

    # Construct the path to the 'site-packages' directory
    parent_dir = script_dir.parent
    parent_dir = script_dir.parent
    target_path = parent_dir / "site-packages"

    # Add the 'site-packages' directory to sys.path if it's not already there
    if str(target_path) not in sys.path:
        sys.path.append(str(target_path))

    sys.path = [p for p in sys.path if p is not None]
    

def Menu():
    menus = unreal.ToolMenus.get()

    # __file__ gives the path of the current file; os.path.abspath ensures it's absolute.
    current_file_path = os.path.abspath(__file__)
    main_file_path = os.path.join(current_file_path, "Main.py")

    # # os.path.dirname gets the directory containing the file.
    # current_dir = os.path.dirname(current_file_path)

    # Find the 'Main' menu, this should not fail,
    # but if we're looking for a menu we're unsure about 'if not'
    # works as nullptr check,
    main_menu = menus.find_menu("LevelEditor.MainMenu")
    if not main_menu:
        print("Failed to find the 'Main' menu. Something is wrong in the force!")

    entry = unreal.ToolMenuEntry(
                                name="Python.Tools",
                                # If you pass a type that is not supported Unreal will let you know,
                                type=unreal.MultiBlockType.MENU_ENTRY,
                                # this will tell unreal to insert this entry into the First spot of the menu
                                insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST)
    )
    entry.set_label("Open Stable Diffusion")
    # this is what gets executed on click

    #run the pyside file
    command_to_run = main_file_path.replace('\\', '/')
    entry.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, custom_type='ExecuteFile', string=command_to_run)
    

    # add a new menu called PyTools to the MainMenu bar. You should probably rename the last 3 properties here to useful things for you
    script_menu = main_menu.add_sub_menu(main_menu.get_name(), "StableDiffusionTool", "StableDiffusionTool", "StableDiffusionTool")
    # add our new entry to the new youe
    script_menu.add_menu_entry("Scripts",entry)
    # refresh the UI
    menus.refresh_all_widgets()


append_path()
Menu()