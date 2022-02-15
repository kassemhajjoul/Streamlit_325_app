import pandas as pd
import numpy as np
import scipy as sp
import chart_studio.plotly as py
import plotly as plt
import geopy
import streamlit as st
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.offline import init_notebook_mode, iplot
import plotly.express as px
st.title("MSBA 325 Assignment 2")
st.markdown("Kassem Hajjoul")
df=pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQ6LntwY7UX5EP4UikQn2-AfzzhaVmnAVYbR0Tj0gJZ_AHwvueSOhshraFIJeelYixzqHgK-8a3Ottk/pub?gid=1546798312&single=true&output=csv")
st.header("Our Data:")
st.markdown("Inspecting the table")
st.write(df.head())
indexnames = df[df['Country']=='Israel'].index
df.drop(indexnames, inplace= True)
df.reset_index(inplace=True)
st.header("Data table:")
tablee = ff.create_table(df)
st.plotly_chart(tablee)
data = [go.Bar(x=df.Country.head(100),
            y=df.Score.head(100))]
st.header("Line plot for the happiness scores per countries")
st.plotly_chart(data)
#Plotting the effect of GDP PER Capita, Freedom and Social support on the total score
ax1=px.scatter(df, x="Score", y="GDP_per_capita", labels={"Score": "Score", "GDP_per_capita":"GDP Per Capita"},color="Social_support", size = "Freedom")
st.header("Scatter plot on the relationship between different economic and social factors")
st.plotly_chart(ax1)
st.header("Stacked bar plot for various economic and social factors per countries")
ax3=px.bar(df,x="Country",y=["Score","GDP_per_capita","Generosity","Corruption"])
st.plotly_chart(ax3)
#Top 10 countries
df=df.sort_values(by=['Score', 'Country'])
Top_countries=df["Country"].tail(10)
Top_scores=df["Score"].tail(10)
st.header("The happiest 10 countries ")
ax4=px.bar(df,Top_countries,Top_scores,labels={"x":"Country","y":"Happiness Score"})
st.plotly_chart(ax4)
st.header("Mapping the factors on the world map:")
from geopy.geocoders import Nominatim
Long=[]
Lat=[]
def Geocode(country):
        try:
            geolocator=Nominatim(user_agent="your_app_name")
            return geolocator.geocode(country)
        except:
         return Geocode(country)
    
for i in(df["Country"]):
    if Geocode(i) != None:
        loc=Geocode(i)
        Long.append(loc.longitude)
        Lat.append(loc.latitude)
    else:
        Lat.append(np.nan)
        Long.append(np.nan)
df['Longitude']=Long
df['Latitude']=Lat
#Making sure the function is working correctly
st.write(df.info())
ax4=plt.express.scatter_geo(data_frame=df,lon=df["Longitude"],lat=df["Latitude"],size=df["Rank"],color=df["Score"])
st.plotly_chart(ax4)
st.header("Healthy Life expectancy per countries")
ax5=px.histogram(df,x="Healthy_life_expectancy",hover_name="Country",color="Country",labels={"Healthy_life_expectancy":"Healthy Life Expectancy Score","count":"Score"})
st.plotly_chart(ax5)
x=df['Country']
y=df['Score']
z=df["Corruption"]
trace=go.Scatter3d(x=x,y=y,z=z,mode='markers',marker=dict(size=12,color=z,colorscale='Viridis',opacity=0.8))
data=[trace]
layout=go.Layout(margin=dict(l=0,r=0,b=0,t=0))
fig=go.Figure(data=data, layout=layout)
st.header("3D Plotting the factors on countries:")
st.plotly_chart(fig)
import chart_studio.plotly as py
import numpy as np

data = [dict(
        visible = False,
        line=dict(color='#00CED1', width=6),
        name = '𝜈 = '+str(step),
        x = np.arange(0,10,0.01),
        y = np.sin(step*np.arange(0,10,0.01))) for step in np.arange(0,5,0.1)]
data[10]['visible'] = True

steps = []
for i in range(len(data)):
    step = dict(
        method = 'restyle',
        args = ['visible', [False] * len(data)],
    )
    step['args'][1][i] = True # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active = 10,
    currentvalue = {"prefix": "Frequency: "},
    pad = {"t": 50},
    steps = steps
)]

layout = dict(sliders=sliders)
fig = dict(data=data, layout=layout)
st.header("Tutorial:")
st.markdown("Some plots i did not apply on my dataset:")
df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")
table1 = ff.create_table(df)
st.plotly_chart(table1)
data = [go.Bar(x=df.School,
            y=df.Gap)]

st.plotly_chart(data)
trace_women = go.Bar(x=df.School,
                  y=df.Women,
                  name='Women',
                  marker=dict(color='#ffcdd2'))

trace_men = go.Bar(x=df.School,
                y=df.Men,
                name='Men',
                marker=dict(color='#A2D5F2'))

trace_gap = go.Bar(x=df.School,
                y=df.Gap,
                name='Gap',
                marker=dict(color='#59606D'))

data = [trace_women, trace_men, trace_gap]

layout = go.Layout(title="Average Earnings for Graduates",
                xaxis=dict(title='School'),
                yaxis=dict(title='Salary (in thousands)'))

fig3= go.Figure(data=data, layout=layout)
st.plotly_chart(fig3)
st.header("Frequency slider:")
st.plotly_chart(fig)
