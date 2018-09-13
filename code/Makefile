ALL = gfscale_a.pdf gfscale_b.pdf gfscale_c.pdf gfscale_d.pdf gfscale_e.pdf \
      cmpscale.pdf \
      resiliency_a.pdf resiliency_b.pdf resiliency_c.pdf resiliency_d.pdf \
      layouts_a.pdf layouts_b.pdf layouts_c.pdf \
      routingalgos_a.pdf routingalgos_b.pdf \
      gfft_a.pdf gfft_b.pdf gffb_a.pdf gffb_b.pdf gfsfdf_a.pdf gfsfdf_b.pdf \
      gf_ur_a.pdf gf_ur_b.pdf gf_ur_c.pdf gf_ur_d.pdf \
      gf_w_a.pdf gf_w_b.pdf gf_w_c.pdf gf_w_d.pdf \
      packets_a.pdf packets_b.pdf \
      bbw_sf_a.pdf bbw_sf_b.pdf bbw_3dfb_a.pdf bbw_3dfb_b.pdf bbw_5dfb_a.pdf bbw_5dfb_b.pdf

all: $(ALL)

gfscale_a.pdf: gfscale.py
	python3 gfscale.py
	pdfcrop gfscale_a.pdf gfscale_a.pdf
	pdfcrop gfscale_b.pdf gfscale_b.pdf
	pdfcrop gfscale_c.pdf gfscale_c.pdf
	pdfcrop gfscale_d.pdf gfscale_d.pdf
	pdfcrop gfscale_e.pdf gfscale_e.pdf

cmpscale.pdf: cmpscale.py
	python3 cmpscale.py
	pdfcrop cmpscale.pdf cmpscale.pdf

resiliency_a.pdf: resiliency.py
	python3 resiliency.py
	pdfcrop resiliency_a.pdf resiliency_a.pdf
	pdfcrop resiliency_b.pdf resiliency_b.pdf
	pdfcrop resiliency_c.pdf resiliency_c.pdf
	pdfcrop resiliency_d.pdf resiliency_d.pdf

layouts_a.pdf: layouts.py
	python3 layouts.py
	pdfcrop layouts_a.pdf layouts_a.pdf
	pdfcrop layouts_b.pdf layouts_b.pdf
	pdfcrop layouts_c.pdf layouts_c.pdf
routingalgos_a.pdf: routingalgos.py
	python3 routingalgos.py
	pdfcrop routingalgos_a.pdf routingalgos_a.pdf
	pdfcrop routingalgos_b.pdf routingalgos_b.pdf
gfft_a.pdf: cmplatency.py
	python3 cmplatency.py
	pdfcrop gfft_a.pdf gfft_a.pdf
	pdfcrop gfft_b.pdf gfft_b.pdf
	pdfcrop gffb_a.pdf gffb_a.pdf
	pdfcrop gffb_b.pdf gffb_b.pdf
	pdfcrop gfsfdf_a.pdf gfsfdf_a.pdf
	pdfcrop gfsfdf_b.pdf gfsfdf_b.pdf
gf_ur_a.pdf: cmpgfconfigs.py
	python3 cmpgfconfigs.py
	pdfcrop gf_ur_a.pdf gf_ur_a.pdf
	pdfcrop gf_ur_b.pdf gf_ur_b.pdf
	pdfcrop gf_ur_c.pdf gf_ur_c.pdf
	pdfcrop gf_ur_d.pdf gf_ur_d.pdf
	pdfcrop gf_w_a.pdf gf_w_a.pdf
	pdfcrop gf_w_b.pdf gf_w_b.pdf
	pdfcrop gf_w_c.pdf gf_w_c.pdf
	pdfcrop gf_w_d.pdf gf_w_d.pdf
packets_a.pdf: packets.py
	python3 packets.py
	pdfcrop packets_a.pdf packets_a.pdf
	pdfcrop packets_b.pdf packets_b.pdf
bbw_sf_a.pdf: bbw.py
	python3 bbw.py
	pdfcrop bbw_sf_a.pdf bbw_sf_a.pdf
	pdfcrop bbw_sf_b.pdf bbw_sf_b.pdf
	pdfcrop bbw_3dfb_a.pdf bbw_3dfb_a.pdf
	pdfcrop bbw_3dfb_b.pdf bbw_3dfb_b.pdf
	pdfcrop bbw_5dfb_a.pdf bbw_5dfb_a.pdf
	pdfcrop bbw_5dfb_b.pdf bbw_5dfb_b.pdf
