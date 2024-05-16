# ascii_art_generator_cli.py

import time
import pyfiglet
from colorama import Fore, Style, init
from loguru import logger
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import InMemoryHistory
from rich.columns import Columns
from rich.console import Console
from tqdm import tqdm

# Initialize colorama
init()

SAMPLE_TEXT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+1234567890abcdefghijklmnopqrstuvwxyz"
USER_TEXT_PROMPT = "Enter the text you want to convert to ASCII art: "
FONT_CHOICE_PROMPT = "Enter the number of the font you want to use: "
SAVE_PROMPT = "Do you want to save the ASCII art to a file? (yes/no): "
CONTINUE_PROMPT = "Do you want to continue? (yes/no): "
USE_SAMPLE_TEXT_PROMPT = "Do you want to use the sample text? (yes/no): "

class AsciiArtGenerator:
    """Generates ASCII art using a specified font."""

    def __init__(self, font='block'):
        self.font = font

    def generate(self, text):
        return pyfiglet.figlet_format(text, font=self.font)

class CLI:
    """Handles all user interactions."""

    def __init__(self):
        self.console = Console()
        self.fonts = pyfiglet.FigletFont.getFonts()

    def display_fonts(self):
        numbered_fonts = [f"{i}. {font}" for i, font in enumerate(self.fonts, start=1)]
        self.console.print(Columns(numbered_fonts))

    def get_font_choice(self):
        while True:
            try:
                font_choice = prompt(FONT_CHOICE_PROMPT, completer=WordCompleter([str(i) for i in range(1, len(self.fonts) + 1)]), history=InMemoryHistory())
                font_choice = int(font_choice)
                if 1 <= font_choice <= len(self.fonts):
                    return self.fonts[font_choice - 1]  # Subtract 1 because list indices start at 0
                else:
                    print(Fore.RED + "Please enter a number within the valid range." + Style.RESET_ALL)
            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a numeric value." + Style.RESET_ALL)

    @staticmethod
    def get_user_text():
        use_sample_text = prompt(USE_SAMPLE_TEXT_PROMPT, completer=WordCompleter(['yes', 'no']), history=InMemoryHistory())
        if use_sample_text.lower() == 'yes':
            return SAMPLE_TEXT
        else:
            return prompt(USER_TEXT_PROMPT, history=InMemoryHistory())

    def ask_to_save(self, ascii_art):
        save_choice = prompt(SAVE_PROMPT, completer=WordCompleter(['yes', 'no']), history=InMemoryHistory())
        if save_choice.lower() == 'yes':
            self.save_to_file(ascii_art)

    @staticmethod
    def ask_to_continue():
        user_choice = prompt(CONTINUE_PROMPT, completer=WordCompleter(['yes', 'no']), history=InMemoryHistory())
        return user_choice.lower() == 'yes'

    @staticmethod
    def save_to_file(ascii_art):
        filename = prompt("Enter the filename to save the ASCII art (without extension): ", history=InMemoryHistory())
        with open(f"{filename}.txt", 'w') as file:
            file.write(ascii_art)
        print(Fore.GREEN + f"ASCII art saved to {filename}.txt" + Style.RESET_ALL)

def run_cli():
    cli = CLI()
    while True:
        cli.display_fonts()
        font = cli.get_font_choice()
        generator = AsciiArtGenerator(font)
        logger.info("Generating ASCII art...")
        for _ in tqdm(range(100)):
            time.sleep(0.01)  # Simulate time delay
        user_text = cli.get_user_text()
        ascii_art = generator.generate(user_text)
        if ascii_art:
            print(Fore.GREEN + "ASCII art generated successfully!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Failed to generate ASCII art." + Style.RESET_ALL)

        print(Fore.CYAN + ascii_art + Style.RESET_ALL)
        cli.ask_to_save(ascii_art)
        if not cli.ask_to_continue():
            break
