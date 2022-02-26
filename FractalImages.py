#   Author: Joe Ingenito
#   Date Created: 2/25/22
#   Description: A module that computes images of self similar fractal strings. 

from SimilarFractalString import SelfSimilarFractalString as SSFS
from TypeModule import ResolutionType as rType
from Util import BinarySearch, ImageMods as ImMods
from PIL import Image

def CreateFractalStringImage(fractalString : SSFS, rowRange : tuple, filename : str) :
    """Use this method to create an image representation of the specified Fractal String."""
    fstring, bit_array = fractalString.GetMaxFractalString(), []
    for y in range(fractalString.Resolution) :
        bit_array.append([])
        for x in range(fractalString.Resolution) :
            if y >= rowRange[0] and y <= rowRange[1] :
                #draw black if in the cantor string, otherwise draw white
                bit_array[y].append(0 if BinarySearch(fstring, x) != -1 else 1)
            else:
                #draw white inbetween tiers
                bit_array[y].append(1)
    ImMods.BitArrayToImage(bit_array).save(filename)
    