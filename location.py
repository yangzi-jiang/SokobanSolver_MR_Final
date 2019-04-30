class Location:
    '''
    Cartesian coordinate
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Location(x, y)

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return str(self.x) + ', ' + str(self.y)

    def space_past_box(self):
        ''' Checks one space pass the box '''
        # Why is this * 2 ?
        return Location(self.x * 2, self.y * 2)