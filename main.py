from TypeModule import ScalingRatio as SRatio, FractalScalingType as fsType
from SimilarFractalString import SelfSimilarFractalString as SSFS
import Util.SerializationModule as SerMod

print('Creating test data.')
data = [SRatio(fsType.Ratio, 1.0/3.0),
        SRatio(fsType.Gap, 1.0/3.0),
        SRatio(fsType.Ratio, 1.0/3.0)]
cString = SSFS(1000,4,data)

print('Finished creating data, now test pickling data.')
filename = 'bin/PickleTest'
SerMod.PickleData(cString,filename)
print('Pickled data, now unpickling data.')
reloaded_string = SerMod.UnpickleData(filename)
print("Unpickled data, test Resolution, Tier : " + str(reloaded_string.Resolution) + ', ' + str(reloaded_string.Tier))
print('Finished test.')