from location import Location

class Direction:

    '''
    Maps a Location object to character that occupies that coordinate
    '''

    def __init__(self, location, character):
        self.location = location
        self.character = character

    def __str__(self):
        return self.character
