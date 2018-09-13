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
  x3=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.622]
  y30=[139.164,139.396,139.648,139.906,140.249,140.671,141.245,141.992,142.975,144.399,146.633,150.847,164.528,1000]
  x4=[0.0025,0.005,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5]
  y40=[180.465,180.732,181.041,181.353,181.76,182.303,183.082,184.25,186.31,191.783,1000]
  x5=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.86]
  y50=[141.479,141.608,141.717,141.837,141.966,142.114,142.301,142.515,142.755,143.053,143.406,143.845,144.4,145.147,146.21,147.887,151.173,161.982,1000]
  x6=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55]
  y60=[252.714,252.873,253.203,253.626,254.063,254.667,255.457,256.562,258.35,261.78,275.957,1000]
  x7=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.86]
  y70=[178.156,178.358,178.556,178.757,178.99,179.264,179.603,179.991,180.482,181.077,181.804,182.733,183.934,185.586,188.004,191.967,200.416,253.892,1000]

  fig, ax = plt.subplots()
  l1 = ax.plot(x3, y30, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF$');
  l2 = ax.plot(x4, y40, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF$');
  l3 = ax.plot(x5, y50, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$');
  l4 = ax.plot(x6, y60, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$');
  l5 = ax.plot(x7, y70, marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .9)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(100, 500)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("layouts_a.pdf")

  # subfigure b
  x32=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.405]
  y32=[190.557,190.821,191.054,191.39,191.977,193.53,219.942,237.789,605.416,1000]
  x42=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.452]
  y42=[182.389,182.57,182.846,183.182,183.682,184.928,300.303,289.551,281.117,285.982,1000]
  x52=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.702]
  y52=[146.384,146.533,146.633,146.751,146.887,147.049,147.233,147.461,147.723,148.047,148.453,148.977,149.721,151.102,179.201,1000]
  x62=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.405]
  y62=[260.184,260.584,261.037,261.622,262.363,263.399,265.149,269.435,361.361,1000]
  x72=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.855]
  y72=[179.237,179.497,179.712,179.916,180.155,180.445,180.793,181.207,181.744,182.455,185.866,252.855,253.514,251.492,250.199,251.101,257.451,320.703,1000]

  fig, ax = plt.subplots()
  l1 = ax.plot(x32, y32, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF$');
  l2 = ax.plot(x42, y42, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF$');
  l3 = ax.plot(x52, y52, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$');
  l4 = ax.plot(x62, y62, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$');
  l5 = ax.plot(x72, y72, marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .9)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(100, 800)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("layouts_b.pdf")

  # subfigure c
  x31=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.605]
  y31=[147.915,148.352,149.048,149.773,150.744,152.09,153.789,155.949,158.826,162.48,167.49,231.753,817.782,1000]
  x41=[0.0025,0.049,0.1,0.15,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.605]
  y41=[180.713,180.989,181.822,184.106,299.703,296.306,285.352,277.529,272.109,268.537,267.054,268.853,1000]
  x51=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,0.955]
  y51=[143.575,143.876,144.269,144.732,145.195,145.733,146.357,147.101,147.952,149.052,150.376,152.046,154.018,156.594,159.713,163.96,170.188,180.577,200.125,252.356,1000]
  x61=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.505]
  y61=[244.328,244.606,245.31,246.461,247.691,249.368,251.673,254.995,260.625,271.961,304.722,1000]
  x71=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.905]
  y71=[176.494,177.072,177.648,178.296,179.228,181.575,210.35,266.923,266.488,262.067,258.195,255.34,253.362,252.475,252.748,254.662,259.255,268.344,286.808,1000]

  fig, ax = plt.subplots()
  l1 = ax.plot(x31, y31, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF$');
  l2 = ax.plot(x41, y41, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF$');
  l3 = ax.plot(x51, y51, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$');
  l4 = ax.plot(x61, y61, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$');
  l5 = ax.plot(x71, y71, marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, 1)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(100, 500)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("layouts_c.pdf")

if __name__ == '__main__':
  run()
