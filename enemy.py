from character import Character

class Enemy(Character):
    #Leaving this empty, but at some point we'll probably want special behavior
    #for enemies

    def charSpecificUpdate(self):
        if(self.velY == 0):
            self._load_image( self.stand )

class CaptainRussia(Enemy):
	numWalkFrames = 4        #number pics in move anim
	walkDelay = 2        #delay factor to make anims visible

	#movement vars
	runVel = 10     #xcoord movement velocity
	jumpVel = 25    #jumping velocity

	animFolder = 'captnrussia'
