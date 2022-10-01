"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        if item in frequencies:
            current_value = frequencies.get(str(item))
            frequency.update({str(item):current_value + 1})
        else:
            frequency.update({str(item):1})
    return frequencies
