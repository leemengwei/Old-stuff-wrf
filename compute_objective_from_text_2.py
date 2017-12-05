import numpy as np
from IPython import embed
import matplotlib.pyplot as plt

def value_plot(part_TS,part_Pressure,part_Speed):
	plt.plot(part_TS,label="-TS")
	plt.plot(part_Speed,label="Speed")
	plt.plot(part_Pressure,label="Pressure")
	plt.plot((part_Pressure+part_TS+part_Speed),label="Total")
	plt.title("Normalized individual objective")
        plt.legend()
	plt.show()
def correlation_plot(part_TS,part_Pressure,part_Speed):
        plt.scatter(part_Pressure,part_TS,label='Pressure&TS: %s'%round(np.corrcoef(part_Pressure,part_TS)[0,1],3))
        plt.scatter(part_Speed,part_TS,label='Speed&TS: %s'%round(np.corrcoef(part_Speed,part_TS)[0,1],3))
        plt.scatter(part_Pressure,part_Speed,label='Pressure&Speed: %s'%round(np.corrcoef(part_Pressure,part_Speed)[0,1],3))
        plt.legend()
        plt.show()
def data_processing(part_TS,part_Pressure,part_Speed):
        part_TS = (part_TS-part_TS.mean())/part_TS.std()
        part_Pressure = (part_Pressure-part_Pressure.mean())/part_Pressure.std()
        part_Speed = (part_Speed-part_Speed.mean())/part_Speed.std()
        return part_TS,part_Pressure,part_Speed

if __name__ == "__main__":
	data = np.loadtxt('Error_all_200_sensible')
	part_TS = -data[:,2]   #We want TS higher.
	part_Pressure = data[:,0]
	part_Speed = data[:,1]
        #-------functions:
        part_TS,part_Pressure,part_Speed = data_processing(part_TS,part_Pressure,part_Speed)
        value_plot(part_TS,part_Pressure,part_Speed)
        #correlation_plot(part_TS,part_Pressure,part_Speed)


	print "Weighted objective value:",part_TS,part_Pressure,part_Speed
	#embed()
