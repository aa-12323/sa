# satelite_alignment 
This is a project trying to find out satelite alignment signals in the DES's data. 
Please see arXiv:1605.01065 and arXiv:1704.06273v2 for the papers I am reading. 
<br>
<br>
The other part of this project, the measurement of central alignment, can be found <a href="https://github.com/alduto/intrinsic_alignments">here</a>.

## Table of Content
### <a href="https://github.com/zchvsre/sa/blob/master/lib/phi_e_sat.ipynb">phi_e_sat.ipynb</a>
Phi_sat and e calculations and plots.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/model_averaging.ipynb">model_averaging.ipynb</a>
Predictor selection.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/header.ipynb"> header.ipynb </a>
Header file to import all common packages.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/data_marshalling.ipynb"> data_marshalling.ipynb </a>
Data cleaning and column adding.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/properties.ipynb"> properties.ipynb </a>
A file to lookup columns in the catalogs.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/treecorr.ipynb"> treecorr.ipynb </a>
Sum of 2pt function of all individual clusters.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/treecorr_cross.ipynb"> treecorr_cross.ipynb </a>
Weighted average of all 2pt function.
## Journal
### 2019.9.28
Add phi calculation
### 2019.9.29
Add e calculation\
Start linear regression\
Start listing predictors\
Add cluster e calculation
### 2019.9.30
Add weighted phi calculation and e1 e2 statistics\
Add comments to the code
### 2019.10.1
Start to write 2pt functions\
Switch to non-volume-limited catalogues. Got the same result in phi, but both e+ and ex are not zero.
### 2019.10.2
Getting numbers from physical distance treecorr
### 2019.10.4
Produced the correlation function of physical distance
### 2019.10.5
Modified treecorr code in treecorr__cross.ipynb. Got some pathological plots.
### 2019.10.6
Corrected the mistake of not masking the right elipticity in the data processing notebook.\
Got some less pathological 2pt function.
### 2019.10.10
Add z-selection and vollim selection\
Changed folder structure to sync all code for high/low/all z and vollim and not vollim
### 2019.10.11
Get all the statistics for z-selection and vollim selection

## Questions
### What is PFREE?
PFREE is just the probability that the galaxy belongs to the foreground clusters.
### What are the predictors in mcal catalog?

### What are the two features in phi_sat histogram?
Currently we are not sure.

### How does 2-based coordinate system work?
Check spin-2 groups.

### How does the spherical geometry equation in Alex's code work?
Check astropy package.

### How to get R200m?

## TODO
1. 2pt functions of tangential shear (linear bin, both distance and normalized distance)
  R200=1.5R(lambda). 
2. Linear regression
3. Read DES IA paper
4. Read SDSS IA paper
5. Make sure Alex and I are using the same set.

