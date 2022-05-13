import random

"""
Simulates  the  Monty  Hall Problem  given  different  conditions  that  we  
determine  (number  of  times  that  we  play  the  game, whether or not we 
switch doors and how many doors there are).

"""

class Simulation:
    """
    Simulation should take an attribute, an integer, which represents the 
    amount of doors that the simulation will use to play the game.
    
    Attributes: 
    numdoors(Int) - An integer; the number of doors that will be 
    used to play the game.
    
    """
    def __init__(self, numdoors):
        """
        Set  an  attribute  named  numdoors  that  will  be  the  
        number  of  doors  that  will  be  used  to play the game.
        
        """
        self.numdoors = numdoors
        
    def set_random_doors(self):
        """
        Will use numdoors number to create a list containing “zonk” strings. 
        This list should be as  long  as  the  number.  It should then replace 
        one of those items in the list to the string “car” at random.
        
        Returns:
        The randomized list of zonks and cars
        """
        random_num = random.randint(0,self.numdoors - 1)
        zonk_list = ["zonk"] * self.numdoors
        zonk_list[random_num] = "car"
        return zonk_list
    
    def choose_doors(self):
        """
        Call  set_random_doors()  and  save  the  list  to  a  variable.  
        Pick  and  remove  a  random  itemfrom  the  this  list  which 
        represents  the  door  
        that  the  user/contestant  has  chosen.  It should then remove a “zonk” 
        from the list. It should then  pick  and  
        remove  a  random  door  from  the list  as  the  alternate  door.
        
        Returns:
        The contestent door and the alternate door
        """
        game = self.set_random_doors()
        user_choice = int(random.randint(0, len(game) - 1))
        user_choice = game[user_choice]
        game.remove("zonk")
        game.remove(user_choice)
        
        
        alternate_door = int(random.randint(0, len(game) - 1))
        alternate_door = game[alternate_door]
        #game.remove(alternate_door)        
        return (user_choice, alternate_door)
        
    def play_game(self, switch = False, iterations = 1):
        """
        Simulates the Monty Hall game based on how many iterations
        are passed through
        
        Args:
            switch  -  A  boolean;  Default  value  of  False;  
            Determines  whether  a  contestant  decides  to
            switch  their  door  when  playing  the  
            game  and  given  the  option  to  do  so.
            
            iterations  -  An  integer;  Default  value  of  1;  The  number  
            of  times  that  a  person  will  play the  game.  Each  time  they  
            play  a  game  the  doors  should  be  random,  and  the  choices
            should be random.
            
        Returns:
            A float of the percentage of the amount of times the game was won
        
        """
        self.wins = 0.0
        for i in range(iterations):
            user_door, alternate_door = self.choose_doors()
            if switch == True and alternate_door == "car":
                self.wins+=1
                
            if switch == False and user_door == "car":
                
                self.wins+=1
                    
        return self.wins/iterations
        
if __name__ == "__main__":
    test = Simulation(3)
    print(test.play_game(True, 1000))        