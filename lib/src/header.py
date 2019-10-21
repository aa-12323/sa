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

from IPython.display import display, Math


import sys

shape_cat=sys.argv[1]
z_range=sys.argv[2]
vol=sys.argv[3]



if vol=="limited":
    vol_lim='_vollim'
else:
    vol_lim=""

if z_range=="high":
    z="_high_z"
elif z_range=="low":
    z="_low_z"
else:
    z=""

clusters=pd.read_pickle('/home/cz136/project/sa/data/clusters{}{}.pkl'.format(vol_lim,z)) 
shapes=pd.read_pickle('/home/cz136/project/sa/data/shapes{}{}.pkl'.format(vol_lim,z)) 
random=pd.read_pickle('/home/cz136/project/sa/data/random.pkl')

if vol=="limited":
    dir_vol='vollim'
else:
    dir_vol="vol"
    
if z_range=="hight":
    z="_high_z"
elif z_range=="low":
    z="_low_z"
else:
    z=""

dir_string=dir_vol+z

