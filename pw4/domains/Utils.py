import math
import numpy as np
import curses
from curses import wrapper
import zipfile

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

    # Function : file_compress
    def file_compress(inp_file_names, out_zip_file):
        compression = zipfile.ZIP_DEFLATED
        zf = zipfile.ZipFile(out_zip_file, mode="w")

        for file_to_write in inp_file_names:
            zf.write(file_to_write, file_to_write, compress_type=compression)
