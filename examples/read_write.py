import random as rd
import numpy as np
from pathlib import Path
from tqdm import tqdm
from seriejo import Seriejo, SeriejoWriter

def make():
    x = [rd.randrange(10000) for _ in range(rd.randrange(10) + 1)]
    x = np.array(x, dtype = np.uint16)
    return x


if __name__ == '__main__':
    data = [make() for _ in range(1000000)]

    Path('data/rw').mkdir(parents = True, exist_ok = True)
    with SeriejoWriter('data/rw/a') as f:
        for x in tqdm(data, bar_format = '{l_bar}{r_bar}'):
            f.write(x)

    seri = Seriejo('data/rw/a')
    ok = 0
    for i, x in tqdm(enumerate(data)):
        if (x == seri[i]).all():
            ok += 1
    print('{} / {}'.format(ok, len(data)))

