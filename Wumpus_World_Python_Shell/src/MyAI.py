# ======================================================================
# FILE:        MyAI.py
#
# AUTHOR:      Abdullah Younis
#
# DESCRIPTION: This file contains your agent class, which you will
#              implement. You are responsible for implementing the
#              'getAction' function and any helper methods you feel you
#              need.
#
# NOTES:       - If you are having trouble understanding how the shell
#                works, look at the other parts of the code, as well as
#                the documentation.
#
#              - You are only allowed to make changes to this portion of
#                the code. Any changes to other portions of the code will
#                be lost when the tournament runs your code.
# ======================================================================

from Agent import Agent

class MyAI ( Agent ):


    class Position:
        
        def __init__ (self, x, y,direction):
            self.x = x
            self.y = y
            self.direction = direction

        def get_position(self):
            return (self.x,self.y)
        def turn (self, RoL):
            if RoL == 'right':
                if self.direction == 'E':
                    self.direction = 'S'
                elif self.direction == 'N':
                    self.direction = 'E'
                elif self.direction == 'W':
                    self.direction = 'N'
                elif self.direction == 'S':
                    self.direction = 'W'
            if RoL == 'left':
                if self.direction == 'E':
                    self.direction = 'N'
                elif self.direction == 'N':
                    self.direction = 'W'
                elif self.direction == 'W':
                    self.direction = 'S'
                elif self.direction == 'S':
                    self.direction = 'E'

        def move(self):
            if self.direction == 'E':
                self.x += 1
            elif self.direction == 'N':
                self.y += 1
            elif self.direction == 'W':
                self.x -= 1
            elif self.direction == 'S':
                self.y -= 1


    def __init__ ( self ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        self.gold = self.dead = self.shot = False
        self.position  = self.Position(0,0,'E')
        self.track = [(0,0)]
        self.back = False
        self.up_limit = 100
        self. right_limit = 100
        self.visited = [(0,0)]
        self.next_position = (0,0)
        pass
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================

    def getAction( self, stench, breeze, glitter, bump, scream ):
        # ======================================================================
        # YOUR CODE BEGINS
        # ======================================================================
        if self.back:
            return self.go_home()
        if glitter: 
            self.gold = True
            self.back = True
            return Agent.Action.GRAB
        if bump:
            self.position.x= self.track[-2][0]
            self.position.y = self.track[-2][1]
            self.space_limit()
            self.track.pop(-1)
            self.next_position = self.position.get_position()
        if breeze or stench:
            return self.go_home()

        if self.position.get_position() == self.next_position:
            next_list = self.adjacent_node()
            
            if not next_list:
                return self.go_home()
            self.next_position = next_list[0]
        return self.move_to_next(self.position.get_position(),self.next_position,False)
        # ======================================================================
        # YOUR CODE ENDS
        # ======================================================================
    
    # ======================================================================
    # YOUR CODE BEGINS
    # ======================================================================
    def space_limit(self):
        if self.position.direction == 'N':
            self.up_limit = self.position.y 
        if self.position.direction == 'E':
            self.right_limit = self.position.x

    def adjacent_node(self):
        x,y = self.position.get_position()
        left = (x-1,y)
        right = (x+1, y)
        up = (x,y+1)
        down = (x,y-1) 
        l = []
        if y > 0 and (down not in self.visited):
            l.append(down)
        if y < self.up_limit and (up not in self.visited):
            l.append(up)
        if x > 0 and (left not in self.visited):
            l.append(left)
        if x < self.right_limit and (right not in self.visited):
            l.append(right)
        return l

    def move_to_next(self,current_position, next_position,back):
        if (current_position[0]) == (next_position[0]):
            if (current_position[1]) > (next_position[1]):
                if self.position.direction == 'S':
                    if back == False and (next_position not in self.track):
                        self.visited.append(next_position)
                        self.track.append(next_position)
                    else:
                        self.track.pop(-1)
                    self.position.move()
                    return Agent.Action.FORWARD
                if self.position.direction == 'N':
                    self.position.turn('left')
                    return Agent.Action.TURN_LEFT
                if self.position.direction == 'W':
                    self.position.turn('left')
                    return Agent.Action.TURN_LEFT
                if self.position.direction == 'E':
                    self.position.turn('right')
                    return Agent.Action.TURN_RIGHT
            elif current_position[1] < next_position[1]:
                    if self.position.direction == 'N':
                        if back == False and (next_position not in self.track):
                            self.visited.append(next_position)
                            self.track.append(next_position)
                        else:
                            self.track.pop(-1)
                        self.position.move()
                        return Agent.Action.FORWARD
                    if self.position.direction == 'S':
                        self.position.turn('left')
                        return Agent.Action.TURN_LEFT
                    if self.position.direction == 'E':
                        self.position.turn('left')
                        return Agent.Action.TURN_LEFT
                    if self.position.direction == 'W':
                        self.position.turn('right')
                        return Agent.Action.TURN_RIGHT
        if current_position[1] == next_position[1]:
            if current_position[0] > next_position[0]:
                if self.position.direction == 'W':
                    if back == False and (next_position not in self.track):
                        self.visited.append(next_position)
                        self.track.append(next_position)
                    else:
                        self.track.pop(-1)
                    self.position.move()
                    return Agent.Action.FORWARD
                if self.position.direction == 'E':
                    self.position.turn('left')
                    return Agent.Action.TURN_LEFT
                if self.position.direction == 'N':
                    self.position.turn('left')
                    return Agent.Action.TURN_LEFT
                if self.position.direction == 'S':
                    self.position.turn('right')
                    return Agent.Action.TURN_RIGHT
            elif current_position[0] < next_position[0]:
                    if self.position.direction == 'E':
                        if back == False and (next_position not in self.track):
                            self.visited.append(next_position)
                            self.track.append(next_position)
                        else:
                            self.track.pop(-1)
                        self.position.move()
                        return Agent.Action.FORWARD
                    if self.position.direction == 'W':
                        self.position.turn('left')
                        return Agent.Action.TURN_LEFT
                    if self.position.direction == 'S':
                        self.position.turn('left')
                        return Agent.Action.TURN_LEFT
                    if self.position.direction == 'N':
                        self.position.turn('right')
                        return Agent.Action.TURN_RIGHT
    def go_home(self):
        if len(self.track) == 1:
            return Agent.Action.CLIMB
        self.next_position = self.track[-2]
        return self.move_to_next(self.position.get_position(),self.next_position,True)  

    # ======================================================================
    # YOUR CODE ENDS
    # ==
    #====================================================================
