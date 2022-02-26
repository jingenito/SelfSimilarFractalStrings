from SimilarFractalString import SelfSimilarFractalString as SSFS
from TypeModule import ScalingRatio as SRatio, FractalScalingType as fsType
from Util import JSONSerializer as JSON

def BuildTestString(resolution : int, tier : int) :
    scalingLen, filename = 1.0 / 4.0, 'bin/TestString.json'
    scalingRatios = [SRatio(fsType.Ratio, scalingLen),
                    SRatio(fsType.Gap, scalingLen),
                    SRatio(fsType.Ratio, scalingLen),
                    SRatio(fsType.Gap, scalingLen)]

    print("Building the Cantor String Model")
    cantorString = SSFS(resolution, tier, scalingRatios)
    print("Finished, serializing data.")
    JSON.SerializeJSON(cantorString, filename)
    print("Testbench complete.")