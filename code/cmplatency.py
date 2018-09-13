#! python3

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def run():
  markers = ['o', '*', '+', 'x', '^', 'v', '<', '>']
  markersize = 10
  markerfacecolor = 'auto'
  markeredgewidth = 1

  x1=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,]
  y10=[21.4452,21.7883,22.1203,22.5048,22.9778,23.5639,24.3085,25.2868,26.6447,28.7155,32.4159,41.8714,253.145]
  x2=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85]
  y20=[16.5032,16.6813,16.8504,17.0288,17.2394,17.4877,17.78,18.125,18.5392,19.0444,19.6794,20.4997,21.6286,23.3131,26.2114,32.8567,75.5739,732.731]
  x3=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65]
  y30=[13.7618,13.9679,14.182,14.4509,14.7945,15.2334,15.7938,16.5298,17.5238,18.9493,21.198,25.4232,39.0219,200,]
  x4=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,]
  y40=[17.1368,17.4002,17.6794,17.9924,18.3989,18.9472,19.7178,20.8865,22.9454,28.3633,314.06]
  x5=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.88]
  y50=[13.7299,13.8371,13.9442,14.0568,14.1909,14.3455,14.5271,14.7387,14.9861,15.2812,15.6382,16.0766,16.6324,17.3773,18.4378,20.1185,23.4022,34.4914,304.131]
  x6=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55]
  y60=[23.4271,23.6997,24.0475,24.4432,24.9134,25.5096,26.2988,27.424,29.1849,32.6228,46.8716,200]
  x7=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9]
  y70=[17.1127,17.2983,17.4976,17.7006,17.9319,18.2093,18.543,18.9403,19.4257,20.0612,20.7452,21.6718,22.8779,24.5263,26.9273,30.9027,39.3651,88.446,200
  ]
  x51=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,]
  y510=[13.6783,13.8334,13.9854,14.1695,14.3944,14.6687,14.9992,15.4021,15.9089,16.5597,17.4304,18.681,20.6929,25.0711,68.0974,200]

  # gfft a
  fig, ax = plt.subplots()
  l2 = ax.plot(x5, y50, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$')
  l3 = ax.plot(x6, y60, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$')
  l4 = ax.plot(x7, y70, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$')
  l1 = ax.plot(x1, y10, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$FT$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .9)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 80)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gfft_a.pdf")

  # gffb a
  fig, ax = plt.subplots()
  l2 = ax.plot(x5, y50, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$')
  l3 = ax.plot(x6, y60, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$')
  l4 = ax.plot(x7, y70, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$')
  l1 = ax.plot(x2, y20, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$FB$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .9)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 80)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gffb_a.pdf")

  # gfsfdf a
  fig, ax = plt.subplots()
  l2 = ax.plot(x5, y50, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$')
  l3 = ax.plot(x6, y60, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$')
  l4 = ax.plot(x7, y70, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$')
  l5 = ax.plot(x51, y510, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(11,29,1,10,24)$')
  l1 = ax.plot(x3, y30, marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF$')
  l0 = ax.plot(x4, y40, marker=markers[5], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .9)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 80)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gfsfdf_a.pdf")
  
  x1=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,]
  y10=[22.0091,22.2473,22.4884,22.7797,23.1552,23.623,24.2228,25.0149,26.1151,27.8577,31.1947,42.3136,415.703]
  x2=[0.0025,0.05,0.1,0.15,0.2,]
  y20=[17.2617,20.495,22.146,27.1248,200]
  x3=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,]
  y30=[14.0088,14.2207,14.4507,14.7907,15.3695,16.9173,80.3925,81.555,141.581,]
  x4=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,]
  y40=[17.2866,17.5461,17.8353,18.1752,18.6497,19.8966,200]
  x5=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,]
  y50=[13.8662,13.9795,14.0906,14.2109,14.351,14.5183,14.7131,14.9438,15.2204,15.5537,15.971,17.2858,18.7111,54.4441,200]
  x6=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,]
  y60=[23.7875,24.124,24.5961,25.1602,25.9025,26.9651,28.7174,33.0093,451
  ]
  x7=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85]
  y70=[17.2059,17.3968,17.5991,17.8065,18.0435,18.3282,18.678,19.101,19.6278,20.3395,22.7775,92.2278,101.86,101.658,99.3058,97.8457,100.842,339.963]
  x51=[0.0025,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,];
  y510=[13.8639,14.0341,14.2068,14.4186,14.6896,15.0323,15.4865,16.1348,17.3615,32.1529,200];

  # gfft b
  fig, ax = plt.subplots()
  l2 = ax.plot(x5, y50, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$')
  l3 = ax.plot(x6, y60, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$')
  l4 = ax.plot(x7, y70, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$')
  l1 = ax.plot(x1, y10, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$FT$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .7)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 80)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gfft_b.pdf")

  # gffb b
  fig, ax = plt.subplots()
  l2 = ax.plot(x5, y50, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$')
  l3 = ax.plot(x6, y60, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$')
  l4 = ax.plot(x7, y70, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$')
  l1 = ax.plot(x2, y20, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$FB$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .7)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 80)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gffb_b.pdf")
  
  # gfsfdf b
  fig, ax = plt.subplots()
  l2 = ax.plot(x5, y50, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,1,7,28)$')
  l3 = ax.plot(x6, y60, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(15,29,4,2,7)$')
  l4 = ax.plot(x7, y70, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(81,1,10,4,8)$')
  l5 = ax.plot(x51, y510, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(11,29,1,10,24)$')
  l1 = ax.plot(x3, y30, marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF$')
  l0 = ax.plot(x4, y40, marker=markers[5], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .7)
  ax.set_xlabel('Offered Load', fontsize=24, weight='normal')
  ax.set_ylim(0, 80)
  ax.set_ylabel('Latency (cycles)', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("gfsfdf_b.pdf")

if __name__ == '__main__':
  run()
