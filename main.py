from SimilarFractalString import SelfSimilarFractalString as FString
from SimilarFractalLawn import SelfSimilarFractalLawn as FLawn
from TypeModule import ScalingRatio as SRatio, FractalScalingType as fsType
import Util.SerializationModule as SerMod
import FractalImages

theRatios = [SRatio(fsType.Ratio,1.0/3.0),
             SRatio(fsType.Gap,1.0/3.0),
             SRatio(fsType.Ratio,1.0/3.0)]
fractalStrings = [FString(1920,4,theRatios),
                  FString(1080,4,theRatios)]
cLawn = FLawn(fractalStrings)
picklefile = 'bin/CantorLawnPickle'
SerMod.PickleData(cLawn,picklefile)
FractalImages.VisualizePickle(picklefile,'Images/CantorLawn4.png')