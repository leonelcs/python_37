# files/compression/zip.py
from zipfile import ZipFile

with ZipFile('example.zip', 'w') as zp:
    zp.write('raef.txt')
    zp.write('fear.txt')

with ZipFile('example.zip') as zp:
    zp.extract('raef.txt', 'extract_zip')
    zp.extract('fear.txt', 'extract_zip')