import math
import numpy as np
import curses
from curses import wrapper

def cursesInput(stdscr,string):
        curses.echo()
        stdscr.addstr(string)
        input = stdscr.getstr()

        return input.decode()