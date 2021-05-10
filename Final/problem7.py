# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:09:50 2021

@author: akladke
"""

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
    
class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        Campus.__init__(self, center_loc)
        self.center_loc = center_loc
        self.tent_loc = tent_loc
        self.tents = [self.tent_loc]
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        new_loc = str(new_tent_loc).replace("<", "").replace(">", "").split(",")
        new_loc_xy = list(map(float, new_loc))
        x = True
        for i in self.tents:
            cur_loc = str(i).replace("<", "").replace(">", "").split(",")
            cur_loc_xy = list(map(float, cur_loc))
            distance = ((new_loc_xy[0] - cur_loc_xy[0])**2 + (new_loc_xy[1] - cur_loc_xy[1])**2)**0.5
            if new_tent_loc == i or distance < 0.5:
                x = False
        if x == True:
            self.tents.append(new_tent_loc)
            return True
        return False
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        # Throws a value error if not in the tents list,
        # which is the intended functionality
        self.tents.remove(tent_loc)
        
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        new_tents = []
        for i in self.tents:
            new_tents.append(str(i))
        return sorted(new_tents)
        
c = MITCampus(Location(1,2))
print(c.add_tent(Location(1,2)))
print(c.add_tent(Location(0,0)))
print(c.add_tent(Location(2,3)))
print(c.add_tent(Location(2,3)))
print(c.get_tents())

c = MITCampus(Location(1,2),Location(-1,-2))
print(c.add_tent(Location(1,2))) # this should actually work!
print(c.add_tent(Location(-1,-2)))
print(c.add_tent(Location(-1,-2)))
print(c.add_tent(Location(-1,-2)))
print(c.add_tent(Location(-1,-2)))
print(sorted(c.get_tents()))

c = MITCampus(Location(1,2), Location(0,1))
c.add_tent(Location(-1,2))
c.add_tent(Location(1,-10))
c.add_tent(Location(1,10))
c.add_tent(Location(1,20))
c.add_tent(Location(1,40))
print(sorted(c.get_tents()))
#print(check_if_x_sorted(c.get_tents()))

print("--------------------------------------")

c = MITCampus(Location(1,2), Location(3,1))
print(c.add_tent(Location(2.5,1)))
c = MITCampus(Location(1,2), Location(3,1))
print(c.add_tent(Location(2.49,1)))
c = MITCampus(Location(1,2), Location(3,1))
print(c.add_tent(Location(2.51,1)))

print("--------------------------------------")

c = MITCampus(Location(1,2), Location(3,1))
c.add_tent(Location(1,1))
print(c.add_tent(Location(1.5,1)))
c = MITCampus(Location(1,2), Location(3,1))
c.add_tent(Location(1,1))
print(c.add_tent(Location(1.49,1)))
c = MITCampus(Location(1,2), Location(3,1))
c.add_tent(Location(1,1))
print(c.add_tent(Location(1.51,1)))


print("--------------------------------------")

c = MITCampus(Location(1,2), Location(0,1))
c.add_tent(Location(-1,2))
c.add_tent(Location(1,-10))
c.add_tent(Location(1,10))
c.add_tent(Location(1,20))
c.add_tent(Location(1,40))
print(sorted(c.get_tents()))
print(c.get_tents())
#x = sorted(c.get_tents())
#print(c.get_tents == x)
#print(check_if_x_sorted(c.get_tents()))

# l = Location(1, 2)
# m = Location(3, 1)
# print(l.getX())