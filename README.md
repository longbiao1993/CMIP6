<img
  src='https://github.com/longbiao1993/CMIP6/blob/main/data/figures/group.log.jpg'
  height='150'
/>

# 

**main dataset information**

[![GitHub][github-badge]][github]
[![Build Status]][actions]
![MIT License][]

[github]: https://github.com/carbonplan/carbonplan.org
[github-badge]: https://badgen.net/badge/-/github?icon=github&label
[build status]: https://github.com/carbonplan/carbonplan.org/actions/workflows/main.yml/badge.svg
[actions]: https://github.com/carbonplan/carbonplan.org/actions/workflows/main.yml
[mit license]: https://badgen.net/badge/license/MIT/blue

The dataset is simulated by WRF4.3 by ERA5 and GCM 6 hourly forcing in NSCC HPC 
1. All output is daily netcdf files with equal area projection at three domains
   (12.5km: south east Asia; 2.5km: around Singapore; 500m: singapore)
2. Files include names with wrfout_d01_year-mon-day_00:00:00 (first running)
   and wrfout_d01_year-mon-day_03:00:00 (restart running)
3. Every file has 8 timesteps (0,3,6,9,12,15,18,21 ; or 3,6,9,12,15,18,21,0)
4. Due to the restart running,there are one or more files named by the same day.
   7 timesteps in the last *_00:00:00 file are the same with the first *_03:00:00 file
   We can select the first timestep in last *_00:00:00 file by xarray, then select required var and mergetime all the file
   Must mind that precpitation include two vars and those are accumulated from the start
5. We offer a shell code (based on cdo) and a python code (based on xarray) which help the 
   user extract the var  from wrfout and combine the vars to file in each year
   shell code (less than 8 minutes a year) is more quick than python code (over 14 minutes a year)
   for single var (Note: the xarray will output file with less size because this lib can maintain higher compression)
## use the dataset
```shell
import xarray as xr
import salem 
import datetime
#Extract WRF variables from NAS; You must mount the NAS by samba in linux or windows
#you must donload the code to your PC and run this in a local folder 
for yr in range(1981,2020):
  #the dirwrf is mount point dir  
  #mon="%02d" % mn
  print(yr)
  dirwrf='/mnt/y/WRF_3domain_fERA5/d02/'+str(yr)+'/'
  ds=xr.open_mfdataset(dirwrf+'wrfout_d02_*',concat_dim='Time',combine='nested')
  #odir is the local dir for saving out data,'./' means present folder
  odir='./'
  #RAINNC is the var name, you can change this to your requirement;
  #the whole output vars is in wrfout.vars_list.txt
  ds.RAINNC.to_netcdf(odir+'RAINNC.'+str(yr)+'.nc')
  #you can also use salem.deacc to de-accumulate the variables(RAINC RAINNC)
  #df=ds.RAINNC.salem.deacc(as_rate=False)
  #df.to_netcdf(odir+'RAINNC.'+str(yr)+'.nc')
  time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
  print(time)
```
## license

All the code in this repository is [MIT](https://choosealicense.com/licenses/mit/) licensed, but we request that you please provide attribution if reusing any of our digital content (graphics, logo, copy, etc.).

## about us

SgCALE is a non-profit organization that uses data and science for climate action. We aim to improve the transparency and scientific integrity of climate solutions with open data and tools. Find out more at [https://SgCALE.github.io/downscaling](https://SgCALE.github.io/downscaling) or get in touch by [opening an issue](https://SgCALE.github.io/downscaling/issues/new) or [sending us an email](mailto:hexg@u.nus.edu).
