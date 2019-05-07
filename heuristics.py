from copy import deepcopy
from hash_table import HashTable
from location import Location
import math

class Heuristic:

    def manhattan(self, a, b):
        ''' Manhattan Distance between two points, x is col, y is row '''
        a_x_cord = Location.__x_cord__(a)
        a_y_cord = Location.__y_cord__(a)
        b_x_cord = Location.__x_cord__(b)
        b_y_cord = Location.__y_cord__(b)
        return abs(a_x_cord - b_x_cord) + abs(a_y_cord - b_y_cord)
        
    def euclidean(self, a, b):
        a_x_cord = Location.__x_cord__(a)
        a_y_cord = Location.__y_cord__(a)
        b_x_cord = Location.__x_cord__(b)
        b_y_cord = Location.__y_cord__(b)
        return math.sqrt(float(a_x_cord - b_x_cord)*(a_x_cord - b_x_cord) + float(a_y_cord - b_y_cord)*(a_y_cord - b_y_cord))

    def min_dist(self, obj, targets, h_method):
        '''calculate the minimum distance between an object to a set of coordinates'''
        min_dist = 1000000

        for target in targets:
            if h_method == 'm':
                dist = self.manhattan(obj, target)
            else:
                dist = self.euclidean(obj, target)
            if dist < min_dist:
                min_dist = dist
        return min_dist

    def calc_heuristics(self, board, h_method):
        '''calculate the heuristic value for the current state of board'''
        boxes = set(board.boxes)
        goals = set(board.goals)
        sum = 0.0

        player = board.player
        player_min = float(self.min_dist(player, boxes, h_method))
        # print (player_min)
        sum += player_min

        for box in boxes:
            box_min = float(self.min_dist(box, goals, h_method))
            # print (box_min)
            sum += box_min

        return sum

    def get_heuristics(self, board, h_method = None):
        '''main'''
        # manhattan distance
        if (h_method == 'm'):
            return self.calc_heuristics(board, 'm')
        # euclidean distance
        if (h_method == 'e'):
            return self.calc_heuristics(board, 'e')
        # max of the two - the less the heuristic function undershoots, the better
        return max(self.calc_heuristics(board, 'm'), self.calc_heuristics(board, 'e'))