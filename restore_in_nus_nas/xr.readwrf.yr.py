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
