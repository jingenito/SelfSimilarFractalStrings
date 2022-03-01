#   Author: Joe Ingenito
#   Date Created: 2/25/22
#   Description: A module that computes images of self similar fractal strings. 

from SimilarFractalString import SelfSimilarFractalString as FString, CantorString as CString
from SimilarFractalLawn import SelfSimilarFractalLawn as FLawn, CantorLawn as CLawn
from Util import BinarySearch, ImageMods as ImMods, SerializationModule as SerMod
from TypeModule import ResolutionType as rType
from os import path

ImagePath = 'Images'

def CreateFractalStringImage(fractalString : FString, resolution_Y : int, rowRange : tuple, filename : str == None) :
    """Use this method to create an image representation of the specified Fractal String."""
    if fractalString == None :
        print('The fractalString is null.')
        return
    if resolution_Y <= 0 :
        print('Resolution_Y must be positive.')
        return 
    if len(rowRange) != 2 :
        print('RowRange must be a tuple of length 2.')
        return 
    for i in rowRange:
        if i <= 0 :
            print('RowRange must contain positive numbers.')
            return
        elif i >= resolution_Y:
            print('The values inside of RowRange must be less than resolution_Y.')
    if filename == None or filename.isspace() :
        filename = path.join(ImagePath, 'FractalStringTest' + str(fractalString.Tier) + '.png')

    fstring, bit_array = fractalString.GetMaxFractalString(), []
    for y in range(resolution_Y) :
        bit_array.append([])
        for x in range(fractalString.Resolution) :
            if y >= rowRange[0] and y <= rowRange[1] :
                #draw black if in the cantor string, otherwise draw white
                bit_array[y].append(0 if BinarySearch(fstring, x) != -1 else 1)
            else:
                #draw white inbetween tiers
                bit_array[y].append(1)
    ImMods.BitArrayToImage(bit_array).save(filename)

def CreateFractalLawnImage(fractalLawn : FLawn, filename : str) :
    """Use this method to create an image of the specified fractalLawn, by uses the first two dimensions"""
    if fractalLawn == None :
        print('FractalLawn is null.')
        return
    if filename == None or filename.isspace() :
        filename = path.join(ImagePath, 'FractalLawnTest' + str(fractalLawn.Tier) + '.png')

    bitArray, fLawn = [], fractalLawn.GetMaxTierFractalLawn((1,2))
    for y in range(fractalLawn.Resolution[rType.Height]) :
        if BinarySearch(fLawn[rType.Height],y) != -1 :
            bitArray.append([])
            for x in range(fractalLawn.Resolution[rType.Width]) :
                bitArray[y].append(0 if BinarySearch(fLawn[rType.Width], x) != -1 else 1)
        else:
            bitArray.append([1 for x in range(fractalLawn.Resolution[rType.Width])])
    ImMods.BitArrayToImage(bitArray).save(filename)

def VisualizePickle(filename : str, image_filename : str) :
    """
        Use this method to visualize a pickle file at the specified filename, as long as it can be made into 
        an image.
    """
    fractal = SerMod.UnpickleData(filename)
    if type(fractal) == FString :
        print('Creating fractal string image.')
        CreateFractalStringImage(fractal,(450,550),image_filename)
    elif type(fractal) == FLawn :
        print('Creating fractal lawn image.')
        CreateFractalLawnImage(fractal,image_filename)
    else: print('Pickle must represent either a FractalString or a FractalLawn.')

def CreateCantorStringImage(resolution : tuple, rowRange : tuple, tier : int, filename : str = None) :
    """Use this method to create an image of the CantorString."""
    if filename == None or filename.isspace() :
        filename = 'CantorString' + str(tier) + '.png'
    cString = CString(resolution[rType.Width], tier)
    CreateFractalStringImage(cString,resolution[rType.Height],rowRange,path.join(ImagePath,filename))

def CreateCantorLawnImage(resolution : tuple, tier : int, filename : str = None) :
    """Use this method to create an image of the CantorLawn."""
    if filename == None or filename.isspace() : 
        filename = 'CantorLawn' + str(tier) + '.png'
    cLawn = CLawn(resolution, tier, 2)
    CreateFractalLawnImage(cLawn, path.join(ImagePath,filename))
