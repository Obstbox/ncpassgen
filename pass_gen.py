import curses
from curses import wrapper

class Settings:
    def __init__(self, length=8, with_numbers=False, with_symbols=False, with_upper=False):
        self.length = length
        self.with_numbers = with_numbers
        self.with_symbols = with_symbols
        self.with_upper = with_upper

def checkbox(value):
    if value == True:
        return "X"
    else:
        return " "


def main(stdscr):

    passwd_settings = Settings(6, True)

    stdscr.clear()
    curses.curs_set(0)

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # constants
    VERT_WIN_HEIGHT = 20
    HORIZ_WIN_LENGTH  = 84
    PASS_WELCOME_STRING = 'Your new password:'
    PASS_FIELD_MARGIN = 2
    COL_TITLEBAR = curses.color_pair(1)
    COL_GREEN = curses.color_pair(2)
    X_OFFSET = 36

    # может разнести окна по отдельным объектам?
    title_win = curses.newwin(3, HORIZ_WIN_LENGTH, 0, 1)
    title_win.addstr(1, 1, "Password Generation Util", curses.A_REVERSE)
    title_win.chgat(-1, curses.A_REVERSE)
    title_win.border()
    title_win.refresh()

    help_win = curses.newwin(VERT_WIN_HEIGHT, 33, 3, 52)
    help_win.addstr( 1, 1, "Help:", COL_TITLEBAR | curses.A_BOLD)
    help_win.chgat(-1, COL_TITLEBAR) 
    help_win.addstr( 4, 1, "Press 'L' to set length")
    help_win.addstr( 5, 1, "Press 'U' to toggle uppercase")
    help_win.addstr( 6, 1, "Press 'S' to toggle symbols")
    help_win.addstr( 7, 1, "Press 'N' to toggle numbers")
    help_win.addstr( 8, 1, "Press 'G' to generate new")
    help_win.addstr(10, 1, "Press 'Q' for exit")
    help_win.chgat(4, 8, 1, curses.A_BOLD)
    help_win.chgat(5, 8, 1, curses.A_BOLD)
    help_win.chgat(6, 8, 1, curses.A_BOLD)
    help_win.chgat(7, 8, 1, curses.A_BOLD)
    help_win.chgat(8, 8, 1, curses.A_BOLD)
    help_win.chgat(10, 8, 1, curses.A_BOLD)

    help_win.border()
    help_win.refresh()

    settings_win = curses.newwin(VERT_WIN_HEIGHT, 50, 3, 1)
    settings_win.addstr(1, 1, "Options:", COL_TITLEBAR | curses.A_BOLD)
    settings_win.chgat(-1, COL_TITLEBAR) 
    settings_win.addstr(4, 1, "Password Length                   [  ]")
    settings_win.addstr(5, 1, "Include Uppercase (e.g. ABCDEF)   ( )")
    settings_win.addstr(6, 1, "Include Symbols   (e.g. @#$%^&)   ( )")
    settings_win.addstr(7, 1, "Include Numbers   (e.g. 012345)   ( )")
    settings_win.chgat( 4, 35, 4, COL_GREEN) 
    settings_win.chgat( 5, 35, 3, COL_GREEN) 
    settings_win.chgat( 6, 35, 3, COL_GREEN) 
    settings_win.chgat( 7, 35, 3, COL_GREEN) 

    settings_win.attron(COL_GREEN | curses.A_BOLD)
    settings_win.addstr(4, X_OFFSET, str(passwd_settings.length))
    settings_win.addstr(5, X_OFFSET, checkbox(passwd_settings.with_upper))
    settings_win.addstr(6, X_OFFSET, checkbox(passwd_settings.with_symbols))
    settings_win.addstr(7, X_OFFSET, checkbox(passwd_settings.with_numbers))
    settings_win.attroff(COL_GREEN | curses.A_BOLD)
    settings_win.border()
    settings_win.refresh()

    pass_win = curses.newwin(3, HORIZ_WIN_LENGTH, VERT_WIN_HEIGHT+3, 1)
    pass_win.border()
    pass_win.addstr(1, 1, PASS_WELCOME_STRING, COL_TITLEBAR)

    password = "k001_pa$$w0rd"
    password = "k001_p"

    x1 = len(PASS_WELCOME_STRING) + 2
    x2 = pass_win.getmaxyx()[1] - 2
    pass_field_center = int((x2 - x1) / 2 + x1)
    x3 = pass_field_center - int(len(password) / 2)
    margin1 = x3 - PASS_FIELD_MARGIN
    margin2 = x3 + len(password) + PASS_FIELD_MARGIN
    print(margin1, pass_field_center, margin2)
    for i in range(margin1, margin2):
        pass_win.addch(1, i, ' ', COL_GREEN | curses.A_REVERSE | curses.A_BOLD)
    pass_win.addstr(1, pass_field_center - int(len(password) / 2), password, COL_GREEN | curses.A_REVERSE | curses.A_BOLD)

    pass_win.refresh()


    settings_win.getch()

wrapper(main)
