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
  x3=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.755]
  y30=[142.676,143.621,144.194,144.748,145.492,146.262,147.241,148.311,149.685,151.244,153.281,155.852,159.041,163.406,169.673,179.906,1000]
  x4=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.855]
  y40=[184.498,184.994,185.57,186.164,187.015,187.948,188.916,190.091,191.466,193.117,195.093,197.513,200.534,204.428,209.55,216.644,227.254,245.453,1000]
  x15=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.86]
  y150=[141.479,141.608,141.717,141.837,141.966,142.114,142.301,142.515,142.755,143.053,143.406,143.845,144.4,145.147,146.21,147.887,151.173,161.982,1000]
  x16=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55]
  y160=[252.714,252.873,253.203,253.626,254.063,254.667,255.457,256.562,258.35,261.78,275.957,1000]
  x17=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.86]
  y170=[178.156,178.358,178.556,178.757,178.99,179.264,179.603,179.991,180.482,181.077,181.804,182.733,183.934,185.586,188.004,191.967,200.416,253.892,1000]
  x5=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,0.955]
  y50=[145.428,145.86,146.212,146.62,147.081,147.576,148.177,148.799,149.565,150.451,151.462,152.711,154.231,156.153,158.616,161.99,166.929,174.942,190.649,237.103,1000]
  x6=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.505]
  y60=[256.793,257.321,258.157,259.184,260.544,262.458,265.02,268.727,275.123,289.186,361.911,1000]
  x7=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.955]
  y70=[182.381,182.686,183.078,183.619,184.267,184.924,185.723,186.605,187.661,188.837,190.215,191.908,193.911,196.454,199.661,204.012,210.098,219.593,236.952,1000]

  fig, ax = plt.subplots()
  ax.plot(x15, y150, marker=markers[0], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(15,29,1,7,28)\ len=1$');
  ax.plot(x16, y160, marker=markers[1], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(15,29,4,2,7)\ len=1$');
  ax.plot(x17, y170, marker=markers[2], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(81,1,10,4,8)\ len=1$');
  ax.plot(x5, y50, marker=markers[3], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(15,29,1,7,28)\ len=5$');
  ax.plot(x6, y60, marker=markers[4], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(15,29,4,2,7)\ len=5$');
  ax.plot(x7, y70, marker=markers[5], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(81,1,10,4,8)\ len=5$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, 1)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(100, 800)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("packets_a.pdf")

  # subfigure b
  x32=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.505]
  y32=[194.546,195.091,195.699,196.439,197.455,198.825,200.731,203.574,208.296,219.741,422.969,1000]
  x42=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.805]
  y42=[186.497,186.85,187.399,188.116,188.857,189.798,190.825,192.08,193.599,195.613,198.874,209.401,234.42,243.676,250.468,260.035,278.498,1000]
  x152=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.702]
  y152=[146.384,146.533,146.633,146.751,146.887,147.049,147.233,147.461,147.723,148.047,148.453,148.977,149.721,151.102,179.201,1000]
  x162=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.405]
  y162=[260.184,260.584,261.037,261.622,262.363,263.399,265.149,269.435,361.361,1000]
  x172=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.855]
  y172=[179.237,179.497,179.712,179.916,180.155,180.445,180.793,181.207,181.744,182.455,185.866,252.855,253.514,251.492,250.199,251.101,257.451,320.703,1000]
  x52=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,0.955]
  y52=[150.555,150.722,151.138,151.551,152.017,152.529,153.129,153.79,154.565,155.458,156.527,157.82,159.37,161.367,163.927,167.504,172.658,180.924,197.265,245.568,1000]
  x62=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.405]
  y62=[264.252,265.135,266.408,268.019,270.347,273.811,280.079,297.192,476.879,1000]
  x72=[0.0025,0.049,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,0.955]
  y72=[183.483,183.73,184.245,184.787,185.437,186.125,186.904,187.793,188.844,190.035,191.493,193.181,195.227,197.822,201.09,205.48,211.755,221.407,239.357,289.974,1000]

  fig, ax = plt.subplots()
  ax.plot(x152, y152, marker=markers[0], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(15,29,1,7,28)\ len=1$');
  ax.plot(x162, y162, marker=markers[1], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(15,29,4,2,7)\ len=1$');
  ax.plot(x172, y172, marker=markers[2], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(81,1,10,4,8)\ len=1$');
  ax.plot(x52, y52, marker=markers[3], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(15,29,1,7,28)\ len=5$');
  ax.plot(x62, y62, marker=markers[4], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(15,29,4,2,7)\ len=5$');
  ax.plot(x72, y72, marker=markers[5], markersize=markersize,
          markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
          label='$GF(81,1,10,4,8)\ len=5$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, 1)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(100, 950)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("packets_b.pdf")

if __name__ == '__main__':
  run()
