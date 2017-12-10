#Import defs from plot_basemap.py then compute objective function.
import numpy as np
from plot_basemap import WRF
from plot_basemap import get_TS
from plot_basemap import platform_judge
from plot_basemap import get_speed_pressure_seq
from plot_basemap import get_seq_error
from plot_basemap import get_rain_obs_x_y_z
from plot_basemap import interp_obs
from IPython import embed
def TS_wrapper(data_path,case_name,inner_domain):
	x,long_obs,y,lat_obs,z,monthly_obs = get_rain_obs_x_y_z(data_path,case_name,"default",3)
	CLONG_D02,CLAT_D02,WRFOUT_P_D02,U2,V2 = WRF(inner_domain)
	new_obs = interp_obs(x,y,z,CLONG_D02,CLAT_D02)
	score = get_TS(WRFOUT_P_D02,new_obs)
	over_area = 0
	for i in range(WRFOUT_P_D02.shape[1]):
        	for j in range(WRFOUT_P_D02.shape[2]):
        		if WRFOUT_P_D02.sum(axis=0)[i][j]>3.0*10.0 or new_obs[i][j]>3.0*10.0:
				over_area += 1
	amount_error = abs(WRFOUT_P_D02.sum() - new_obs.sum())/over_area/3.0
	return score,amount_error
def Speed_Pressure_wrapper(wrfout,speed_obs,pressure_obs):
	speed_seq,pressure_seq = get_speed_pressure_seq(wrfout)
	error_speed,error_pressure = get_seq_error(speed_obs,pressure_obs,speed_seq,pressure_seq)
	return error_speed,error_pressure
def loop_over_200_sensible():
	f=open("/vol6/home/ganyj/limengwei/Objectives.txt",'w')
	f.write("Amount_error -TS_score Pressure_error Speed_error\n")
	for number in range(1,201):
		data_path_model = "/vol6/home/ganyj/limengwei/case_run_0_rumbia/WRF_%s/WRF_%s/"%(number,number)
		print "Results--------%s--------------"%number
#		embed();
		score,error_amount = TS_wrapper(data_path,'Rumbia',data_path_model+"wrfout_d02_2013-06-30_00:00:00")
		print "TS score:",score
		print "Cumulative Error:",error_amount,"mm"
		error_speed,error_pressure = Speed_Pressure_wrapper(data_path_model+"wrfout_d01_2013-06-30_00:00:00",speed_Rumbia,pressure_Rumbia)
		print "Pressure Error:",error_pressure.mean()
		print "Speed Error:",error_speed.mean()
		f.write("%s %s %s %s\n"%(round(error_amount),round(-score*100,2),round(error_pressure.mean(),2),round(error_speed.mean(),2)))
	f.close()
	import sys
	sys.exit()
if __name__ == "__main__":
	print "Computing Objectives according to compute_objective.py...."
	case_name = "Rumbia"
#	case_name = "Kongrey"
	mode = "default"
#	mode = "optimized"
	pressure_Rumbia =  [998.0,996.0,992.0,992.0,992.0,990.0,985.0,980.0,976.0,985.0,998.0,1000.0]
	speed_Rumbia =[18.0,20.0,23.0,23.0,23.0,25.0,28.0,30.0,25.0,23.0,18.0,15.0]
	data_path = platform_judge()
	wrfout1 = data_path+'wrfout_d01_%s_%s'%(case_name,mode)
	wrfout2 = data_path+'wrfout_d02_%s_%s'%(case_name,mode)# x,y for interpolation, and z for TS
	
	loop_over_200_sensible()
	
