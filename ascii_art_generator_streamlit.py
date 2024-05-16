# ascii_art_generator_streamlit.py

import pyfiglet
import streamlit as st
from colorama import init

# Initialize colorama
init()

SAMPLE_TEXT = "ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+1234567890abcdefghijklmnopqrstuvwxyz"


class AsciiArtGenerator:
    """Generates ASCII art using a specified font."""

    def __init__(self, font='block'):
        self.font = font

    def generate(self, text):
        return pyfiglet.figlet_format(text, font=self.font)


def run_streamlit():
    st.title("ASCII Art Generator")
    fonts = pyfiglet.FigletFont.getFonts()
    font_choice = st.selectbox("Choose a font:", fonts)
    use_sample_text = st.checkbox("Use sample text?")
    if use_sample_text:
        user_text = SAMPLE_TEXT
    else:
        user_text = st.text_input("Enter the text you want to convert to ASCII art:")
    if st.button("Generate ASCII Art"):
        generator = AsciiArtGenerator(font_choice)
        ascii_art = generator.generate(user_text)
        if ascii_art:
            st.success("ASCII art generated successfully!")
            st.code(ascii_art)
            st.download_button(
                label="Download ASCII Art",
                data=ascii_art,
                file_name='ascii_art.txt',
                mime='text/plain'
            )
        else:
            st.error("Failed to generate ASCII art.")
