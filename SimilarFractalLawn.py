#   Author: Joe Ingenito
#   Date Created: 2/26/22
#   Description: Contains a class that represents a Self Similar Fractal Lawn, defined using
#               the SelfSimilarFractalString class. 

from SimilarFractalString import SelfSimilarFractalString as SSFS
import numpy as np

class SelfSimilarFractalLawn:
    """A class that represents a self similar fractal lawn."""

    def __init__(self, fractalStrings : list) :
        self.FractalStrings = {}
        #Validate fractalStrings
        for i in range(len(fractalStrings)) :
            string = fractalStrings[i]
            if type(string) != SSFS :
                print("An element of fractalStrings is not a SelfSimilarFractalString.")
                return
            else: self.FractalStrings[i] = string #setting the dimensions in the order that they are listed
        #setting the tier to the minimum of all the tiers
        self.Tier = int(np.min(list(map(lambda x: x.Tier, fractalStrings))))
        self.Resolution = tuple(list(map(lambda x: x.Resolution, fractalStrings)))

    #these methods are for pickling and unpickling ###################
    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__ = d
    ##################################################################

    def GetFractalLawn(self, iteration : int, dimensions : tuple) -> list :
        """
            Use this method to get the Fractal Lawn at the specified iteration, returns a list with each string
            in each dimension.
        """
        dimCount = len(self.Resolution)
        if iteration > self.Tier :
            print('The iteration is greater than the minimum Tier of all strings.')
            return None
        elif len(dimensions) > len(self.Resolution) :
            print('Length of dimensions tuple is greater than the amount of dimensions.')
            return None
        
        strings = []
        for dim in dimensions :
            if dim > 0 and dim <= len(self.Resolution) :
                strings.append(self.FractalStrings[dim-1].GetFractalString(iteration))
            else: print('Skipping over invalid dimension: ' + str(dim))
        return strings

    def GetMaxTierFractalLawn(self, dimensions : tuple) -> list :
        return self.GetFractalLawn(self.Tier, dimensions)