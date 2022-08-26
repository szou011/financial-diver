from bokeh.layouts import column, row
from bokeh.plotting import figure, curdoc
from bokeh.models import Select

from models import get_retailer, get_retailgroup

groupname, groupcount = get_retailer("Farmers")


# create a plot and style its properties
p = figure(x_range=groupname, width=1600, height=400, toolbar_location=None)

# add a text renderer to the plot (no data yet)
r = p.vbar(x=groupname, top=groupcount, width=0.9, bottom=0)
print(r.data_source.data)
p.xaxis.major_label_orientation = 1

ds = r.data_source

def update_retailgroup(attr, old, new):
    global groupname, groupcount
    groupname, groupcount = get_retailer(new)
    new_data = {'x':groupname, 'top':groupcount}
    print(new_data)
    p.x_range.factors = groupname
    ds.data = new_data  

select = Select(title='Select Retail Group:', value='Farmers', options=get_retailgroup())
select.on_change('value', update_retailgroup)
# put the button and plot in a layout and add to the document
curdoc().add_root(row(select, p))