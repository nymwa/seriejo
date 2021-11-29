import random as rd
from pathlib import Path
from tqdm import tqdm
from seriejo import SeriejoWriter

if __name__ == '__main__':
    Path('data/mili').mkdir(parents = True, exist_ok = True)

    with SeriejoWriter('data/mili/a') as f:
        for i in tqdm(range(1000000)):
            x = [rd.randrange(10000) for _ in range(rd.randrange(100) + 1)]
            f.write(x)
