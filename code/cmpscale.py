#! python3

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def run():
  r = 48
  ps = np.arange(1, r+1, dtype=int)
  markers = ['o', '*', '+', 'x', '^', 'v', '<', '>']
  markersize = 10
  markerfacecolor = 'auto'
  markeredgewidth = 1
  xticks = np.arange(0, r+1, 8)
  n0 = np.power(((r - ps) / 3 + 1), 3) * ps # FB
  n1=2*np.power(((2*(r-ps)+1)/3),2)*ps; # SF
  n2=((2*(r+1-ps)/3)*((r+1-ps)/3)+1)*(2*(r+1-ps)/3)*ps; # DF
  n3=2*np.power((r/2),2)*ps;                            # FT
  n4=np.power(((4*(r+1-2-ps)/3)+1),2)*2*ps;             # GF
  n5=np.power(((6*(r+1-3-ps)/3)+1),2)*3*ps;             # GF
  ub = max(n0.max(), n1.max(), n2.max(), n3.max(), n4.max(), n5.max(), )
  fig, ax = plt.subplots()
  l0 = ax.plot(ps, n0, marker=markers[0], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$FB$');
  l1 = ax.plot(ps, n1, marker=markers[1], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$SF$');
  l2 = ax.plot(ps, n2, marker=markers[2], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$DF$');
  l3 = ax.plot(ps[:len(ps)//2], n3[:len(ps)//2], marker=markers[3], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$FT$')
  l4 = ax.plot(ps[:-1], n4[:-1], marker=markers[4], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(n\!\!>\!\!1,q\!\!=\!\!n,a\!\!=\!\!2,p,h)$')
  l5 = ax.plot(ps[:-2], n5[:-2], marker=markers[5], markersize=markersize,
               markerfacecolor=markerfacecolor, markeredgewidth=markeredgewidth,
               label='$GF(n\!\!>\!\!1,q\!\!=\!\!n,a\!\!=\!\!3,p,h)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, r+8)
  ax.set_xlabel('Terminals/Router ($p$)', fontsize=24, weight='normal')
  ax.set_ylim(0, ub*1.2)
  ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
  ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  ax.tick_params(labelsize=20)
  ax.yaxis.get_offset_text().set_fontsize(20);
  ax.legend(fontsize=16, ncol=1)
  fig.savefig("cmpscale.pdf")

if __name__ == '__main__':
  run()
