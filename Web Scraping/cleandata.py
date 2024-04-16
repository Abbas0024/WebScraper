import pandas as pd

# read csv file
df = pd.read_csv("final.csv")

# check number of rows and columns
print(df.shape)

# Delete columns
df.drop(columns=['hyperlink', 'pl_name', 'pl_controvflag', 'pl_pnum', 'pl_orbper', 'pl_orbpererr1', 'pl_orbpererr2', 'pl_orbperlim',
                 'pl_orbsmax', 'pl_orbsmaxerr1', 'pl_orbsmaxerr2', 'pl_orbsmaxlim', 'pl_orbeccen', 'pl_orbeccenerr1', 'pl_orbeccenerr2', 'pl_orbeccenlim',
                 'pl_orbinclerr1', 'pl_orbinclerr2', 'pl_orbincllim', 'pl_bmassj', 'pl_bmassjerr1', 'pl_bmassjerr2', 'pl_bmassjlim', 'pl_bmassprov',
                 'pl_radj', 'pl_radjerr1', 'pl_radjerr2', 'pl_radjlim', 'pl_denserr1', 'pl_denserr2', 'pl_denslim', 'pl_ttvflag',
                 'pl_kepflag', 'pl_k2flag', 'pl_nnotes', 'ra', 'dec', 'st_dist', 'st_disterr1', 'st_disterr2', 'st_distlim', 'gaia_dist',
                 'gaia_disterr1', 'gaia_disterr2', 'gaia_distlim', 'st_optmag', 'st_optmagerr', 'st_optmaglim', 'gaia_gmag', 'gaia_gmagerr',
                 'gaia_gmaglim', 'st_teff', 'st_tefferr1', 'st_tefferr2', 'st_tefflim', 'st_mass', 'st_masserr1', 'st_masserr2', 'st_masslim',
                 'st_rad', 'st_raderr1', 'st_raderr2', 'st_radlim'], inplace=True)

print(df.shape)

# Rename column headers
df = df.rename({
    'pl_hostname': 'solarsystemname',
    'pl.discmethod': 'planetdiscovermethod',
    'pl_orbincline': 'planetorbitalinclination',
    'pl_dens': 'planetdensity',
    'ra_str': 'rightsenses',
    'dc_str': 'strdeclaration',
    'st_teff': 'hosttemperature',
    'st_mass': 'hostmass',
    'st_rad': 'hostradius',

}, axis="columns")

# Save the data into main.csv
df.to_csv("main.csv")
