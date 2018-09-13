#! python3

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def run():
  markers = ['o', '*', '+', 'x', '^', 'v', '<', '>']
  markersize = 10
  markerfacecolor = 'auto'
  markeredgewidth = 1

  x1=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,]
  y10=[13.6783,13.8334,13.9854,14.1695,14.3944,14.6687,14.9992,15.4021,15.9089,16.5597,17.4304,18.681,20.6929,25.0711,68.0974,200]
  x2=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.88]
  y20=[13.7299,13.8371,13.9442,14.0568,14.1909,14.3455,14.5271,14.7387,14.9861,15.2812,15.6382,16.0766,16.6324,17.3773,18.4378,20.1185,23.4022,34.4914,304.131
  ]
  x3=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9]
  y30=[17.1127,17.2983,17.4976,17.7006,17.9319,18.2093,18.543,18.9403,19.4257,20.0612,20.7452,21.6718,22.8779,24.5263,26.9273,30.9027,39.3651,88.446,200
  ]
  x4=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,]
  y40=[17.1368,17.4002,17.6794,17.9924,18.3989,18.9472,19.7178,20.8865,22.9454,28.3633,314.06]
  x5=[0.0025,0.05,0.1,0.15,]
  y50=[20.7328,21.902,28.2844,200]
  x6=[0.0025,0.05,0.1,0.15,0.2,]
  y60=[21.0092,21.6291,22.7589,26.0881,200
  ]
  x7=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55]
  y70=[23.4271,23.6997,24.0475,24.4432,24.9134,25.5096,26.2988,27.424,29.1849,32.6228,46.8716,200]
  x8=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5]
  y80=[23.1059,23.3982,23.7371,24.1119,24.5575,25.1249,25.8851,26.9768,28.7555,33.0264,257.037]

  # gf ur a
  fig, ax = plt.subplots()
  l2 = ax.plot(x1, y10, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(11,29,1,10,24)$')
  l3 = ax.plot(x2, y20, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .9)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 100)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gf_ur_a.pdf")
  # gf ur b
  fig, ax = plt.subplots()
  l2 = ax.plot(x3, y30, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$')
  l3 = ax.plot(x4, y40, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(56,1,11,5,5)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .9)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 100)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gf_ur_b.pdf")
  # gf ur c
  fig, ax = plt.subplots()
  l2 = ax.plot(x5, y50, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(11,29,2,5,12)$')
  l3 = ax.plot(x6, y60, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,37,2,3,16)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .2)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 100)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gf_ur_c.pdf")
  # gf ur d
  fig, ax = plt.subplots()
  l2 = ax.plot(x7, y70, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$')
  l3 = ax.plot(x8, y80, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(11,37,4,2,7)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .6)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 100)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gf_ur_d.pdf")

  x1=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5]
  y10=[13.8639,14.0341,14.2068,14.4186,14.6896,15.0323,15.4865,16.1348,17.3615,32.1529,200]
  x2=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,]
  y20=[13.8662,13.9795,14.0906,14.2109,14.351,14.5183,14.7131,14.9438,15.2204,15.5537,15.971,17.2858,18.7111,54.4441,200]
  x3=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85]
  y30=[17.2059,17.3968,17.5991,17.8065,18.0435,18.3282,18.678,19.101,19.6278,20.3395,22.7775,92.2278,101.86,101.658,99.3058,97.8457,100.842,339.963]
  x4=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,]
  y40=[17.2866,17.5461,17.8353,18.1752,18.6497,19.8966,200]
  x5=[0.0025,0.05,0.1,]
  y50=[21.559,23.3616,200]
  x6=[0.0025,0.05,0.1,0.15,]
  y60=[21.6409,22.469,24.5054,200]
  x7=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,]
  y70=[23.7875,24.124,24.5961,25.1602,25.9025,26.9651,28.7174,33.0093,451]
  x8=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35]
  y80=[23.7884,24.1363,24.6073,25.2043,26.0107,27.2852,30.1803,378.19]

  # gf w a
  fig, ax = plt.subplots()
  l2 = ax.plot(x1, y10, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(11,29,1,10,24)$')
  l3 = ax.plot(x2, y20, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .9)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 100)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gf_w_a.pdf")
  # gf w b
  fig, ax = plt.subplots()
  l2 = ax.plot(x3, y30, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$')
  l3 = ax.plot(x4, y40, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(56,1,11,5,5)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .6)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 80)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gf_w_b.pdf")
  # gf w c
  fig, ax = plt.subplots()
  l2 = ax.plot(x5, y50, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(11,29,2,5,12)$')
  l3 = ax.plot(x6, y60, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,37,2,3,16)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .13)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 80)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gf_w_c.pdf")
  # gf w d
  fig, ax = plt.subplots()
  l2 = ax.plot(x7, y70, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$')
  l3 = ax.plot(x8, y80, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(11,37,4,2,7)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .48)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 80)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gf_w_d.pdf")
  

if __name__ == '__main__':
  run()
