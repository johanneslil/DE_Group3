# import plotting
import matplotlib.pyplot as plt
import numpy as np

# Plotting for scalability study 

# Data
nr_cores = [1, 2, 4, 8]
tot_time = [300.4680299758911, 156.14600825309753, 88.36659026145935, 58.15558362007141]
read_data_time = [59.46717834472656, 36.48017764091492, 20.34749412536621, 10.628390789031982]
computation_time = [120.48841381072998, 63.47409105300903, 33.38731050491333, 22.95405149459839]
plot_time = [120.51239657402039, 56.19168996810913, 34.63174867630005, 24.573099851608276]

# 1. Plot the speedup for different number of cores
times = {
    'Read data time': read_data_time,
    'Computation time': computation_time,
    'Plot time': plot_time
}

fig, ax = plt.subplots()
ax.stackplot(nr_cores, times.values(),
           labels=times.keys(), alpha=0.8)
ax.legend(loc='upper right')
ax.set_title('Total processing time for different number of spark cores')
ax.set_xlabel('Number of cores')
ax.set_ylabel('Time (s)')

plt.show()

# 2. Plot the speedup for different number of nodes
ideal_time = []
ideal_cores = np.linspace(1, 8, 1000)
for i in ideal_cores:
    ideal_time.append(tot_time[0] / i)
    

fig2, ax2 = plt.subplots()
ax2.plot(nr_cores, tot_time,  label='Total time', linestyle="solid")
ax2.plot(ideal_cores, ideal_time, label='Ideal speedup time', linestyle="dashed")
ax2.legend(loc='upper right')
ax2.set_title('Total processing time for different number of spark cores')
ax2.set_xlabel('Number of cores')
ax2.set_ylabel('Time (s)')

plt.show()

