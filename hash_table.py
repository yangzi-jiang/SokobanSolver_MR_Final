import sokoban_state


class HashTable:
    def __init__(self):
        self.table = {}

    # sm is SokoMap
    def checkAdd(self, state):
        key = str(state.boxes + [state.player])
        if key in self.table:
            return True
        else:
            self.table[key] = True
            return False

