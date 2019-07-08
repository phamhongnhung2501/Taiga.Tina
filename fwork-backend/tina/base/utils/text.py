# -*- coding: utf-8 -*-


def strip_lines(text):
    """
    Given text, try remove unnecesary spaces and
    put text in one unique line.
    """
    output = text.replace("\r\n", " ")
    output = output.replace("\r", " ")
    output = output.replace("\n", " ")

    return output.strip()


def split_in_lines(text):
    """Split a block of text in lines removing unnecessary spaces from each line."""
    return (line for line in map(str.strip, text.split("\n")) if line)
