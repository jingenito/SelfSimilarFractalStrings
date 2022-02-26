#   Author: Joe Ingenito
#   Date Created: 2/25/22
#   Description: Contains a class that represents a Self Similar Fractal String, defined using
#               scaling ratios and gaps. 

from TypeModule import FractalScalingType as fsType, ScalingRatio
import numpy as np

class SelfSimilarFractalString:
    """A class that represents a self similar fractal string."""

    def __init__(self, resolution : int, tier : int, scalingRatios : list, _generate_newString = True) :
        #Validate scalingRatios
        sum = 0
        for x in scalingRatios :
            if type(x) != ScalingRatio :
                print('An element of scaling ratios was not a ScalingRatio.')
                return
            else:
                sum += x.Value
        if sum != 1 :
            print('All of the scaling ratios should add to 1.')
            return
        #set properties
        self.Resolution, self.Tier, self.ScalingRatios = resolution, tier, scalingRatios
        if _generate_newString : self._build_StringIterations()

    # @classmethod
    # def fromJSON(cls, filename) :
    #     fs_data = JSON.DeserializeJSON(filename)
    #     x = cls(fs_data['Resolution'],fs_data['Tier'],fs_data['ScalingRatios'],False)
    #     x.Iterations = fs_data['Iterations']
    #     return x

    #these methods are for pickling and unpickling ###################
    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__ = d
    ##################################################################

    def _build_StringIterations(self) :
        """Internal."""
        #each element of iterations is a list that represents the scaling ratios of the ith iteration
        self.Iterations, sRatio = [], ScalingRatio(fsType.Ratio, self.Resolution)
        self.Iterations.append([sRatio])
        for i in range(1, self.Tier + 1) :
            self.Iterations.append([])
            for j in self.Iterations[i-1]:
                if j.Type == fsType.Ratio :
                    self.Iterations[i].extend(self._process_length(j.Value))
                elif j.Type == fsType.Gap :
                    self.Iterations[i].append(j)
                        
    def _process_length(self, length : float) -> list :
        """Internal."""
        level = []
        for sRatio in self.ScalingRatios :
            new_value = sRatio.Value * length
            if sRatio.Type == fsType.Ratio :
                level.append(ScalingRatio(fsType.Ratio, new_value))
            elif sRatio.Type == fsType.Gap :
                level.append(ScalingRatio(fsType.Gap, new_value))
        return level

    def GetFractalString(self, iteration : int) -> list :
        """
            Returns a list that represents the fractal string for the specified iteration, which is by 
            definition the set formed from the gaps at each iteration.
        """
        fstring, max = [], 0
        if iteration > self.Tier : 
            print("The specified iteration is greater than the set Tier.")
            return None
        else:
            for sRatio in self.Iterations[iteration]:
                if sRatio.Type == fsType.Ratio :
                    max += int(np.ceil(sRatio.Value))
                elif sRatio.Type == fsType.Gap :
                    #For the Fractal String we keep the gaps, not the ratios
                    next_max = max + int(np.ceil(sRatio.Value))
                    fstring.extend(range(max, next_max + 1))
                    max = next_max
        return fstring
    
    def GetMaxFractalString(self) -> list :
        """Use this method to get the Fractal String from the maximum iteration."""
        return self.GetFractalString(self.Tier)
                    