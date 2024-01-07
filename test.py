import FractalImages
from SimilarFractalString import SelfSimilarFractalString as FractalString, CantorString
from SimilarFractalLawn import SelfSimilarFractalLawn as FractalLawn, CantorLawn
from TypeModule import FractalScalingType as fsType, ScalingRatio as sRatio

fractal = FractalString(3880, 5, [sRatio(fsType.Ratio, 1.0/2.0), sRatio(fsType.Gap, 1.0/4.0), sRatio(fsType.Ratio, 1.0/4.0)])
cantor = CantorString(2160, 5)

flawn = FractalLawn([fractal, cantor])
FractalImages.CreateFractalLawnImage(flawn, 'test.png')
FractalImages.CreateFractalStringImage(fractal, 2160, (90,110), '2-4-string.png')