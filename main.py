# main.py

import sys
from ascii_art_generator_cli import run_cli
from ascii_art_generator_streamlit import run_streamlit


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py [cli|streamlit]")
        sys.exit(1)

    mode = sys.argv[1]

    if mode == "cli":
        run_cli()
    elif mode == "streamlit":
        run_streamlit()
    else:
        print("Invalid mode. Choose 'cli' or 'streamlit'.")
        sys.exit(1)


if __name__ == "__main__":
    main()
