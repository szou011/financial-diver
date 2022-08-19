from database import acc_group, group_count

from bokeh.layouts import column
from bokeh.plotting import figure, curdoc

# create a plot and style its properties
p = figure(width=400, height=400)

# add a text renderer to the plot (no data yet)
p.vbar(x=acc_group, top=group_count, width=0.5, bottom=0)


# put the button and plot in a layout and add to the document
curdoc().add_root(column(p))