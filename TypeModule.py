#   Author: Joe Ingenito
#   Date Created: 2/25/22
#   Description: Contains the enum types and classes that will be used throughout the project.

from enum import Enum

class ResolutionType(int, Enum):
    """ Indeces for all resolution - tuples """
    Width = 0
    Height = 1
    Depth = 2

class FractalScalingType(int, Enum):
    """Types of scaling lengths for defining fractals."""
    Ratio = 0
    Gap = 1

class ScalingRatio :
    """A class the represents a Scaling Type with a value."""
    def __init__(self, type : FractalScalingType, value : float) :
        self.Type, self.Value = type, value

    #these methods are for pickling and unpickling ###################
    def __getstate__(self):
        return self.__dict__

    def __setstate__(self, d):
        self.__dict__ = d
    ##################################################################