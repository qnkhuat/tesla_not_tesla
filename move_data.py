import os
from glob import glob
import shutil




for cl in ['tesla','others']:
    
    os.makedirs(f'data/train/{cl}',exist_ok=True)
    os.makedirs(f'data/valid/{cl}',exist_ok=True)
    os.makedirs(f'data/test/{cl}',exist_ok=True)

    ls = glob(f'data/images/{cl}/*')
    valid_ck = int(len(ls)*.7)
    test_ck = int(len(ls)*.9)


    for f in ls[:valid_ck]:
        dest = f'data/train/{cl}'
        shutil.move(f,dest)

    for f in ls[valid_ck:test_ck]:
        dest = f'data/valid/{cl}'
        shutil.move(f,dest)

    for f in ls[test_ck:]:
        dest = f'data/test/{cl}'
        shutil.move(f,dest)




