import pandas as pd
import numpy as np
import astropy as ap
from tqdm.notebook import trange, tqdm
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from astropy.coordinates import SkyCoord  # High-level coordinates
from astropy.coordinates import ICRS, Galactic, FK4, FK5  # Low-level frames
from astropy.coordinates import Angle, Latitude, Longitude  # Angles
import astropy.units as u

from IPython.display import display, Math,HTML


import sys

shape_cat=sys.argv[1]
vol=sys.argv[2]
z_range=sys.argv[3]



if vol=="vlim":
    vol_lim='vlim'
elif vol=="all":
    vol_lim="all"
elif vol=="uber":
    vol_lim="uber"

if z_range=="high_z":
    z="_high_z"
elif z_range=="low_z":
    z="_low_z"
elif z_range=="all_z":
    z=""
else:
    raise
    
clusters=pd.read_pickle('/home/cz136/project/sa/data/{}/{}/clusters{}.pkl'.format(shape_cat,vol_lim,z)) 
shapes=pd.read_pickle('/home/cz136/project/sa/data/{}/{}/shapes{}.pkl'.format(shape_cat,vol_lim,z)) 
random=pd.read_pickle('/home/cz136/project/sa/data/{}/{}/random.pkl'.format(shape_cat,vol_lim))

