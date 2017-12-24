import numpy as np
import matplotlib.pyplot as plt
import os,sys,time
from IPython import embed 
def darken(data):
	data = data*1.2
	return data
def whiten(data):
	data = data*0.8
	return data
def block_data(txtname):
	data = np.loadtxt(txtname,delimiter=',')
	dark_list = [(-4,9),(-4,8),(-2,3),(-2,8),(-2,3),(-2,3),(-2,11),(-2,11),(-2,11),(-2,11),(-2,7),(-2,8),(-2,8),(-2,8),(-2,8),(-2,8),(-2,8),(-2,8),(-2,3),(-2,17),(-2,3),(-2,3),(-3,3)]
	whiten_list = [(-4,3),(-3,17),(-4,8),(-3,17),(-3,16),(-3,6),(-3,7),(-4,6)]
	for pair in dark_list:
		i,j = pair[0],pair[1]
		data[i,j] = darken(data[i,j])
	for pair in whiten_list:
		i,j = pair[0],pair[1]
		data[i,j] = whiten(data[i,j])

	data[-1,:] = (data[-2,:]+data[-3,:]+data[-4,:])/3.0
	return data[-4:,:]#data[0:4,:]


if __name__ == "__main__":
	print "SA_blocks...."
	txtname = 'Array_for_matlab_MARS.txt'
	labels_on_x = "XKA CZO pd pe ph TIMEC TKEMAX Ice_stokes_fac N0r dimax peaut CSSCA SECANG beta_P brcr_sbrob brcr_sb pfac bfac sm DSATDK DMAXSMC DSATPSI DBB".split()
	labels_on_y = "Rainfall_related Pressure_related Windspeed_related Weighted_score".split()
	data = block_data(txtname)
	plt.imshow(data,cmap="Greys")

	plt.xticks(np.arange(0.0,23.0,1.0),labels_on_x,rotation=-68,fontsize=10)
	plt.yticks(np.arange(0.0,4.0,1.0),labels_on_y,rotation=0,fontsize=8)
	plt.colorbar(shrink=0.4)
#	plt.grid(xdata=range(23),ydata=range(5),color='k',linewidth=1)
	rank = data[-1,:].argsort()[::-1]
	for index,i in enumerate(rank):
		if index<8:
			plt.text(i-0.3,2.7,"rank:%s"%int(index+1),color='red',fontsize=8,rotation=-76)
			print index,i
		else:
			pass

	plt.title("Evaluated sensitivity of objectives",fontsize=12)
#	plt.xlim(-0.5,22.5)
	plt.show()
