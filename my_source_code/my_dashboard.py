# Get libraries for data import and visualization
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import datetime
import os
import glob

# ****************
# * Get the data *
# ****************

# Get current script directory.
script_directory = os.path.dirname(os.path.realpath(__file__))

# Define relative paths for input and output subdirectories.
input_path = "../my_data_intermediate"
output_path = "../my_data_outputs"

# Join script directory and relative paths for absolute paths.
abs_input_path = os.path.join(script_directory, input_path)
abs_output_path = os.path.join(script_directory, output_path)

# Get the pickle files and sort alphabetically.
files = glob.glob(os.path.join(abs_input_path, "*.csv"))
files.sort()

# Read each .csv into a dataframe.
dfs = [pd.read_csv(f) for f in files]

# Unpack the list of dfs.
df_hand, df_loc, df_loggers, df_rain = dfs

# ********************
# * Create Dashboard *
# ********************

# Initialize a faceted dashboard
fig = make_subplots(
    rows=2, cols=2,
    specs=[[{},{'rowspan': 2, 'type': 'scattermapbox'}],
           [{}, None]],
    subplot_titles=('Hourly Water Levels',
                    'Monitoring Locations',
                    'Daily Rainfall',
                    ),
    column_widths=[0.67, 0.33],
    row_heights=[0.7, 0.3],
    horizontal_spacing=0.03,
    vertical_spacing=0.07,
    shared_xaxes=True
)

# UPPER LEFT: Add a trace for each well in the AESI set.
for col in df_loggers.columns[2:]:
    fig.add_trace(
       go.Scattergl(
        x=df_loggers.Date,
        y=df_loggers[col],
        mode='lines',
        name=col),
    row=1,
    col=1)

# UPPER LEFT: Label the y-axis of elevations plot.
fig.update_yaxes(
   title_text="Water Level Elevation (ft)",
   showticklabels=True,
   automargin=True,
   row=1,
   col=1)

# UPPER LEFT: Add a trace for well in the hand data set.
for col in df_hand.columns[2:]:
   fig.add_trace(
      go.Scattergl(
         x=df_hand.Date,
         y=df_hand[col],
         mode='markers',
         name=col),
    row=1,
    col=1)

# MIDDLE LEFT: Add rainfall data as a barplot.
for gauge in df_rain['Weather Station'].unique():
   subset = df_rain[df_rain['Weather Station'] == gauge]
   fig.add_trace(
      go.Scattergl(
         x=subset.Date,
         y=subset['Rain (in)'],
         mode='lines',
         name=gauge,
      ),
      row=2,
      col=1
      )

# MIDDLE LEFT: Label the y-axis of rainfall plot.
fig.update_yaxes(
   title_text="Rainfall (in)",
   showticklabels=True,
   automargin=True,
   row=2,
   col=1
   )

# MIDDLE LEFT: configure the rainfall bars to display side-by-side.
fig.update_layout(barmode='group')

# RIGHT SIDE: Add a map with the monitoring locations.
fig.add_trace(
   go.Scattermapbox(
      lat=df_loc.lat,
      lon=df_loc.lon,
      mode='markers+text',
      marker=dict(size=15),
      text=df_loc.Name,
      textposition='middle left',
      hovertemplate=df_loc.Name+
       '<br>Lat: %{lat:.4f}<br>'+
       'Lon: %{lon:.4f}<extra></extra>',
      showlegend=False,
   ),
   row=1,
   col=2
)

# **********************************
# * Configure the dashboard layout *
# **********************************

# Move legend to left side of dashboard.
fig.update_layout(
   legend=dict(
      x=-0.26,
      y=0.5
   )
)

# Change the default colors to improve readability.
fig.update_layout(plot_bgcolor='whitesmoke')

# Make the legend background have no color to stop obscuring tick labels.
fig.update_layout(legend_bgcolor='rgba(0,0,0,0)')

# Configure mapbox.
fig.update_layout(
   mapbox=dict(
      style='open-street-map',
      zoom=12,
      center=dict(
         # Center of Project Site
         lat=49, # lat and lon removed for privacy
         lon=-122),
   ),
)

# Set the title and add subtitle with today's date.
current_date = datetime.datetime.today().strftime('%Y-%m-%d')
title = "<b>Project Site Water Level Monitoring<b>"
subtitle = "<br><sub>Dashboard Prepared On: " + current_date
fig.update_layout(title_text=title+subtitle)

# Change size of dashboard.
fig.update_layout(
   height=850,
   width=1900
)

# Show the axes labels.
fig.update_layout(
   xaxis=dict(showticklabels=True),
   xaxis2=dict(showticklabels=True)
   )

# Set pan mode as default plot interaction.
fig.update_layout(dragmode='pan')

# Add hovermode button.
fig.update_layout(modebar_add=["v1hovermode"])

# Set scroll-to-zoom for zooming on html.
config = {'scrollZoom': True}

# Show the figure upon run.
fig.show(config=config)

# Download the dashboard to a shareable .html file.
fig.write_html(os.path.join(
   abs_output_path,
   "ProjectSite_Dashboard_" + current_date + ".html"
   ),  
   config=config)