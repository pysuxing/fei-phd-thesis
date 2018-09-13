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
  lq1=[0, 0.2, 0.4, 0.7, 0.75, 0.8, 0.85];
  aq1=[1.888, 2.1499, 2.4077, 3.0458, 3.2764, 3.6363, 30];
  lq2=[0, 0.2, 0.4, 0.6, 0.8, 0.85, 0.9];
  aq2=[1.9289, 2.2535, 2.5131, 2.7897, 3.4772, 3.9963, 30];
  lq3=[0, 0.2, 0.4, 0.6, 0.8, 0.85, 0.9];
  aq3=[1.9416, 2.2589, 2.5165, 2.7574, 3.3757, 3.74, 30];
  lq4=[0, 0.2, 0.4, 0.6, 0.8, 0.85, 0.88, 0.9];
  aq4=[1.9668, 2.3058, 2.5763, 2.7901, 3.315, 3.5942, 3.8666, 30];

  ls1=[0, 0.2, 0.4, 0.6, 0.62, 0.65];
  as1=[1.9295, 2.2506, 2.5626, 3.0245, 3.1863, 30];
  ls2=[0, 0.2, 0.4, 0.6, 0.65, 0.7];
  as2=[1.9567, 2.3211, 2.6078, 2.971, 3.1565, 30];
  ls3=[0, 0.2, 0.4, 0.6, 0.7, 0.75, 0.8, 0.85];
  as3=[1.9669, 2.3117, 2.5976, 2.8947, 3.2314, 3.4591, 3.8294, 30];
  ls4=[0, 0.15, 0.3, 0.45, 0.6, 0.7, 0.8, 0.85, 0.9];
  as4=[1.9799, 2.2583, 2.4878, 2.6861, 2.853, 3.0981, 3.5798, 4.0096, 30];

  fig, ax = plt.subplots()
  l1 = ax.plot(lq1, aq1, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 0.2K$');
  l2 = ax.plot(lq2, aq2, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 0.5K$');
  l3 = ax.plot(lq3, aq3, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 1.0K$');
  l4 = ax.plot(lq4, aq4, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 2.0K$');
  l1 = ax.plot(ls1, as1, marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF\ 0.2K$');
  l2 = ax.plot(ls2, as2, marker=markers[5], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF\ 0.5K$');
  l3 = ax.plot(ls3, as3, marker=markers[6], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF\ 1.0K$');
  l4 = ax.plot(ls4, as4, marker=markers[7], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF\ 2.0K$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, 1)
  ax.set_xlabel('Link Failure Ratio', fontsize=24, weight='normal')
  ax.set_ylim(0, 12)
  ax.set_ylabel('Average Path Length', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("resiliency_a.pdf")

  # subfigure b
  lq1=[0, 0.2, 0.4, 0.7, 0.75, 0.8, 0.85];
  aq1=[2, 4, 4, 5, 6, 8, 30];
  lq2=[0, 0.2, 0.4, 0.6, 0.8, 0.85, 0.9];
  aq2=[2, 4, 4, 4, 6, 7, 30];
  lq3=[0, 0.2, 0.4, 0.6, 0.8, 0.85, 0.9];
  aq3=[2, 4, 4, 4, 6, 6, 30];
  lq4=[0, 0.2, 0.4, 0.6, 0.8, 0.85, 0.88, 0.9];
  aq4=[2, 3, 4, 4, 5, 6, 8, 30];

  ls1=[0, 0.2, 0.4, 0.6, 0.62, 0.65];
  as1=[2, 4, 4, 6, 6, 30];
  ls2=[0, 0.2, 0.4, 0.6, 0.65, 0.7];
  as2=[2, 4, 4, 5, 5, 30];
  ls3=[0, 0.2, 0.4, 0.6, 0.7, 0.75, 0.8, 0.85];
  as3=[2, 4, 4, 4, 5, 6, 7, 30];
  ls4=[0, 0.15, 0.3, 0.45, 0.6, 0.7, 0.8, 0.85, 0.9];
  as4=[2, 4, 4, 4, 4, 5, 6, 7, 30];

  fig, ax = plt.subplots()
  l1 = ax.plot(lq1, aq1, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 0.2K$');
  l2 = ax.plot(lq2, aq2, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 0.5K$');
  l3 = ax.plot(lq3, aq3, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 1.0K$');
  l4 = ax.plot(lq4, aq4, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 2.0K$');
  l1 = ax.plot(ls1, as1, marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF\ 0.2K$');
  l2 = ax.plot(ls2, as2, marker=markers[5], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF\ 0.5K$');
  l3 = ax.plot(ls3, as3, marker=markers[6], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF\ 1.0K$');
  l4 = ax.plot(ls4, as4, marker=markers[7], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF\ 2.0K$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, 1)
  ax.set_xlabel('Link Failure Ratio', fontsize=24, weight='normal')
  ax.set_ylim(0, 20)
  ax.set_ylabel('Diameter', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("resiliency_b.pdf")

  # subfigure c
  lq1=[0, 0.2, 0.4, 0.45, 0.5];
  aq1=[3.4727, 3.8996, 4.6244, 4.9635, 30];
  lq2=[0, 0.2, 0.4, 0.5, 0.52];
  aq2=[3.8412, 4.3304, 5.102, 5.6845, 30];
  lq3=[0, 0.2, 0.4, 0.45, 0.5, 0.55, 0.6];
  aq3=[3.8516, 4.2496, 4.8495, 5.0275, 5.2521, 5.6478, 30];
  lq4=[0, 0.15, 0.3, 0.35, 0.45, 0.5, 0.6, 0.62];
  aq4=[4.0249, 4.3631, 4.7579, 4.902, 5.2243, 5.4472, 6.0733, 30];

  ls1=[0, 0.2, 0.4, 0.5, 0.55, 0.6];
  as1=[2.6937, 3.1086, 3.5949, 3.9111, 4.1705, 30];
  ls2=[0, 0.2, 0.4, 0.5, 0.55, 0.6, 0.65];
  as2=[2.7612, 3.1867, 3.616, 3.8879, 4.0779, 4.3894, 30];
  ls3=[0, 0.2, 0.4, 0.5, 0.6, 0.65, 0.7];
  as3=[2.8357, 3.2759, 3.6611, 3.9244, 4.2745, 4.533, 30];
  ls4=[0, 0.2, 0.4, 0.6, 0.65, 0.7];
  as4=[2.8582, 3.2986, 3.6789, 4.2521, 4.4964, 30];

  fig, ax = plt.subplots()
  l1 = ax.plot(lq1, aq1, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 0.2K$');
  l2 = ax.plot(lq2, aq2, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 0.5K$');
  l3 = ax.plot(lq3, aq3, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 1.0K$');
  l4 = ax.plot(lq4, aq4, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 2.0K$');
  l1 = ax.plot(ls1, as1, marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF\ 0.2K$');
  l2 = ax.plot(ls2, as2, marker=markers[5], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF\ 0.5K$');
  l3 = ax.plot(ls3, as3, marker=markers[6], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF\ 1.0K$');
  l4 = ax.plot(ls4, as4, marker=markers[7], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF\ 2.0K$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .7)
  ax.set_xlabel('Link Failure Ratio', fontsize=24, weight='normal')
  ax.set_ylim(0, 20)
  ax.set_ylabel('Average Path Length', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("resiliency_c.pdf")

  # subfigure d
  lq1=[0, 0.2, 0.4, 0.45, 0.5];
  aq1=[5, 7, 9, 10, 38];
  lq2=[0, 0.2, 0.4, 0.5, 0.52, ];
  aq2=[5, 8, 10, 12, 38];
  lq3=[0, 0.2, 0.4, 0.45, 0.5, 0.55, 0.6];
  aq3=[5, 7, 8, 9, 9, 11, 38];
  lq4=[0, 0.15, 0.3, 0.35, 0.45, 0.5, 0.6, 0.62];
  aq4=[5, 7, 8, 8, 9, 9, 11, 38];

  ls1=[0, 0.2, 0.4, 0.5, 0.55, 0.6];
  as1=[3, 5, 6, 7, 9, 38];
  ls2=[0, 0.2, 0.4, 0.5, 0.55, 0.6, 0.65];
  as2=[3, 5, 6, 7, 7, 9, 38];
  ls3=[0, 0.2, 0.4, 0.5, 0.6, 0.65, 0.7];
  as3=[3, 5, 6, 6, 7, 8, 38];
  ls4=[0, 0.2, 0.4, 0.6, 0.65, 0.7];
  as4=[3, 5, 6, 7, 8, 38];

  fig, ax = plt.subplots()
  l1 = ax.plot(lq1, aq1, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 0.2K$');
  l2 = ax.plot(lq2, aq2, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 0.5K$');
  l3 = ax.plot(lq3, aq3, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 1.0K$');
  l4 = ax.plot(lq4, aq4, marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF\ 2.0K$');
  l1 = ax.plot(ls1, as1, marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF\ 0.2K$');
  l2 = ax.plot(ls2, as2, marker=markers[5], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF\ 0.5K$');
  l3 = ax.plot(ls3, as3, marker=markers[6], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF\ 1.0K$');
  l4 = ax.plot(ls4, as4, marker=markers[7], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF\ 2.0K$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, .7)
  ax.set_xlabel('Link Failure Ratio', fontsize=24, weight='normal')
  ax.set_ylim(0, 35)
  ax.set_ylabel('Diameter', fontsize=24, weight='normal')
  # ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.tick_params(labelsize=20)
  ax.legend(loc='upper left', fontsize=16, ncol=1)
  fig.savefig("resiliency_d.pdf")




if __name__ == '__main__':
  run()

