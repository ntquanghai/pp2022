from domains.Class import Class
from domains.Course import Course
from domains.Student import Student
from domains.Utils import Utils
import cursesInput
import output
import math
import numpy as np
import curses
from curses import wrapper
import os
import json

studentList = []

coursesList = [
    {
        "name": "LA",
        "credits": 3,
        "id": 0
    },
    {
        "name": "CN",
        "credits": 3,
        "id": 1
    },
    {
        "name": "PS",
        "credits": 3,
        "id": 2
    },
    {
        "name": "SE",
        "credits": 4,
        "id": 3
    },
    {
        "name": "Python",
        "credits": 5,
        "id": 4
    },
]

if(os.stat("coursesList.txt").st_size == 0):
    with open("coursesList.txt","w") as f:
        f.write(json.dumps((str(coursesList)), indent=4))
else:
    print("List imported.")