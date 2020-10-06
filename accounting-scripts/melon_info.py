"""Print out all the melons in our inventory."""
from melons import melons


def print_melons(melons):
    """Print each melon with corresponding attribute information."""

    for melon, attribute in melons.items():
        print('MELON TYPE:', melon)
        for attribute, value in attribute.items():
            print(attribute, value) 

print_melons(melons)