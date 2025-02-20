import curses
import os
import subprocess


def mainOS(stdscr):
    curses.curs_set(0)
    options = ["Windows", "Linux"]
    current_index = 0
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Select your OS (q to exit):")
        for i, option in enumerate(options):
            if i == current_index:
                stdscr.addstr(i + 2, 0, option, curses.A_REVERSE)
            else:
                stdscr.addstr(i + 2, 0, option)
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current_index > 0:
            current_index -= 1
        elif key == curses.KEY_DOWN and current_index < len(options) - 1:
            current_index += 1
        elif key in [10, 13]:
            break
        elif key == ord("q"):
            return None
    return current_index


def get_input(stdscr, prompt):
    curses.echo()
    stdscr.clear()
    stdscr.addstr(0, 0, prompt)
    stdscr.refresh()
    input_str = stdscr.getstr(1, 0).decode("utf-8")
    curses.noecho()
    return input_str


def main(stdscr):
    os_choice = mainOS(stdscr)
    if os_choice is None:
        return
    browser_path = get_input(stdscr, "Enter the Chrome executable path:")
    profile_path = get_input(stdscr, "Enter the profile path:")
    logged_in = get_input(stdscr, "Are you logged in? (1 for yes, 0 for no):")
    file_to_run = os.path.join(
        "./scripts", "botlinkdinW.py" if os_choice == 0 else "botlinkdinL.py"
    )
    stdscr.clear()
    stdscr.addstr(
        0, 0, f"Running bot for {'Windows' if os_choice == 0 else 'Linux'}..."
    )
    stdscr.refresh()
    subprocess.run(["python", file_to_run, browser_path, profile_path, logged_in])
    stdscr.addstr(2, 0, "Bot executed. Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()


if __name__ == "__main__":
    curses.wrapper(main)
