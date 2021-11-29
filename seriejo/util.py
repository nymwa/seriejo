import numpy as np

class SeriejoFiles:

    def __init__(self, file):
        self.js = file + '.json'
        self.pos = file + '.pos'
        self.len = file + '.len'
        self.dat = file + '.dat'


def make_view(filename, dtype):
    mmap = np.memmap(filename, mode = 'r', dtype = dtype)
    view = memoryview(mmap)
    return view

