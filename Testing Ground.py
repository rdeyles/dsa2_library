from PIL import Image
import matplotlib.pyplot as mp
import numpy as np

img = np.asarray(Image.open('/Users/rhysdavideyles/Documents/CS/Github/dsa2_library/maze-2.png'))
print(repr(img))