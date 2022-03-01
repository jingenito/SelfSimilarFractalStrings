import FractalImages
from SimilarFractalString import CantorString as CString

print('Welcome to the Fractal Image Library')
print('1) Cantor String Image')
print('2) Cantor Lawn Image')
inp = input('Select an image to create: ')

if inp.isnumeric() :
    mode = int(inp)

if mode == 1 :
    FractalImages.CreateCantorStringImage((1000,200),(90,110),4)
elif mode == 2:
    FractalImages.CreateCantorLawnImage((1000,1000),4)