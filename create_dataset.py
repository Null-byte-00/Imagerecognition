"""
    github: Null-byte-00
    Copyright (C)   Soroush(Amirali) Rafie

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from PIL import Image
import numpy as np
import pandas as pd
import os

class ConvertDir:
    def __init__(self, label, dir, convert=True) -> None:
        self.label = label
        self.dir = dir
        self.image_arrays = []
        if convert:
            self.convert()
    
    def convert(self):
        images = os.listdir(self.dir)
        for image in images:
            im = Image.open(os.path.join(self.dir,image))
            array = np.mean(np.array(im), axis=2)
            bool_array = (array == 255)
            binary_array = bool_array.astype(float)
            self.image_arrays.append(binary_array)

class CreateDataset:
    def __init__(self, dir_paths) -> None:
        data = []
        dirs = []
        for path in dir_paths:
            dirs.append(ConvertDir(path, path))
        for dir in dirs:
            arrs = dir.image_arrays
            for arr in arrs:
                data.append([dir.label, arr])
        self.dataframe = pd.DataFrame(data, columns=['label', 'image']).sample(frac=1)
    
    def save(self,filename='dataset.hdf'):
        self.dataframe.to_hdf(filename, key='dataset')

if __name__ == '__main__':
    c = CreateDataset(['house', 'fish', 'smilingface'])
    c.save()