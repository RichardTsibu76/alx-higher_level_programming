#!/usr/bin/python3
"""This writes a string to file using the write """


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    Args:
        filename (str): name of file
        text (str): contents to be written
    Return:
        the number of characters written
    """
    with open(filename, "w") as task_focus:
        return task_focus.write(text)
