#! python3

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

trans = True

def run():
  r = 48
  ps = np.arange(1, r+1, dtype=int)
  markers = ['o', '*', '+', 'x', '^', 'v', '<', '>']
  markersize = 10
  rxticks = np.arange(0, r+1, 8)

  # subfigure cables
  k1=np.array([0.5,1,2,3,4,5,6,7])
  p1=np.array([57,64,73,84,95,119,149,159])./40
  k2=np.array([3,5,10,15,20,30,50,100,200,300])
  p2=np.array([379,379,399,419,439,499,609,919,1429,2095])./40

  fig, ax = plt.subplots()
  ax.plot(Ksf4, Nsf4, marker=markers[0], markersize=markersize, label='$SF$')
  ax.plot(K14, N14, marker=markers[1], markersize=markersize, label='$GF(n=q)$')
  ax.plot(K24, N24, marker=markers[2], markersize=markersize, label='$GF(n=2q)$')
  ax.plot(K34, N34, marker=markers[3], markersize=markersize, label='$GF(n=q/2)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, 50)
  ax.set_xlabel('Router Radix ($r$)', fontsize=24, weight='normal')
  ax.set_ylim(0, 12000)
  ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
  ax.set_xticks(rxticks)
  ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  ax.tick_params(labelsize=20)
  ax.yaxis.get_offset_text().set_fontsize(20)
  ax.legend(loc='upper left')
  fig.savefig("bbw_sf_a.pdf")

