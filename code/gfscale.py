#! python3

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def run():
  r = 48
  ps = np.arange(1, r+1, dtype=int)
  markers = ['o', '*', '+', 'x', '^', 'v', '<', '>']
  markersize = 10
  xticks = np.arange(0, r+1, 8)
  # subfigure a
  n = (r + 1 - ps) * ps
  fig, ax = plt.subplots()
  l = ax.plot(ps, n, marker=markers[0], markersize=markersize);
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, r)
  ax.set_xlabel('Terminals/Router ($p$)', fontsize=24, weight='normal')
  ax.set_ylim(0, n.max()*1.1)
  ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
  ax.set_xticks(xticks)
  # ax.set_xticklabels(xticks)
  ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  ax.tick_params(labelsize=20)
  ax.yaxis.get_offset_text().set_fontsize(20);
  fig.savefig("gfscale_a.pdf")
  # subfigure b
  n0 = np.power((2 * (r - ps) + 3) / 3, 2) * ps
  n1 = ((r - ps) / 2 + 1) * (r - ps + 1) * ps
  n2 = ((r - ps) / 3 + 1) * (4 * (r - ps) / 3 + 1) * ps
  ub = max(n0.max(), n1.max(), n2.max())
  fig, ax = plt.subplots()
  l0 = ax.plot(ps, n0, marker=markers[0], markersize=markersize, label='$n=q$');
  l1 = ax.plot(ps, n1, marker=markers[1], markersize=markersize, label='$n=q/2$');
  l2 = ax.plot(ps, n2, marker=markers[2], markersize=markersize, label='$n=q/4$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, r)
  ax.set_xlabel('Terminals/Router ($p$)', fontsize=24, weight='normal')
  ax.set_ylim(0, ub * 1.1)
  ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
  ax.set_xticks(xticks)
  ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  ax.tick_params(labelsize=20)
  ax.yaxis.get_offset_text().set_fontsize(20);
  ax.legend(fontsize=20);
  fig.savefig("gfscale_b.pdf")
  # subfigure c
  n0 = ((2 * (r + 1 - ps) / 3) * ((r + 1 - ps) / 3) + 1) * (2 * (r + 1 - ps) / 3) * ps
  n1 = (np.power(((r + 1 - ps) / 2), 2) + 1) * ((r + 1 - ps) / 2) * ps
  ub = max(n0.max(), n1.max())
  fig, ax = plt.subplots()
  l0 = ax.plot(ps, n0, marker=markers[0], markersize=markersize, label='$a=2h$');
  l1 = ax.plot(ps, n1, marker=markers[1], markersize=markersize, label='$a=h$');
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, r)
  ax.set_xlabel('Terminals/Router ($p$)', fontsize=24, weight='normal')
  ax.set_ylim(0, ub * 1.1)
  ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
  ax.set_xticks(xticks)
  ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  ax.tick_params(labelsize=20)
  ax.yaxis.get_offset_text().set_fontsize(20);
  ax.legend(fontsize=20);
  fig.savefig("gfscale_c.pdf")
  # subfigure d
  n0=np.power(((2*(2*(r+1-ps)/3)*((r+1-ps)/3)/3)+1),2)*(2*(r+1-ps)/3)*ps
  n1=np.power(((2*((r+1-ps)/2)*((r+1-ps)/2)/3)+1),2)*((r+1-ps)/2)*ps
  ub = max(n0.max(), n1.max())
  fig, ax = plt.subplots()
  l0 = ax.plot(ps, n0, marker=markers[0], markersize=markersize, label='$a=2h$')
  l1 = ax.plot(ps, n1, marker=markers[1], markersize=markersize, label='$a=h$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, r)
  ax.set_xlabel('Terminals/Router ($p$)', fontsize=24, weight='normal')
  ax.set_ylim(0, ub * 1.1)
  ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
  ax.set_xticks(xticks)
  ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  ax.tick_params(labelsize=20)
  ax.yaxis.get_offset_text().set_fontsize(20);
  ax.legend(fontsize=20);
  fig.savefig("gfscale_d.pdf")
  # subfigure e
  n0=np.power(((4*(r+1-2-ps)/3)+1),2)*2*ps;
  n1=np.power(((6*(r+1-3-ps)/3)+1),2)*3*ps;
  n2=np.power(((8*(r+1-4-ps)/3)+1),2)*4*ps;
  n3=np.power(((10*(r+1-5-ps)/3)+1),2)*5*ps;
  n4=np.power(((12*(r+1-6-ps)/3)+1),2)*6*ps;
  ub = max(n0.max(), n1.max(), n2.max(), n3.max(), n4.max())
  fig, ax = plt.subplots()
  l0 = ax.plot(ps[:-1], n0[:-1], marker=markers[0], markersize=markersize, label='$a=2$')
  l1 = ax.plot(ps[:-2], n1[:-2], marker=markers[1], markersize=markersize, label='$a=3$')
  l2 = ax.plot(ps[:-3], n2[:-3], marker=markers[2], markersize=markersize, label='$a=4$')
  l3 = ax.plot(ps[:-4], n3[:-4], marker=markers[3], markersize=markersize, label='$a=5$')
  l4 = ax.plot(ps[:-5], n4[:-5], marker=markers[4], markersize=markersize, label='$a=6$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, r)
  ax.set_xlabel('Terminals/Router ($p$)', fontsize=24, weight='normal')
  ax.set_ylim(0, ub * 1.1)
  ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
  ax.set_xticks(xticks)
  ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  ax.tick_params(labelsize=20)
  ax.yaxis.get_offset_text().set_fontsize(20);
  ax.legend(fontsize=20);
  fig.savefig("gfscale_e.pdf")



if __name__ == '__main__':
  run()
