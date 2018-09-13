#! python3

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def run():
  markers = ['o', '*', '+', 'x', '^', 'v', '<', '>']
  markersize = 10
  markerfacecolor = 'auto'
  markeredgewidth = 1

  # subfigure a
  x60=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.405]
  y60=[244.145,244.413,245.328,246.351,247.684,249.338,251.692,254.928,264.17,1000]
  x61=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.405,]
  y61=[244.131,244.625,245.466,246.564,247.787,249.495,251.701,255.125,262.242,1000]
  x62=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.455,]
  y62=[244.328,244.449,245.37,246.412,247.72,249.389,251.645,254.992,260.644,272.29,1000]
  x63=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.505]
  y63=[244.328,244.606,245.31,246.461,247.691,249.368,251.673,254.995,260.625,271.961,304.722,1000]

  fig, ax = plt.subplots()
  l1 = ax.plot(x60, y60, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$MIN$')
  l2 = ax.plot(x61, y61, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$NAR$')
  l3 = ax.plot(x62, y62, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$NAL$')
  l4 = ax.plot(x63, y63, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$NAG$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .6)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(100, 600)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("routingalgos_a.pdf")

  # subfigure b
  x50=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,]
  y50=[143.767,143.909,144.311,144.698,145.147,145.73,146.341,147.092,147.944,149.069,150.752,182.49,888.998]
  x51=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,0.955]
  y51=[143.575,143.876,144.269,144.732,145.195,145.733,146.357,147.101,147.952,149.052,150.376,152.046,154.018,156.594,159.713,163.96,170.188,180.577,200.125,252.356,1000]
  x60=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.405]
  y60=[244.145,244.413,245.328,246.351,247.684,249.338,251.692,254.928,264.17,1000]
  x61=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.505]
  y61=[244.328,244.606,245.31,246.461,247.691,249.368,251.673,254.995,260.625,271.961,304.722,1000]
  x70=[0.0025,0.049,0.1,0.15,0.2,0.25,0.255]
  y70=[176.48,177.028,177.631,178.273,179.256,181.641,1000]
  x71=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.905]
  y71=[176.494,177.072,177.648,178.296,179.228,181.575,210.35,266.923,266.488,262.067,258.195,255.34,253.362,252.475,252.748,254.662,259.255,268.344,286.808,1000]

  fig, ax = plt.subplots()
  l1 = ax.plot(x50, y50, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)\ MIN$')
  l2 = ax.plot(x51, y51, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)\ NAG$')
  l3 = ax.plot(x60, y60, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)\ MIN$')
  l4 = ax.plot(x61, y61, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)\ NAG$')
  l5 = ax.plot(x70, y70, marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)\ MIN$')
  l6 = ax.plot(x71, y71, marker=markers[5], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)\ NAG$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, 1)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(100, 850)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("routingalgos_b.pdf")

if __name__ == '__main__':
  run()
