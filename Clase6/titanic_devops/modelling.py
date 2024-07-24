#=============================================================================#
#         Design Machine learning software model to Classification problem.   #
#.                   Universidad Nacional de Colombia.                        #
#.                              2024.                                         #
#=============================================================================#



# Import Libraries ------------
import pandas as pd 
import numpy as numpy
import matplotlib.pyplot as plt
import tarfile
from pathlib import Path
import urllib.request


# download dataset ---------

def load_titanic_data():
    tarball_path = Path("datasets/titanic.tgz")
    if not tarball_path.is_file():
        Path("datasets").mkdir(parents=True, exist_ok=True)
        url = "https://github.com/ageron/data/raw/main/titanic.tgz"
        urllib.request.urlretrieve(url, tarball_path)
        with tarfile.open(tarball_path) as titanic_tarball:
            titanic_tarball.extractall(path="datasets")
    return [pd.read_csv(Path("datasets/titanic") / filename)
            for filename in ("train.csv", "test.csv")]
    

