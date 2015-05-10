import ship
class player_object (ship.ship_object):
        def __init__(self,art,context_size,context,weapon):
            ship.ship_object.__init__(self,art,context_size,context,weapon) # add weapon

        def update(self):
            if self.pos[0]+self.vel[0]>=0 and self.pos[0]+self.vel[0]+32<=self.context_size[0]:
                self.pos[0] = self.pos[0]+self.vel[0]
            if self.pos[1]+self.vel[1]>=0 and self.pos[1]+self.vel[1]+32<=self.context_size[1]:
                self.pos[1] = self.pos[1]+self.vel[1]
                
            print("ship position: " + str(self.pos))
            self.weapon.set_pos(self.pos)
