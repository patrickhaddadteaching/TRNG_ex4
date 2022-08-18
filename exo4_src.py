import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
from ipywidgets import widgets,Layout,interactive

cell_height=30
cell_width=220
nb_p=100001
nb_p_to_be_ploted=1
p_min=0.0
p_max=0.5

current_h_value=0.997


max_required_bits=40000
current_required_bits=20000
current_relative_th=346


v_p=p_min+(p_max-p_min)*((np.arange(nb_p,dtype=np.float64)/(nb_p-1)))
v_h=np.zeros((nb_p,),dtype=np.float64)
v_index_nn=np.where((v_p*(1-v_p))!=0)[0]
v_h[v_index_nn]=(np.log2(v_p[v_index_nn])*(v_p[v_index_nn])+np.log2(1-v_p[v_index_nn])*(1-v_p[v_index_nn]))*-1
index_0p5=np.argmin(abs(v_p-0.5))
current_p_value=v_p[np.argmin(abs(v_h-current_h_value))]
v_p_to_be_ploted=np.array([current_p_value],dtype=np.float64)
v_items=[]

box_layout = Layout(height='%dpx'%cell_height,width='%dpx'%cell_width,border='1px solid gray',margin='0px 0px 0px 0px',justify_content='center',align_items='center')
box_layout2 = Layout(height='%dpx'%cell_height,width='%dpx'%(cell_width*nb_p_to_be_ploted),border='1px solid gray',margin='0px 0px 0px 0px',justify_content='center',align_items='center')

v_items_h=[]
v_items_h.append(widgets.HTMLMath('',layout=box_layout))
v_items_h.append(widgets.HTMLMath('<p align="center">Null hypothesis is <b>in fact true</b></p>',layout=box_layout))
v_items_h.append(widgets.HTMLMath('<p align="center">Null hypothesis is <b>in fact false</b></p>',layout=box_layout2))
v_items.append(v_items_h)

v_items_h=[]
v_items_h.append(widgets.HTMLMath('<p align="center" >Entropy H<sub>1</sub></p>',layout=box_layout))
v_items_h.append(widgets.HTMLMath('<p align="center" >H<sub>1</sub>=1.00</p>',layout=box_layout))
for i in range(nb_p_to_be_ploted):
    if ((v_p_to_be_ploted[i])*(1-v_p_to_be_ploted[i]))!=0:
        h=-1*(v_p_to_be_ploted[i])*np.log2(v_p_to_be_ploted[i])-(1-v_p_to_be_ploted[i])*np.log2(1-v_p_to_be_ploted[i])
    else:
        h=0
    v_items_h.append(widgets.HTMLMath('<p align="center"> H<sub>1</sub>=%.3f</p>'%h,layout=box_layout))
v_items.append(v_items_h)

v_beta = 1+binom.cdf(current_required_bits-current_relative_th, current_required_bits, v_p_to_be_ploted)-binom.cdf(current_required_bits+current_relative_th, current_required_bits, v_p_to_be_ploted)
alpha=v_beta[0]
    
v_items_h=[]
v_items_h.append(widgets.HTMLMath('<p align="center">Test <b>rejects</b> Null hypothesis </p>',layout=box_layout))
v_items_h.append(widgets.HTMLMath('<p align="center"; style="color:#FF8000";><b>&#945=%.3E</b></p>'%alpha,layout=box_layout))
for i in range(nb_p_to_be_ploted):
    v_items_h.append(widgets.HTMLMath('<p align="center"; style="color:#00FF00";><b>1-&#946=%.3E</b></p>'%(1-v_beta[i]),layout=box_layout))
v_items.append(v_items_h)

v_items_h=[]
v_items_h.append(widgets.HTMLMath('<p align="center">Test <b>does not reject</b> Null hypothesis</p>',layout=box_layout))
v_items_h.append(widgets.HTMLMath('<p align="center"; style="color:#00FF00";><b>1-&#945=%.3E</b></p>'%(1-alpha),layout=box_layout))
for i in range(nb_p_to_be_ploted):
    v_items_h.append(widgets.HTMLMath('<p align="center"; style="color:#FF0000";><b>&#946=%.3E</b></p>'%(v_beta[i]),layout=box_layout))
v_items.append(v_items_h)

