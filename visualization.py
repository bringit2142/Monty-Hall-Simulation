from matplotlib import pyplot as plt
import monty_hall as mh
import seaborn as sns
import pandas as pd

"""
Run  simulations  and  use  the  conditions  of  the  
simulations  that  we  run,  as well  as  the  percentage  
of  times  that  we  won in  order  to  create  a  visualization  
where  the  x  axis  is how many times we played the game, and 
the y axis is the win percentage.
"""

class Plot:
    """
    This class stores the data for a particular instance of 
    a simulation of the monty hall problem. It contains functionality 
    to export a visualization of the win percentages.
    
    Attributes:
        doors: An integer; The number of doors that the simulation 
        will be based on.
        
        iterations: An integer; The number of iterations that a 
        simulation will be based on.
        
        sequence:  A  list;  Starts  empty,  is  later  populated  
        by  dictionaries  each  containing:  num  of iterations a 
        game was played, percentage won for that simulation, doors 
        used in that simulation, whether the door was switched 
        or not for that simulation.
    
    """
    def __init__(self, doors = 3, iterations = 200):
        """
        Loops for as many times as the value of iterations. 
        Starting at 1, the loop will determine if the current
        value of iteration is odd or even. If even: the loop should
        create an instance of simulation from  the  monty_hall  namespace  
        and  invoke  the  play_game  method. Appends the sequence variable
        with a dictionary of the iterations, percentage, doors and if the user
        switched.
        
        Args:
            doors - An integer; Defaults to 3; The number of doors that the 
            simulation will be based on.
            
            iterations  -  iterations:  An  integer;  Defaults  to  200;  The  
            number  of  iterations  that  a simulation will be based on.  
        
        """
        
        self.doors = doors
        self.iterations = iterations
        self.sequence = []
        self.switch = True
        for i in range(1, iterations + 1):
            if (i % 2) == 0:
                sim = mh.Simulation(doors)
                self.switch = True
                wins = sim.play_game(self.switch, i)
            else:
                sim = mh.Simulation(doors)
                self.switch = False
                wins = sim.play_game(self.switch, i)
            self.sequence.append({"iterations":i, "percentage":wins, 
                                  "doors":self.doors, "switched":self.switch})
        self.make_plot()
        
    def make_plot(self):
        """
        This method will use the sequence attribute to create a pandas Dataframe. 
        We will then use the lmplot method of seaborn in order to create a plot 
        object where x is “iterations”,
        y is “percentage”, data is the pandas dataframe that we created 
        and “hue” is “switched”.
        
        """
        sns.set_theme(color_codes=True)
        df = pd.DataFrame(self.sequence)
        df = sns.lmplot(x = 'iterations', y = 'percentage', data = df, hue='switched')  
        plt.savefig(f"iterations{self.iterations}_doors_{self.doors}.png")      
        
if __name__ == "__main__":
    Plot(3,400)
            
        