import curses
import os
import subprocess

SCRIPTS_DIR = "./scripts"


def mainOS(stdscr):
    curses.curs_set(0)
    options = ["Windows", "Linux7w7"]
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
            return
    stdscr.clear()
    stdscr.addstr(0, 0, f"You Selected: {options[current_index]}")
    stdscr.refresh()
    stdscr.getch()


def list_scripts():
    return [f for f in os.listdir(SCRIPTS_DIR) if f.endswith(".py")]


def run_script(script_name):
    script_path = os.path.join(SCRIPTS_DIR, script_name)
    subprocess.run(["python", script_path])


def main(stdscr):
    curses.curs_set(0)
    scripts = list_scripts()
    if not scripts:
        stdscr.addstr(0, 0, "No scripts found in the folder.")
        stdscr.refresh()
        stdscr.getch()
        return
    current_index = 0
    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Select a script to run (q to exit):")
        for idx, script in enumerate(scripts):
            if idx == current_index:
                stdscr.addstr(idx + 2, 0, f"> {script}", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 2, 0, f"  {script}")
        stdscr.refresh()
        key = stdscr.getch()
        if key == curses.KEY_UP and current_index > 0:
            current_index -= 1
        elif key == curses.KEY_DOWN and current_index < len(scripts) - 1:
            current_index += 1
        elif key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(0, 0, f"Running {scripts[current_index]}...")
            stdscr.refresh()
            run_script(scripts[current_index])
            stdscr.addstr(2, 0, "Script executed. Press any key to return to the menu.")
            stdscr.refresh()
            stdscr.getch()
        elif key == ord("q"):
            break


if __name__ == "__main__":
    curses.wrapper(mainOS)
    curses.wrapper(main)
