import xarray as xr
import glob

# Useful paths;
def print_all_mhw_paths():
    # SST DATA
    ghrsst = '/g/data/v45/jr5971/mhw-analysis/ghrsst_data/ghrsst_tas1km.nc'
    oisst = '/g/data/v45/jr5971/notebooks/data/oisst_sst.nc'
    noaa_raw = '/g/data/ia39/aus-ref-clim-data-nci/oisst/data/yearly/'
    biorgn_om2 = '/g/data/v45/jr5971/notebooks/data/sst_spav.nc'
    

    # ANOMALIES
    oissta_eac = '/g/data/v45/jr5971/notebooks/data/oissta_eac.nc'

    # MHW RESULTS
    noaa_mhw = '/g/data/v45/jr5971/mhw-analysis/mhws_noaa/temp_res/'
    ghrsst_mhw = 'jr5971/mhw-analysis/ghrsst_data/'
    
# open mhw results
def open_mhw_results(path, result = ['th*','det*', 'int*']):
    
    

def open_files_after_date(path, pattern, startyear):
    ds_list = glob.glob(path + pattern)
    ds_list.sort()
    newlist = []
    i = 0
    while f'{startyear}' not in ds_list[i]:
        i+=1
    first = i
    newlist = ds_list[first:]
    return newlist
    
def subset_spatially(data, idx):
    try: 
        data = data.sel(lat=slice(idx['S'], idx['N']),
                        lon=slice(idx['W'], idx['E']))
    return data

def combine_mhw_results(datasets, concat_dim):
    ds_combined = xr.combine_nested(datasets, concat_dim)
    return ds_combined





