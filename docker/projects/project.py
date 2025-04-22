# project.py

import time
import numpy as np
from tqdm import tqdm

total = 100
iter_tqdm = tqdm(range(total))
for i in iter_tqdm:
    iter_tqdm.set_description(f"x = {i/100}, sin = {np.sin(i/100):.4f}")
    time.sleep(1)


# import time
# import numpy as np

# total = 1000
# for i in range(total):
#     print(f"sin({i/100}) = {np.sin(i/100):.4f}")
#     time.sleep(1)