## Rename numerically
## has to be run outside of /tools

import os
seq = 0

for file in os.listdir("imgs/clean_inferno"):
    full = "imgs/clean_inferno/" + file
    os.rename(full, "imgs/clean_inferno/" + str(str('%04d' % seq) + "_" + str(file)))
    seq +=1
