import random as rd
from tqdm import tqdm
from seriejo import Seriejo

if __name__ == '__main__':
    for _ in tqdm(range(100000), bar_format = '{l_bar}{r_bar}'):
        data = Seriejo('data/mili/a')
        i = rd.randrange(len(data))
        x = data[i]

