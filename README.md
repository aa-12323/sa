This is a project trying to find out satelite alignment signals in the DES's data. 
Please see arXiv:1605.01065 and arXiv:1704.06273v2 for the papers I am reading. 
<br>
<br>
The other part of this project, the measurement of central alignment, can be found <a href="https://github.com/alduto/intrinsic_alignments">here</a>.

## Table of Content

### <a href="https://github.com/zchvsre/sa/tree/master/lib/src">/lib/src</a>
The source notebooks with empty parameters. The notebooks in output is acquired by run these notebooks with parameters.
### <a href="https://github.com/zchvsre/sa/tree/master/lib/output">/lib/output</a>
The output notebooks organized by [measurement]/[volume]/[z_range]

### <a href="https://github.com/zchvsre/sa/blob/master/lib/src/phi_e_sat.ipynb">phi_e_sat.ipynb</a>
Phi_sat and e calculations and plots.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/model_averaging.ipynb">model_averaging.ipynb</a>
Predictor selection.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/src/header.py"> header.ipynb </a>
Header file to import all common packages.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/src/data_marshalling.ipynb"> data_marshalling.ipynb </a>
Data cleaning and column adding.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/src/properties.ipynb"> properties.ipynb </a>
A file to lookup columns in the catalogs.
### <a href="https://github.com/zchvsre/sa/blob/master/lib/src/treecorr_cross.ipynb"> treecorr.ipynb </a>
2pt function by summing xi and counts in each cluster.
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
Get all the statistics for z-selection and vollim selection\
Fixed the wrong way to use weight in histograms\
Find out that 22.5 and 67.5 bumps have a tight RA distribution
### 2019.10.18
Add Papermill parametrization\
Add code for normalized R
### 2019.10.22
Finish parametrization, changed to log bin and get a signal at the small seperation
### 2019.10.25
Fixed the elipticity correction in im3, got something weird around 0
### 2019.10.26
Fixed the bumps in phi caused by sorting the phi column and using e1/e1 in pa calculation
### 2019.10.27
Fixed the reference axis in measuring position angle, cofirmed that we got a radial alignment at small seperations
### 2019.10.28
Fixed the glitch that is caused by not filling np.empty properly\
Fixed the center theta in phi calculation
### 2019.10.30
Start making ubermember catalog for systematic detection\
### 2019.10.30
Start fixing members associated with multiple clusters\
### 2019.11.1
Making new catalogs with multilple associated clusters\
### 2019.11.2
Made new ubermember catalog
### 2019.11.3
Add quantile comparison of 2pt function
### 2019.11.14
Made background and foreground 2pt. got unexpected results
### 2019.11.15
Get the fraction of redmapper clusters used in cluster lensing 
### 2019.11.23
Change the z_frac code to be vlim\
Wrote code to calculate gammaT\
The code does not work because of memory leakage
### 2019.11.25
Solved the memery leaking problem by use gc.collect()\
The calculation of red satellite in lensing source is not right\
Plotted the impact of satellite alignment on weak lensing mass calibration

## Questions
### What is PFREE?
PFREE is just the probability that the galaxy belongs to the foreground clusters.
### What are the predictors in mcal catalog?

### What are the two features in phi_sat histogram?
Currently we are not sure.\
Update: I fathered those two bumps with my exceptional bug-writing skills.

### How does 2-based coordinate system work?
Check spin-2 groups.

### How does the spherical geometry equation in Alex's code work?
Check astropy package.

### How to get R200m?
Normalize with R__Lambda

### What is the probelm with im3 2pt functions?

### How to make foreground and background galaxies?
Cut out R and cut red_ shift
 
### Should I make empty cluster cut?

### selection effect and errors in redmagic
Shape bias is always multiplicative

### are there other catalogs?

## TODO
2. Linear regression
3. Read DES IA paper
4. Read SDSS IA paper
