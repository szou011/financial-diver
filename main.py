from bokeh.plotting import figure, row
from bokeh.io import curdoc
from bokeh.models import Select

from models import get_retailer, get_retailgroup

groupname, groupcount = get_retailer("Farmers")


# create a plot and style its properties
p = figure(x_range=groupname, width=640, height=400, toolbar_location=None, name='bokeh_jinja_figure')

# add a text renderer to the plot (no data yet)
r = p.vbar(x=groupname, top=groupcount, width=0.9, bottom=0)
p.xaxis.major_label_orientation = 1

ds = r.data_source

def update_retailgroup(attr, old, new):
    global groupname, groupcount
    groupname, groupcount = get_retailer(new)
    new_data = {'x':groupname, 'top':groupcount}
    p.x_range.factors = groupname
    ds.data = new_data  

select = Select(title='Select Retail Group:', value='Farmers', options=get_retailgroup(), name='bokeh_jinja_widget')
select.on_change('value', update_retailgroup)
# put the button and plot in a layout and add to the document
curdoc().add_root(row(select, p))
