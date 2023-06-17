import os
import basic_search_tool as bst

cli_instruction = [
    """
    [s] Search mode
    [h] Display history
    """
]
mode_option = ['s', 'h']

def cls():
    # function to clear the screen
    if os.name == 'nt':
        _ = os.system('cls')
        # windows
    else:
        _ = os.system('clear')
        # mac or linux

def search_mode():
    return

def cli_mode():
    print(cli_instruction)
    mode = input('Please enter the mode:\n')

    if mode.lower not in mode_option:
        _ = input('Illegal input, press any key to reenter.')
        cls()
        cli_mode()
    
    if mode.lower == 's':
        search_mode()
    
    if mode.lower == 'h':
        bst.show_history()

    exit(0)

if __name__ == '__main__':
    cli_mode()