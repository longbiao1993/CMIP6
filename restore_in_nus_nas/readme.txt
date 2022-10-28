#The dataset is simulated by WRF4.3 by ERA5 forcing in NSCC HPC 
#1. All output is daily netcdf files with equal area projection at three domains
#   (12.5km: south east Asia; 2.5km: around Singapore; 500m: singapore)
#2. Files include names with wrfout_d01_year-mon-day_00:00:00 (first running)
#   and wrfout_d01_year-mon-day_03:00:00 (restart running)
#3. Every file has 8 timesteps (0,3,6,9,12,15,18,21 ; or 3,6,9,12,15,18,21,0)
#4. Due to the restart running,there are one or more files named by the same day.
#   7 timesteps in the last *_00:00:00 file are the same with the first *_03:00:00 file
#   We can select the first timestep in last *_00:00:00 file by cdo, then select required var and mergetime all the file
#   Must mind that precpitation include two vars and those are accumulated from the start
#5. We offer a shell code (based on cdo) and a python code (based on xarray) which help the 
#   user extract the var  from wrfout and combine the vars to file in each year
#   shell code (less than 8 minutes a year) is more quick than python code (over 14 minutes a year)
#   for single var (Note: the xarray will output file with less size because this lib can maintain higher compression)
#author: Long Biao (Lanzhou University&&National University of Singapore)
#advisor: He Xiaogang (National University of Singapore)
