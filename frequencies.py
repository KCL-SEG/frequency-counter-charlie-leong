"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if str(item) in frequencies:
            current_value = frequencies.get(str(item))
            frequencies.update({str(item):current_value + 1})
        else:
            frequencies.update({str(item):1})
    return frequencies
