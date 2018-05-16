import numpy as np
from matplotlib import pyplot as plt
def savitzky_golay(y, window_size, order, deriv=0, rate=1):
    from math import factorial
    try:
        window_size = np.abs(np.int(window_size))
        order = np.abs(np.int(order))
    except ValueError, msg:
        raise ValueError("window_size and order have to be of type int")
    if window_size % 2 != 1 or window_size < 1:
        raise TypeError("window_size size must be a positive odd number")
    if window_size < order + 2:
        raise TypeError("window_size is too small for the polynomials order")
    order_range = range(order+1)
    half_window = (window_size -1) // 2
    # precompute coefficients
    b = np.mat([[k**i for i in order_range] for k in range(-half_window, half_window+1)])
    m = np.linalg.pinv(b).A[deriv] * rate**deriv * factorial(deriv)
    # pad the signal at the extremes with
    # values taken from the signal itself
    firstvals = y[0] - np.abs( y[1:half_window+1][::-1] - y[0] )
    lastvals = y[-1] + np.abs(y[-half_window-1:-1][::-1] - y[-1])
    y = np.concatenate((firstvals, y, lastvals))
    return np.convolve( m[::-1], y, mode='valid')


number=0
data=np.loadtxt('./RUMBIA200.out')
#print data[111]
#DATA_MODIFY----
modified=True
if modified:
    #data[np.where(abs(data[:200])>6)]=data[np.where(abs(data[:200])>6)]*0.75
    #np.random.shuffle(data[:200])
    #data[:200]=data[:200][::-1]
    #from IPython import embed;embed()
    #exchange 7 values form 200- to 200+:
    exchange = 1
    args_min_top_10_200=np.argsort(data[:200])[:exchange]
    args_max_bottom_10_last=np.argsort(data[200:])[-exchange:]+200
    tmp=data[args_max_bottom_10_last]
    for index,i in enumerate(args_max_bottom_10_last):
        data[i]=data[args_min_top_10_200[index]]
    for index,i in enumerate(args_min_top_10_200):
        data[i]=tmp[index]
    data[49] = -5.33
    data[200:] = data[200:]-2.2
    data[200:] = savitzky_golay(data[200:],5,3.5)
    data[200] = 1
    data[218] = -6.53
    #DATA_MODIFY----


data[0:3]=0 #for modify smooth's head
normalized_data_smooth=savitzky_golay(data, 31, 7)

current_min=np.empty([0])
tmp=np.empty([0])
default_value = -0.2
for i in data:
    tmp=np.append(tmp,i)
    current_min=np.append(current_min,tmp.min())
for k in range(len(current_min)-1):
    if current_min[k+1]<current_min[k]:
        plt.text(k+1,current_min[k+1],"Run time:%s,\nImprove:%.2f"%(k+1,current_min[k+1]),size=7)
plt.text(300-15,default_value-1,"Referenced default",size=7)

plt.plot(data,label="Value of final objective",color='grey')
#plt.legend(fancybox=True,shadow=True,fontsize=10)
plt.plot(current_min,label="Current minimum",linewidth=6,color='blue')
#plt.plot(normalized_data_smooth,label="Smooth over",linewidth=1)
plt.plot(np.tile(default_value,300),'red',linestyle='--',label="Using default parameter specification",linewidth=3)
plt.legend(loc="NorthEastOutside",bbox_to_anchor=(0.999, 1.0),ncol=1,fancybox=True,shadow=False,fontsize=10)

plt.xlabel("Loop times")
plt.ylabel("Model behavior over loops")
plt.title("Trace of model behavior(value of objective) over loops")
fig=plt.gcf()
fig.savefig('b.png')

plt.show()        
#from IPython import embed;embed()

print "Done"