nb_lines=len(v_items)
v_hb=[]
for i in range(nb_lines):
    v_tmp=v_items[i]
    nb_row=len(v_tmp)
    v_box=[]
    for j in range(nb_row):
        v_box.append(v_tmp[j])
    v_hb.append(widgets.HBox(v_box))
v_box_table=widgets.VBox(v_hb)

def plot_graph(nb_of_required_bits, delta_Th,h_in):
    
    index_pin=np.argmin(abs(v_h-h_in))
    
    th_l=int(nb_of_required_bits/2)-delta_Th
    th_h=int(nb_of_required_bits/2)+delta_Th
    
    v_prob = 1+binom.cdf(th_l, nb_of_required_bits, v_p)-binom.cdf(th_h, nb_of_required_bits, v_p)
    prob0p5=v_prob[index_0p5]

    fig_ratio=3.5
    fig, (ax2,ax1) = plt.subplots(1,2,figsize=[6*fig_ratio,fig_ratio])

    range_plot_to_zoom=0.001
    index_range_plot_to_zoom=int(range_plot_to_zoom*nb_p/(p_max-p_min))
    v_index_plot_to_zoom=index_pin+np.arange(index_range_plot_to_zoom*2,dtype=np.uint64)-index_range_plot_to_zoom
    v_good_index=np.where((v_index_plot_to_zoom<nb_p)&(v_index_plot_to_zoom>=0))[0]
    
    v_index_plot_to_zoom=v_index_plot_to_zoom[v_good_index]   
    
    ax1.set_ylabel(r'Pr{Hypo. Reject.}',fontsize=20.0)
    ax1.set_xlabel(r'$H_{1}$',fontsize=20.0)
    ax1.set_title("Null hypothesis is "+r"$\bf{in}$"+" "+r"$\bf{fact}$"+" "+r"$\bf{false}$",fontsize=20.0)    
    
    if v_prob[index_pin]>0.5:
        ax1.plot([v_h[v_index_plot_to_zoom[0]],v_h[v_index_plot_to_zoom[-1]]],[1,1],color='#000000',alpha=0.5)
        ax1.plot([v_h[index_pin],v_h[index_pin]],[v_prob[index_pin],1],color='#FF0000',marker='o')
        ax1.text(v_h[v_index_plot_to_zoom[0]]+(v_h[v_index_plot_to_zoom[-1]]-v_h[v_index_plot_to_zoom[0]])*0.6,1-(1-v_prob[index_pin])/2,r'$\beta=%E$'%(1-v_prob[index_pin]),color='#FF0000',weight='bold',backgroundcolor='white',fontsize=20.0)
    else:
        ax1.plot([v_h[v_index_plot_to_zoom[0]],v_h[v_index_plot_to_zoom[-1]]],[0,0],color='#000000',alpha=0.5)
        ax1.plot([v_h[index_pin],v_h[index_pin]],[0,v_prob[index_pin]],color='#00FF00',marker='o')
        ax1.text(v_h[v_index_plot_to_zoom[0]]+(v_h[v_index_plot_to_zoom[-1]]-v_h[v_index_plot_to_zoom[0]])*0.1,v_prob[index_pin]/2,r'$1-\beta=%E$'%(v_prob[index_pin]),color='#00FF00',weight='bold',backgroundcolor='white',fontsize=20.0)
    

    ax1.plot(v_h[v_index_plot_to_zoom],v_prob[v_index_plot_to_zoom],color='blue') 
    
    range_plot_to_zoom2=0.001
    index_range_plot_to_zoom2=int(range_plot_to_zoom2*nb_p/(p_max-p_min))
    
    v_index_plot_to_zoom2=(index_0p5-np.arange(index_range_plot_to_zoom2,dtype=np.uint64))[::-1]
    
    
    if prob0p5>0.5:
        ax2.plot([v_h[v_index_plot_to_zoom2[0]],v_h[v_index_plot_to_zoom2[-1]]],[1,1],color='#000000',alpha=0.5)
        ax2.plot([1,1],[prob0p5,1],color='#00FF00',marker='o')
        ax2.text(v_h[v_index_plot_to_zoom2[0]]+(v_h[v_index_plot_to_zoom2[-1]]-v_h[v_index_plot_to_zoom2[0]])*0.6,(prob0p5+1)/2,r'$1-\alpha=%E$'%(1-prob0p5),color='#00FF00',weight='bold',backgroundcolor='white',fontsize=20.0)
    else:
        ax2.plot([v_h[v_index_plot_to_zoom2[0]],v_h[v_index_plot_to_zoom2[-1]]],[0,0],color='#000000',alpha=0.5)
        ax2.plot([1,1],[0,prob0p5],color='#FF8000',marker='o')
        ax2.text(v_h[v_index_plot_to_zoom2[0]]+(v_h[v_index_plot_to_zoom2[-1]]-v_h[v_index_plot_to_zoom2[0]])*0.6,prob0p5/2,r'$\alpha=%E$'%(prob0p5),color='#FF8000',weight='bold',backgroundcolor='white',fontsize=20.0)

        
    ax2.plot(v_h[v_index_plot_to_zoom2],v_prob[v_index_plot_to_zoom2],color='blue') 
    ax2.set_xticks([v_h[v_index_plot_to_zoom2[0]],v_h[v_index_plot_to_zoom2[-1]]])
    ax2.set_xticklabels(['%e'%(v_h[v_index_plot_to_zoom2[0]]),'%e'%(v_h[v_index_plot_to_zoom2[-1]])])
    ax2.set_ylabel(r'Pr{Hypo. Reject.}',fontsize=20.0)
    ax2.set_xlabel(r'$H_{1}$',fontsize=20.0)    
    ax2.set_title('Null hypothesis is <b>in fact true</b>',fontsize=20.0)        
    ax2.set_title("Null hypothesis is "+r"$\bf{in}$"+" "+r"$\bf{fact}$"+" "+r"$\bf{true}$",fontsize=20.0)
    plt.show()

    if ((v_p[index_pin])*(1-v_p[index_pin]))!=0:
        h_for_table=-1*(v_p[index_pin])*np.log2(v_p[index_pin])-(1-v_p[index_pin])*np.log2(1-v_p[index_pin])
    else:
        h_for_table=0
    
    v_items[1][2].value='<p align="center"> H<sub>1</sub>=%.3f</p>'%h_for_table
        
    v_items[2][1].value='<p align="center"; style="color:#FF8000";><b>&#945=%.3E</b></p>'%(v_prob[index_0p5])
    v_items[3][1].value='<p align="center"; style="color:#00FF00";><b>1-&#945=%.3E</b></p>'%(1-v_prob[index_0p5])      
    
    v_items[2][2].value='<p align="center"; style="color:#00FF00";><b>1-&#946=%.3E</b></p>'%(v_prob[index_pin])
    v_items[3][2].value='<p align="center"; style="color:#FF0000";><b>&#946=%.3E</b></p>'%(1-v_prob[index_pin])


