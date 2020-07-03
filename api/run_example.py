import os
from tester import Tester
import time
import sys 
import os.path 
model_weight_path = 'models/model_weights.pth.tar'
argv = sys.argv[1]

if os.path.exists(argv):
	example_video = sys.argv[1]
else:
	print("File does not exist")

tester = Tester(model_weight_path, batch_size=64, workers=8, quiet=True)
tic = time.time()
results = tester.test(example_video)
took = time.time()-tic
n_frames = results[list(results.keys())[0]].shape[0]
print("Prediction takes {:.4f} seconds for {} frames, average {:.4f} seconds for one frame.".format(
	took, n_frames, took/n_frames))

for video in results.keys():
	print("{} predictions".format(video))
	print(results[video])
