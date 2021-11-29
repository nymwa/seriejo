import json
import numpy as np
from .util import (
        SeriejoFiles,
        make_view)

class Seriejo:

    def __init__(self, file):
        self.files = SeriejoFiles(file)
        with open(self.files.js, 'r') as f:
            self.i = json.load(f)
        self.pos_view = make_view(self.files.pos, np.int64)
        self.len_view = make_view(self.files.len, np.int16)
        self.dat_view = make_view(self.files.dat, np.uint16)

    def __len__(self):
        return self.i

    def __getitem__(self, index):
        point = self.pos_view[index]
        size = self.len_view[index]
        x = np.frombuffer(self.dat_view, dtype = np.uint16, count = size, offset = point)
        return x

