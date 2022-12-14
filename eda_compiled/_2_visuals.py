#%%
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from _1_load_data import Load_Data
#import streamlit as st

import warnings
warnings.filterwarnings('ignore')


class Graphs:

    def __init__(self):

        dl=Load_Data()
        self.pp_raw_hotel_data=dl.pp_raw_hotel_data()


        #Config
        self.config = {
        'toImageButtonOptions': {
            'format': 'png', # one of png, svg, jpeg, webp
            'filename': 'custom_image',
            'height': 490,
            'width': 1300,
            'scale': 2 # Multiply title/legend/axis/canvas sizes by this factor
  }
}


        #Background Color
        self.bgcolor="#FAFAF9"  ##F8FBFB"  #FAFAF9  #F0F2F6
        self.gridcolor="#D4E5E6"


        #Content Colors
        purple="#646EC8"
        green="#4fdd63"
        red="#DD634F"

        self.line_color1=purple
        self.line_color2=green
        self.line_color3=red


        #Annotation Colors
        self.ann_text_color="#ffffff"
        self.ann_arrow_color="#636363"
        self.ann_border_color="#c7c7c7"
        self.ann_bg_color="#ff7f0e"

        self.ann_bg_color2="#63A2B6"
        self.ann_bg_color3="black"
        self.ann_bg_color4="red"



        #Style- CSS #FAFAF9

    #Annotate- Non Subplot
    def annotate(self,fig,x,y,text,axv,axy, bg_color, border_color,showarrow=True):
        border_color=border_color
        bg_color=bg_color
        
        
        fig.add_annotation(
        x=x,
        y=y,
        xref="x",
        yref="y",
        text=text,
        showarrow=showarrow,
        font=dict(
            family="Courier New, monospace",
            size=12, 
            color=self.ann_text_color
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1,
        arrowcolor=self.ann_arrow_color,
        ax=axv,
        ay=axy,
        bordercolor=border_color,
        borderwidth=2,
        borderpad=4,
        bgcolor=bg_color,
        opacity=0.8
        )


    #Annotate Subplot
    def annotate_subplot_box(self,fig,x,y,text,axv,axy,xref,yref, bgcolor=1,showarrow=True):
        if bgcolor==1:
            bgc=self.line_color3
        elif bgcolor==2:
            bgc=self.ann_bg_color4
        elif bgcolor==3:
            bgc=self.ann_bg_color3
        elif bgcolor==4:
            bgc=self.ann_bg_color4


        fig.add_annotation(
        x=x,
        y=y,
        xref=xref,
        yref=yref,
        text=text,
        showarrow=showarrow,
        font=dict(
            family="Courier New, monospace",
            size=12, 
            color=self.ann_text_color
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1,
        arrowcolor=self.ann_arrow_color,
        ax=axv,
        ay=axy,
        bordercolor=self.ann_border_color,
        borderwidth=2,
        borderpad=4,
        bgcolor=bgc,
        opacity=0.8
        )

    def annotate_subplot_text(self,fig,x,y,text,axv,axy,xref,yref, bgcolor=1,showarrow=False):

        fig.add_annotation(
        x=x,
        y=y,
        xref=xref,
        yref=yref,
        text=text,
        showarrow=showarrow,
        font=dict(
            family="sans-serif",
            size=14, 
            color=self.line_color1
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=1,
        ax=axv,
        ay=axy,
        opacity=1
        )


    #Actual Plotting
    def plot_reviews_timeseries(self):
        df=self.pp_raw_hotel_data
        data1=df.groupby("date_stayed")[["review_score"]].mean()
        data2=df[df.good_review==1].groupby("date_stayed")[["review_score"]].sum()
        data3=df[df.good_review==0].groupby("date_stayed")[["review_score"]].sum()

        fig = make_subplots(rows=1, cols=2,
                            #vertical_spacing = 0.04,
        subplot_titles=("", ""))




        fig.add_trace(
            go.Scatter(x=data1.index, y=data1.review_score.tolist(),name="Review Score", 
                    line_color=self.line_color1, 
                    legendgroup=1,
                    showlegend=False,
                
                    #mode='lines+markers'
                    ),
                    row=1, col=1)

        fig.add_trace(
            go.Scatter(x=data2.index, y=data2.review_score.tolist(), name="Positive Reviews", 
                    #line_color=self.line_color2, 
                    #legendgroup=2,
                    fill='tozeroy',
                    #stackgroup=1
                    ),
                    row=1, col=2)


        fig.add_trace(
            go.Scatter(x=data3.index, y=data3.review_score.tolist(), name="Negative Reviews", 
                    #line_color=self.line_color3, 
                    #legendgroup=2,
                    fill='tozeroy',
                    #stackgroup=1
                    ),
                    row=1, col=2)



        fig.update_yaxes(showgrid=True, 
                        gridwidth=1, 
                        gridcolor="grey", 
                        griddash='dot',
                        zeroline=False)

        fig.update_xaxes(showgrid=False,zeroline=False)

        #bgcolor=self.bgcolor
        bgcolor="#FAFAF9"
        bgcolor="#F8FBFB"
        fig.update_layout(legend=dict(
            orientation="v",
            groupclick="toggleitem"
            ),
                title={
                        'text': "<b>Total Reviews from 2019-2022</b>",
                        'y':0.9,
                        'x':0.5,
                        'font_size':20,
                        'xanchor': 'center',
                        'yanchor': 'top'},
            #height=490, width=1300,
            #font_size=10,
            paper_bgcolor=bgcolor,#F8FBFB
            plot_bgcolor=bgcolor
            )

        self.annotate_subplot_text(fig,'2023-03-01',7.9,"<b>Average<br>Review<br>Score</b>",-50,0,"x1","y1")
        #fig.show(renderer="browser")
        fig.show(config=self.config)






#%%
if __name__=='__main__':
    #print("Hello")
    g=Graphs()
    g.plot_reviews_timeseries()




# %%
