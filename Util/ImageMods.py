#   Author: Joe Ingenito
#   Date Created: 2/25/22
#   Description: Contains helpful methods to be used with the PIL library to create images.

from PIL import Image, ImageOps 
from TypeModule import ResolutionType

def ReverseImage(originalFileName : str, newFileName : str) :
    print('Opening image...')
    image = Image.open(originalFileName)

    print('Inverting image...')
    inverted_image = ImageOps.invert(image)
    inverted_image.save(newFileName)

    print('Saved Image!')

def BlendImages(image1 : Image, image2 : Image, steps : int) -> list :
    """ Call this method to blend the 2 images with the specified step size """
    newList = []
    #blend over the images with the specified step size
    for x in range(steps) :
        scale = (x + 1) / steps
        img = Image.blend(image1, image2, scale)
        newList.append(img)
    return newList

def BitArrayToImage(bitArray : list) -> Image :
    """ Call this method to convert a bitArray to a PIL Image. """
    _resolution = (len(bitArray[0]), len(bitArray))
    img = Image.new('RGB', (len(bitArray[0]), len(bitArray)), (0,0,0)) 
    pixels = img.load() # Create the pixel map

    for y in range(_resolution[ResolutionType.Height]) :
        for x in range(_resolution[ResolutionType.Width]) :
            pixels[x,y] = (255,255,255) if bitArray[y][x] == 1 else (0,0,0)

    return img