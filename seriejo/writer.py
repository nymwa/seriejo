import json
import struct
from .util import SeriejoFiles

class SeriejoWriter:

    def __init__(self, file):
        self.files = SeriejoFiles(file)
        self.i = 0
        self.json_file = open(self.files.js, 'w')
        self.pos_file = open(self.files.pos, 'wb')
        self.len_file = open(self.files.len, 'wb')
        self.dat_file = open(self.files.dat, 'wb')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        json.dump(self.i, self.json_file)
        self.json_file.close()
        self.pos_file.close()
        self.len_file.close()
        self.dat_file.close()

    def write(self, lst):
        self.i += 1
        point = self.dat_file.tell()
        self.pos_file.write(struct.pack('l', point))
        self.len_file.write(struct.pack('h', len(lst)))
        for x in lst:
            self.dat_file.write(struct.pack('H', x))