w_nb_of_required_bits=widgets.IntSlider(description='Number of input bits',style = {'description_width': 'initial'},value=current_required_bits,min=0,max=max_required_bits)
w_Th=widgets.IntSlider(description='relative threshold',style = {'description_width': 'initial'},value=current_relative_th,min=1,max=max_required_bits, step = 1)
w_p_in=widgets.FloatSlider(description='H<sub>1</sub>',style = {'description_width': 'initial'},value=current_h_value,min=v_h.min(),max=v_h.max())
#interactive_plot = interactive(plot_graph,{'manual': True}, nb_of_required_bits=w_nb_of_required_bits,delta_Th =w_Th ,h_in=w_p_in)
interactive_plot = interactive(plot_graph, nb_of_required_bits=w_nb_of_required_bits,delta_Th =w_Th ,h_in=w_p_in)

interactive_plot.children[0].layout=Layout(width='700px')
interactive_plot.children[1].layout=Layout(width='700px')
interactive_plot.children[2].layout=Layout(width='700px')
interactive_plot.children[-1].layout=Layout(width='700px')
#interactive_plot.children[-2].description='COMPUTE ERRORS'
#interactive_plot.children[-2].layout=Layout(width='700px')
interactive_plot.children[2].step=1E-3
interactive_plot.children[2].readout_format='.3f'
#v_box_top=widgets.VBox([interactive_plot.children[0],interactive_plot.children[1],interactive_plot.children[2],interactive_plot.children[-2],v_box_table,interactive_plot.children[-1]])
v_box_top=widgets.VBox([interactive_plot.children[0],interactive_plot.children[1],interactive_plot.children[2],v_box_table,interactive_plot.children[-1]])