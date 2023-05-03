""" Demo template """


import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()


def f(arg, kwarg=None):
    pass




def main():

    print(Path.cwd())
    


if __name__ == '__main__':
    main()