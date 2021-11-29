import random as rd
from tqdm import tqdm
from seriejo import Seriejo

if __name__ == '__main__':
    dataset = Seriejo('data/mili/a')
    for _ in tqdm(range(100000)):
        i = rd.randrange(len(dataset))
        x = dataset[i]

