from SimilarFractalString import SelfSimilarFractalString as SSFS
from TypeModule import FractalScalingType as fsType, ScalingRatio as SRatio
import FractalImages

print('Beginning Fractal String Testbench.')

print('Starting to build the Cantor String with 2 iterations.')
filename = 'Images/CantorString2_1000.png'
value = 1.0/3.0
ScalingRatios = [SRatio(fsType.Ratio, value),
                 SRatio(fsType.Gap, value),
                 SRatio(fsType.Ratio, value)]
fractalString = SSFS(1000, 2, ScalingRatios)
print('Finished building Cantor String... Saving image.')
FractalImages.CreateFractalStringImage(fractalString, (450,550), filename)
print('Cantor String complete.')

print("Beginning next fractal string test.")
filename = "Images/TestString2_1000.png"
value = 1.0/4.0
ScalingRatios = [SRatio(fsType.Ratio, value),
                 SRatio(fsType.Gap, value),
                 SRatio(fsType.Ratio, value),
                 SRatio(fsType.Gap, value)]
fractalString = SSFS(1000, 2, ScalingRatios)
print('Finished building Test String... Saving image.')
FractalImages.CreateFractalStringImage(fractalString, (450,550), filename)
print('Test String complete.')

print('Testbench complete.')