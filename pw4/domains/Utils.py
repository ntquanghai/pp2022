import math
import numpy as np
import curses
from curses import wrapper

class Utils:
    def find(lst, key, value):
        for i, dic in enumerate(lst):
            if dic[key] == value:
                return i
        return -1
    
    def cursesInput(stdscr,string):
        curses.echo()
        stdscr.addstr(string)
        input = stdscr.getstr()

        return input.decode()