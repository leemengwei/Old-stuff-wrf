import numpy as np
from IPython import embed
import matplotlib.pyplot as plt
import copy
from time import sleep
def value_plot(part_Cumulative,part_TS,part_Pressure,part_Speed,title):
	plt.plot(part_Cumulative,label="Cumulative")
	plt.plot(part_TS,label="-TS")
	plt.plot(part_Speed,label="Speed")
	plt.plot(part_Pressure,label="Pressure")
	plt.plot((part_Cumulative+part_Pressure+part_TS+part_Speed),label="Total")
	plt.title("Normalized individual objective for: %s"%title)
        plt.legend()
def correlation_plot(part_Cumulative,part_TS,part_Pressure,part_Speed):
        plt.scatter(part_Cumulative,part_TS,label='Cumulative&TS: %s'%round(np.corrcoef(part_Cumulative,part_TS)[0,1],3))
        plt.scatter(part_Pressure,part_Cumulative,label='Pressure&Cumulative: %s'%round(np.corrcoef(part_Pressure,part_Cumulative)[0,1],3))
        plt.scatter(part_Cumulative,part_Speed,label='Cumulative&Speed: %s'%round(np.corrcoef(part_Cumulative,part_Speed)[0,1],3))
        plt.scatter(part_Pressure,part_TS,label='Pressure&TS: %s'%round(np.corrcoef(part_Pressure,part_TS)[0,1],3))
        plt.scatter(part_Speed,part_TS,label='Speed&TS: %s'%round(np.corrcoef(part_Speed,part_TS)[0,1],3))
        plt.scatter(part_Pressure,part_Speed,label='Pressure&Speed: %s'%round(np.corrcoef(part_Pressure,part_Speed)[0,1],3))
        plt.legend()
def data_normalizing(data_in):   #Function defined with C++ pointer...
        data_in[:] = (data_in-data_in.mean())/data_in.std()   #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!For the first time, I notice that this [:] can serves as 'pointer'/'return'
        
if __name__ == "__main__":
    cheat_spec = []
    case_list = ['Objectives_rm0.txt','Objectives_ut1.txt','Objectives_jb2.txt','Objectives_tm3.txt','Objectives_kr4.txt']
    for txtname in case_list:
	data = np.loadtxt(txtname)
	part_Cumulative = data[:,0]
        part_TS = -data[:,1]
	part_Pressure = data[:,2]
	part_Speed = data[:,3]
        k = 154
        print part_Cumulative[k],part_TS[k],part_Pressure[k],part_Speed[k]
        #Normalization:
        for data in ("part_Cumulative","part_TS","part_Pressure","part_Speed"):
            data_normalizing(eval(data))
            pass
        cheat_spec.append(part_Cumulative+part_TS+part_Pressure+part_Speed)
        value_plot(part_Cumulative,part_TS,part_Pressure,part_Speed,txtname.split('.')[0].split('_')[-1])
        #correlation_plot(part_Cumulative,part_TS,part_Pressure,part_Speed);plt.show()
        plt.plot([154,154],[-10,10])#all 4
        plt.plot([89,89],[-10,10])#without kongrey
        plt.show()
    cheat_spec = np.array(cheat_spec).sum(axis=0)
    print "Min index over cases:",cheat_spec.argmin(),',',cheat_spec[cheat_spec.argmin()]



	#print "Weighted objective value:",part_Cumulative,part_TS,part_Pressure,part_Speed
	#embed()
