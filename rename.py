## Rename numerically

import os
seq = 0

for file in os.listdir("imgs/"):
    full = "imgs/" + file
    os.rename(full, "imgs/" + str(str('%04d' % seq) + "_" + str(file)[6:]))
    seq +=1
