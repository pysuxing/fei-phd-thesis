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

  # subfigure sf
  Rsf=np.array([50,98,338,578,722,1058,1682,1922,2738,3362,4418,5618,7442])
  Csf=np.array([65,175,1105,2465,3439,6095,12238,14927,25382,34481,51935,74975,113521])
  Ksf=np.array([7,11,19,25,29,35,43,47,55,61,71,79,91])
  Psf1=np.ceil(Csf*2/Rsf)
  Nsf1=Rsf*Psf1
  Ksf1=Psf1+Ksf
  Psf2=np.floor(Ksf/2)
  Nsf2=Rsf*Psf2
  Ksf2=Psf2+Ksf
  Psf3=np.ceil(Csf*2/(Rsf*0.67))
  Nsf3=Rsf*Psf3
  Ksf3=Psf3+Ksf
  Psf4=np.ceil(Csf*2/(Rsf*0.5))
  Nsf4=Rsf*Psf4
  Ksf4=Psf4+Ksf
  Psf5=np.ceil(Csf*2/(Rsf*0.35))
  Nsf5=Rsf*Psf5
  Ksf5=Psf5+Ksf

  R1=np.array([25,49,121,169,289,361,529,961,2209,2809,3721,5329])
  C1=np.array([38,72,342,564,1248,1750,3072,7470,25944,37206,56730,97236])
  K1=np.array([6,10,16,18,24,28,34,46,70,78,90,108])
  P11=np.ceil(C1*2/R1)
  N11=R1*P11
  K11=P11+K1
  P12=np.ceil(C1*2/(R1*0.75))
  N12=R1*P12
  K12=P12+K1
  P13=np.ceil(C1*2/(R1*0.67))
  N13=R1*P13
  K13=P13+K1
  P14=np.ceil(C1*2/(R1*0.5))
  N14=R1*P14
  K14=P14+K1
  P15=np.ceil(C1*2/(R1*0.35))
  N15=R1*P15
  K15=P15+K1

  R2=np.array([50,98,242,338,595,578,703,722,1058,1682,1922,2738,4606,5618,7442])
  C2=np.array([69,190,1331,2197,5202,4913,6498,6915,12226,24389,29791,50653,112800,148877,226981])
  K2=np.array([11,17,27,31,42,41,46,47,58,71,77,91,121,131,151])
  P21=np.ceil(C2*2/R2)
  N21=R2*P21
  K21=P21+K2
  P22=np.ceil(C2*2/(R2*0.75))
  N22=R2*P22
  K22=P22+K2
  P23=np.ceil(C2*2/(R2*0.67))
  N23=R2*P23
  K23=P23+K2
  P24=np.ceil(C2*2/(R2*0.5))
  N24=R2*P24
  K24=P24+K2
  P25=np.ceil(C2*2/(R2*0.35))
  N25=R2*P25
  K25=P25+K2

  R3=np.array([66,77,78,91,136,153,171,190,276,299,406,435,666,703,820,861,1128,1175,1378,1431,1830,1891,2278,2345,2628,2701,3160,3916,4656])
  C3=np.array([99,144,117,168,272,368,418,475,828,1014,1421,1712,2997,3450,4100,4268,6768,7470,8957,9774,13725,14724,19363,20502,24703,24966,31600,43076,55872])
  K3=np.array([11,12,11,12,15,16,18,19,23,24,27,28,35,36,39,40,47,48,51,52,59,60,67,68,71,72,79,87,95])
  P31=np.ceil(C3*2/R3)
  N31=R3*P31
  K31=P31+K3
  P32=np.ceil(C3*2/(R3*0.75))
  N32=R3*P32
  K32=P32+K3
  P33=np.ceil(C3*2/(R3*0.67))
  N33=R3*P33
  K33=P33+K3
  P34=np.ceil(C3*2/(R3*0.5))
  N34=R3*P34
  K34=P34+K3
  P35=np.ceil(C3*2/(R3*0.35))
  N35=R3*P35
  K35=P35+K3

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

  if trans:
    fig, ax = plt.subplots()
    ax.plot(Nsf4, Rsf , marker=markers[0], markersize=markersize, label='$SF$')
    ax.plot(N14, R1, marker=markers[1], markersize=markersize, label='$GF(n=q)$')
    ax.plot(N24, R2, marker=markers[2], markersize=markersize, label='$GF(n=2q)$')
    ax.plot(N34, R3, marker=markers[3], markersize=markersize, label='$GF(n=q/2)$')
    ax.set_position([.2,.2,.7,.7])
    ax.set_xlim(0, 12000)
    ax.set_xlabel('Network Size ($N$)', fontsize=24, weight='normal')
    ax.set_ylim(0, 800)
    ax.set_ylabel('Number of Routers ($N_r$)', fontsize=24, weight='normal')
    ax.ticklabel_format(style='sci', scilimits=(0,0))
    ax.tick_params(labelsize=20)
    ax.xaxis.get_offset_text().set_fontsize(20)
    ax.yaxis.get_offset_text().set_fontsize(20)
    ax.legend(loc='upper left')
    fig.savefig("bbw_sf_b.pdf")
  else:
    fig, ax = plt.subplots()
    ax.plot(Rsf, Nsf4, marker=markers[0], markersize=markersize, label='$SF$')
    ax.plot(R1, N14, marker=markers[1], markersize=markersize, label='$GF(n=q)$')
    ax.plot(R2, N24, marker=markers[2], markersize=markersize, label='$GF(n=2q)$')
    ax.plot(R3, N34, marker=markers[3], markersize=markersize, label='$GF(n=q/2)$')
    ax.set_position([.2,.2,.7,.7])
    ax.set_xlim(0, 800)
    ax.set_xlabel('Number of Routers ($N_r$)', fontsize=24, weight='normal')
    ax.set_ylim(0, 12000)
    ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
    ax.ticklabel_format(style='sci', scilimits=(0,0))
    ax.tick_params(labelsize=20)
    ax.xaxis.get_offset_text().set_fontsize(20)
    ax.yaxis.get_offset_text().set_fontsize(20)
    ax.legend(loc='upper left')
    fig.savefig("bbw_sf_b.pdf")

  # subfigure 3d fb
  nfb=np.arange(7,33,2)
  Rfb=np.power(nfb,3)
  Cfb=np.power(nfb,4)/4
  Kfb=3*(nfb-1)
  Pfb1=np.ceil(Cfb*2/Rfb)
  Nfb1=Rfb*Pfb1
  Kfb1=Pfb1+Kfb
  Pfb2=np.ceil(Cfb*2/(Rfb*0.75))
  Nfb2=Rfb*Pfb2
  Kfb2=Pfb2+Kfb
  Pfb3=np.ceil(Cfb*2/(Rfb*0.67))
  Nfb3=Rfb*Pfb3
  Kfb3=Pfb3+Kfb
  Pfb4=np.ceil(Cfb*2/(Rfb*0.5))
  Nfb4=Rfb*Pfb4
  Kfb4=Pfb4+Kfb
  Pfb5=np.ceil(Cfb*2/(Rfb*0.35))
  Nfb5=Rfb*Pfb5
  Kfb5=Pfb5+Kfb
  Aq1=np.arange(4,50,2)
  Kq1=Aq1
  Rq1=(Aq1*Kq1+1)*Aq1
  nq1=Aq1*Kq1+1
  Cq1=np.ceil(nq1/2)*np.floor(nq1/2)
  Pq11=np.ceil(Cq1*2/Rq1)
  Nq11=Pq11*Rq1
  Kq11=Pq11+Kq1+Aq1-1
  Pq12=np.ceil(Cq1*2/(Rq1*0.75))
  Nq12=Pq12*Rq1
  Kq12=Pq12+Kq1+Aq1-1
  Pq13=np.ceil(Cq1*2/(Rq1*0.67))
  Nq13=Pq13*Rq1
  Kq13=Pq13+Kq1+Aq1-1
  Pq14=np.ceil(Cq1*2/(Rq1*0.5))
  Nq14=Pq14*Rq1
  Kq14=Pq14+Kq1+Aq1-1
  Pq15=np.ceil(Cq1*2/(Rq1*0.35))
  Nq15=Pq15*Rq1
  Kq15=Pq15+Kq1+Aq1-1
  Aq2=np.arange(6,70,2)
  Kq2=Aq2/2
  Rq2=(Aq2*Kq2+1)*Aq2
  nq2=Aq2*Kq2+1
  Cq2=np.ceil(nq2/2)*np.floor(nq2/2)
  Pq21=np.ceil(Cq2*2/Rq2)
  Nq21=Pq21*Rq2
  Kq21=Pq21+Kq2+Aq2-1
  Pq22=np.ceil(Cq2*2/(Rq2*0.75))
  Nq22=Pq22*Rq2
  Kq22=Pq22+Kq2+Aq2-1
  Pq23=np.ceil(Cq2*2/(Rq2*0.67))
  Nq23=Pq23*Rq2
  Kq23=Pq23+Kq2+Aq2-1
  Pq24=np.ceil(Cq2*2/(Rq2*0.5))
  Nq24=Pq24*Rq2
  Kq24=Pq24+Kq2+Aq2-1
  Pq25=np.ceil(Cq2*2/(Rq2*0.35))
  Nq25=Pq25*Rq2
  Kq25=Pq25+Kq2+Aq2-1
  Aq3=np.arange(3,50,2)
  Kq3=Aq3*2
  Rq3=(Aq3*Kq3+1)*Aq3
  nq3=Aq3*Kq3+1
  Cq3=np.ceil(nq3/2)*np.floor(nq3/2)
  Pq31=np.ceil(Cq3*2/Rq3)
  Nq31=Pq31*Rq3
  Kq31=Pq31+Kq3+Aq3-1
  Pq32=np.ceil(Cq3*2/(Rq3*0.75))
  Nq32=Pq32*Rq3
  Kq32=Pq32+Kq3+Aq3-1
  Pq33=np.ceil(Cq3*2/(Rq3*0.67))
  Nq33=Pq33*Rq3
  Kq33=Pq33+Kq3+Aq3-1
  Pq34=np.ceil(Cq3*2/(Rq3*0.5))
  Nq34=Pq34*Rq3
  Kq34=Pq34+Kq3+Aq3-1
  Pq35=np.ceil(Cq3*2/(Rq3*0.35))
  Nq35=Pq35*Rq3
  Kq35=Pq35+Kq3+Aq3-1

  fig, ax = plt.subplots()
  ax.plot(Kfb4, Nfb4, marker=markers[0], markersize=markersize, label='$3D\ FB$')
  ax.plot(Kq14, Nq14, marker=markers[1], markersize=markersize, label='$GF(a=h)$')
  ax.plot(Kq24, Nq24, marker=markers[2], markersize=markersize, label='$GF(a=2h)$')
  ax.plot(Kq34, Nq34, marker=markers[3], markersize=markersize, label='$GF(a=h/2)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, 50)
  ax.set_xlabel('Router Radix ($r$)', fontsize=24, weight='normal')
  ax.set_ylim(0, 100000)
  ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
  ax.set_xticks(rxticks)
  ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  ax.tick_params(labelsize=20)
  ax.yaxis.get_offset_text().set_fontsize(20)
  ax.legend(loc='upper left')
  fig.savefig("bbw_3dfb_a.pdf")

  if trans:
    fig, ax = plt.subplots()
    ax.plot(Nfb4, Rfb, marker=markers[0], markersize=markersize, label='$3D\ FB$')
    ax.plot(Nq14, Rq1, marker=markers[1], markersize=markersize, label='$GF(a=h)$')
    ax.plot(Nq24, Rq2, marker=markers[2], markersize=markersize, label='$GF(a=2h)$')
    ax.plot(Nq34, Rq3, marker=markers[3], markersize=markersize, label='$GF(a=h/2)$')
    ax.set_position([.2,.2,.7,.7])
    ax.set_xlim(0, 100000)
    ax.set_xlabel('Network Size ($N$)', fontsize=24, weight='normal')
    ax.set_ylim(0, 10000)
    ax.set_ylabel('Number of Routers ($N_r$)', fontsize=24, weight='normal')
    ax.ticklabel_format(style='sci', scilimits=(0,0))
    ax.tick_params(labelsize=20)
    ax.xaxis.get_offset_text().set_fontsize(20)
    ax.yaxis.get_offset_text().set_fontsize(20)
    ax.legend(loc='upper left')
    fig.savefig("bbw_3dfb_b.pdf")
  else:
    fig, ax = plt.subplots()
    ax.plot(Rfb, Nfb4 , marker=markers[0], markersize=markersize, label='$3D\ FB$')
    ax.plot(Rq1, Nq14, marker=markers[1], markersize=markersize, label='$GF(a=h)$')
    ax.plot(Rq2, Nq24, marker=markers[2], markersize=markersize, label='$GF(a=2h)$')
    ax.plot(Rq3, Nq34, marker=markers[3], markersize=markersize, label='$GF(a=h/2)$')
    ax.set_position([.2,.2,.7,.7])
    ax.set_xlim(0, 10000)
    ax.set_xlabel('Number of Routers ($N_r$)', fontsize=24, weight='normal')
    ax.set_ylim(0, 100000)
    ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
    ax.ticklabel_format(style='sci', scilimits=(0,0))
    ax.tick_params(labelsize=20)
    ax.xaxis.get_offset_text().set_fontsize(20)
    ax.yaxis.get_offset_text().set_fontsize(20)
    ax.legend(loc='upper left')
    fig.savefig("bbw_3dfb_b.pdf")

  # subfigure 5d fb
  n5fb=np.arange(4,20,2)
  R5fb=np.power(n5fb,5)
  C5fb=np.power(n5fb,6)/4
  K5fb=5*(n5fb-1)
  P5fb1=np.ceil(C5fb*2/R5fb)
  N5fb1=R5fb*P5fb1
  K5fb1=P5fb1+K5fb
  P5fb2=np.ceil(C5fb*2/(R5fb*0.75))
  N5fb2=R5fb*P5fb2
  K5fb2=P5fb2+K5fb
  P5fb3=np.ceil(C5fb*2/(R5fb*0.67))
  N5fb3=R5fb*P5fb3
  K5fb3=P5fb3+K5fb
  P5fb4=np.ceil(C5fb*2/(R5fb*0.5))
  N5fb4=R5fb*P5fb4
  K5fb4=P5fb4+K5fb
  P5fb5=np.ceil(C5fb*2/(R5fb*0.35))
  N5fb5=R5fb*P5fb5
  K5fb5=P5fb5+K5fb
  Rnq1=np.array([242,338,578,722,1058,1922,4418,5618,7442,10658,12482,13778,15842])
  Cnq1=np.array([204,290,693,1531,1542,3860,25764,34686,52850,95033,115482,134602,171521])
  Knq1=np.array([8,9,12,14,17,23,35,39,45,54,59,62,66])
  Pnq11=np.ceil(Cnq1*2/Rnq1)
  Nnq11=Rnq1*Pnq11
  Knq11=Pnq11+Knq1+1
  Pnq12=np.ceil(Cnq1*2/(Rnq1*0.75))
  Nnq12=Rnq1*Pnq12
  Knq12=Pnq12+Knq1+1
  Pnq13=np.ceil(Cnq1*2/(Rnq1*0.67))
  Nnq13=Rnq1*Pnq13
  Knq13=Pnq13+Knq1+1
  Pnq14=np.ceil(Cnq1*2/(Rnq1*0.5))
  Nnq14=Rnq1*Pnq14
  Knq14=Pnq14+Knq1+1
  Pnq15=np.ceil(Cnq1*2/(Rnq1*0.35))
  Nnq15=Rnq1*Pnq15
  Knq15=Pnq15+Knq1+1
  Rnq2=np.array([507,867,2523,4107,8427,11163,15987,23763,28227,30603,38307])
  Cnq2=np.array([212,356,1762,5594,15726,25932,39808,57886,103146,110830,157520])
  Knq2=np.array([6,8,14,18,26,30,36,44,48,50,56])
  Pnq21=np.ceil(Cnq2*2/Rnq2)
  Nnq21=Rnq2*Pnq21
  Knq21=Pnq21+Knq2+2
  Pnq22=np.ceil(Cnq2*2/(Rnq2*0.75))
  Nnq22=Rnq2*Pnq22
  Knq22=Pnq22+Knq2+2
  Pnq23=np.ceil(Cnq2*2/(Rnq2*0.67))
  Nnq23=Rnq2*Pnq23
  Knq23=Pnq23+Knq2+2
  Pnq24=np.ceil(Cnq2*2/(Rnq2*0.5))
  Nnq24=Rnq2*Pnq24
  Knq24=Pnq24+Knq2+2
  Pnq25=np.ceil(Cnq2*2/(Rnq2*0.35))
  Nnq25=Rnq2*Pnq25
  Knq25=Pnq25+Knq2+2
  Rnq3=np.array([484,1156,1444,6724,7396,17956,21316,31684,37636,45796,51076,68644])
  Cnq3=np.array([216,686,1012,17172,18896,35942,42168,176220,126597,305869,138786,535112])
  Knq3=np.array([4,6,7,15,16,25,27,33,36,40,42,49])
  Pnq31=np.ceil(Cnq3*2/Rnq3)
  Nnq31=Rnq3*Pnq31
  Knq31=Pnq31+Knq3+3
  Pnq32=np.ceil(Cnq3*2/(Rnq3*0.75))
  Nnq32=Rnq3*Pnq32
  Knq32=Pnq32+Knq3+3
  Pnq33=np.ceil(Cnq3*2/(Rnq3*0.67))
  Nnq33=Rnq3*Pnq33
  Knq33=Pnq33+Knq3+3
  Pnq34=np.ceil(Cnq3*2/(Rnq3*0.5))
  Nnq34=Rnq3*Pnq34
  Knq34=Pnq34+Knq3+3
  Pnq35=np.ceil(Cnq3*2/(Rnq3*0.35))
  Nnq35=Rnq3*Pnq35
  Knq35=Pnq35+Knq3+3
  Rnq4=np.array([484,1014,1734,2527,22090,36517,37210,63928,183184,178766])
  Cnq4=np.array([216,352,766,1218,15152,20596,29956,58980,166656,200292])
  Knq4=np.array([4,3,4,4,7,6,9,9,10,12])
  anq4=np.array([3,5,5,6,9,12,9,11,15,13])
  Pnq41=np.ceil(Cnq4*2/Rnq4)
  Nnq41=Rnq4*Pnq41
  Knq41=Pnq41+Knq4+anq4
  Pnq42=np.ceil(Cnq4*2/(Rnq4*0.75))
  Nnq42=Rnq4*Pnq42
  Knq42=Pnq42+Knq4+anq4
  Pnq43=np.ceil(Cnq4*2/(Rnq4*0.67))
  Nnq43=Rnq4*Pnq43
  Knq43=Pnq43+Knq4+anq4
  Pnq44=np.ceil(Cnq4*2/(Rnq4*0.5))
  Nnq44=Rnq4*Pnq44
  Knq44=Pnq44+Knq4+anq4
  Pnq45=np.ceil(Cnq4*2/(Rnq4*0.35))
  Nnq45=Rnq4*Pnq45
  Knq45=Pnq45+Knq4+anq4

  fig, ax = plt.subplots()
  ax.plot(K5fb4, N5fb4, marker=markers[0], markersize=markersize, label='$5D\ FB$')
  ax.plot(Knq14, Nnq14, marker=markers[1], markersize=markersize, label='$GF(a=2)$')
  ax.plot(Knq24, Nnq24, marker=markers[2], markersize=markersize, label='$GF(a=3)$')
  ax.plot(Knq34, Nnq34, marker=markers[3], markersize=markersize, label='$GF(a=4)$')
  ax.plot(Knq44, Nnq44, marker=markers[3], markersize=markersize, label='$GF(h \leq a < 2h)$')
  ax.set_position([.2,.2,.7,.7])
  ax.set_xlim(0, 50)
  ax.set_xlabel('Router Radix ($r$)', fontsize=24, weight='normal')
  ax.set_ylim(0, 200000)
  ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
  ax.set_xticks(rxticks)
  ax.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
  ax.tick_params(labelsize=20)
  ax.yaxis.get_offset_text().set_fontsize(20)
  ax.legend(loc='upper left')
  fig.savefig("bbw_5dfb_a.pdf")

  if trans:
    fig, ax = plt.subplots()
    ax.plot(N5fb4, R5fb, marker=markers[0], markersize=markersize, label='$5D\ FB$')
    ax.plot(Nnq14, Rnq1, marker=markers[1], markersize=markersize, label='$GF(a=2)$')
    ax.plot(Nnq24, Rnq2, marker=markers[2], markersize=markersize, label='$GF(a=3)$')
    ax.plot(Nnq34, Rnq3, marker=markers[3], markersize=markersize, label='$GF(a=4)$')
    ax.plot(Nnq44, Rnq4, marker=markers[3], markersize=markersize, label='$GF(h \leq a < 2h)$')
    ax.set_position([.2,.2,.7,.7])
    ax.set_xlim(0, 200000)
    ax.set_xlabel('Network Size ($N$)', fontsize=24, weight='normal')
    ax.set_ylim(0, 65000)
    ax.set_ylabel('Number of Routers ($N_r$)', fontsize=24, weight='normal')
    ax.ticklabel_format(style='sci', scilimits=(0,0))
    ax.tick_params(labelsize=20)
    ax.xaxis.get_offset_text().set_fontsize(20)
    ax.yaxis.get_offset_text().set_fontsize(20)
    ax.legend(loc='upper left')
    fig.savefig("bbw_5dfb_b.pdf")
  else:
    fig, ax = plt.subplots()
    ax.plot(R5fb, N5fb4, marker=markers[0], markersize=markersize, label='$5D\ FB$')
    ax.plot(Rnq1, Nnq14, marker=markers[1], markersize=markersize, label='$GF(a=2)$')
    ax.plot(Rnq2, Nnq24, marker=markers[2], markersize=markersize, label='$GF(a=3)$')
    ax.plot(Rnq3, Nnq34, marker=markers[3], markersize=markersize, label='$GF(a=4)$')
    ax.plot(Rnq4, Nnq44, marker=markers[3], markersize=markersize, label='$GF(h \leq a < 2h)$')
    ax.set_position([.2,.2,.7,.7])
    ax.set_xlim(0, 65000)
    ax.set_xlabel('Number of Routers ($N_r$)', fontsize=24, weight='normal')
    ax.set_ylim(0, 200000)
    ax.set_ylabel('Network Size ($N$)', fontsize=24, weight='normal')
    ax.ticklabel_format(style='sci', scilimits=(0,0))
    ax.tick_params(labelsize=20)
    ax.xaxis.get_offset_text().set_fontsize(20)
    ax.yaxis.get_offset_text().set_fontsize(20)
    ax.legend(loc='upper left')
    fig.savefig("bbw_5dfb_b.pdf")
  


if __name__ == '__main__':
  run()
