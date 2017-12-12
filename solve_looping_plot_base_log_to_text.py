#Import defs from plot_basemap.py then compute objective function.
import numpy as np
from IPython import embed

fill_value = 999999
def get_log(filename):
    f = open(filename)
    log = f.readlines()
    logs = ""
    for i in log:
        logs=logs+i
    logs = logs.split("x is")
    logs.pop(0) #pop out "rm: cannot remove .log"
    return logs
def get_list(obj_name):
    this_list = np.empty(0)
    for index,i in enumerate(logs):
        i = i.split('\n')
        flag = 0
        for j in i:
            if j.find(obj_name)>=0:
                #print j.split()
                this_list = np.append(this_list,float(j.split()[-1]))
                flag = 1
        if flag != 1:
            print "Bad log in %s when doing %s, filling a value"%(index+1,obj_name),fill_value
            this_list = np.append(this_list,fill_value)  #wrfout solve error, ignore and fill it.
    return this_list
def fill_value_to_normal_mean_value(seq):
    normal_mean = seq[np.where(seq!=fill_value)].mean()
    seq[np.where(seq==fill_value)] = normal_mean
    print "Filling:",normal_mean
    return seq
def write_data_file():
    f=open("./Objectives_%s.txt"%filename.split('.')[-2],'w')
    f.write("Amount_error -TS_score Pressure_error Speed_error\n")
    for i in range(speed_list.shape[0]):
        f.write("%s %s %s %s\n"%(round(cumulative_list[i],2),round(-ts_list[i]*100,2),round(pressure_list[i],2),round(speed_list[i].mean(),2)))
    f.close()
#

if __name__ == "__main__":
    for filename in ("rm0.log","ut1.log","jb2.log","tm3.log","kr4.log"):
        print "Solving-------------------------------------:",filename
        logs = get_log(filename)
        speed_list = get_list("Speed_")
        pressure_list = get_list("Pressure_")
        cumulative_list = get_list("_rainfall_cumulative_error_is:")
        ts_list = get_list("Rain_Score_")
        speed_list = fill_value_to_normal_mean_value(speed_list)
        pressure_list = fill_value_to_normal_mean_value(pressure_list)
        cumulative_list = fill_value_to_normal_mean_value(cumulative_list)
        ts_list = fill_value_to_normal_mean_value(ts_list)
        
        write_data_file()