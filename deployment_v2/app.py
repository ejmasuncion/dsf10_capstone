import streamlit as st
from streamlit_option_menu import option_menu

#st.set_option('deprecation.showPyplotGlobalUse', False)

#from pages import Pages
from charts_functions_compiled import charts

from _1_load_data import Load_Data
from _2_visuals import Graphs
from _2_chart_functions import Chart_Functions
from _2_visuals import Graphs
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from charts_functions_compiled import charts

import pickle
import json
import plotly.io as pio

dl=Load_Data()
cf=Chart_Functions()
g=Graphs()

df_og=dl.pp_raw_hotel_data()

#st.set_page_config (layout="wide")

list_of_pages = [
    "Title Page",
    "Clusters",
    "Dashboard",
    "Model"
]

# Left the inside blank so that it really looks like a navbar
icons = ['building' , 'person','bar-chart-fill', 'gear']
selection = option_menu("", list_of_pages, orientation='horizontal', icons=icons,
        styles={
        #"container": {"padding": "0!important", "background-color": "#fafafa"},
        "container": {"padding": "0!important", "background-color": "#448299"},
        #"icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#AB5474"},  ##eee
        "nav-link-selected": {"background-color": "#AB5474"},    
        })



if selection == "Title Page":
    st.markdown("<h1 style='text-align: center; font-size: 36px;'>TRAVEL LOG</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-size: 20px;color: lightgrey;'> \
                    <em>Harnessing the Power of Data for Business Decisions <br>in the Hotel Industry </em> </h3>"
                    , unsafe_allow_html=True)   




    image_path = "pictures/hotel_background_.svg" 
    #svg = st.svg_reader(image_path)
    st.image(image_path)
    st.markdown("----")
    st.markdown("Project Made By: Andres, Andre, Enrico, Karen, Karla")

    


elif selection == "Dashboard":
    
    st.markdown(
        """
        <style>
            /* Set the background color of the page */
            body {
                background-color: #346476;
            }

            /* Style the cards */
            .card {
                /* Set the card size and position */
                width: 140px;
                height: 140px;
                position: relative;

                /* Add a drop shadow and a border */
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
                border: 0px solid #346476;
                border-radius: 25px;

                /* Color*/
                background-color: #445899;

                /* Set the font and text color */
                font-family: Montserrat;
                color: #fff;

                /* Set the card to be horizontally aligned */
                display: inline-block;
                margin: 1em;
                
                
            }

            /* Style the card content */
            .card-content {
                /* Position the content in the center of the card */
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%);

                /* Add padding and text alignment */
                padding: 20px;
                text-align: center;
                

            }
        </style>
        """
        , unsafe_allow_html=True
    )

    # Use the markdown function to create the card elements
    st.markdown(
        """
        <div class="card ">
            <div class="card-content">
                <h1 style="font-size: 2em">7.55</h1>
                <p style="font-size: 0.8em">Average Review Rating</p>
            </div>
        </div>

        <div class="card">
            <div class="card-content">
                <h1 style="font-size: 2em">$2,000</h1>
                <p style="font-size: 0.8em">Average <br>Price</p>
            </div>
        </div>

        <div class="card">
            <div class="card-content">
                <h1 style="font-size: 2em">4.5</h1>
                <p style="font-size: 0.8em">Average Star Rating</p>
            </div>
        </div>

        <div class="card">
            <div class="card-content">
                <h1 style="font-size: 2em">304</h1>
                <p style="font-size: 0.8em">Total Hotels</p>
            </div>
        </div>
        """
        , unsafe_allow_html=True
    )

    col1, col2= st.columns([0.3,0.7], gap="small")
    
    with col1:
        mapping_dict={1:"Good Review",0: "Bad Review"}
        countries_to_include = ["Philippines"]



        list_for_data=cf.categorical_eda_plots_plotly(df_og,"from_country",
                                            target_mapping=mapping_dict,
                                            column_mapping_list=countries_to_include,others_name="Foreign",
                                            hue="good_review", 
                                            time_series=False,  
                                            #ax=ax1,
                                            )


        data1,data2,data3,order,order_green, order_red=list_for_data
        fig = make_subplots(rows=1, cols=1,
                            #vertical_spacing = 0.04,
        subplot_titles=(""))


        #x=data1.rename(index={"Philippines":'Local'}).index
        fig.add_trace(go.Bar(x=data3.rename(index={"Philippines":'Local'}).index, y=data3[data3.columns[0]].values.tolist(),name="", opacity=0.8, marker_color="white",showlegend=False,),row=1, col=1)
        fig.add_trace(go.Bar(x=data1.rename(index={"Philippines":'Local'}).index, y=data1[data1.columns[0]].values.tolist(),name="Good", opacity=0.9, marker_color="#448299",showlegend=False,),row=1, col=1)
        fig.add_trace(go.Bar(x=data2.rename(index={"Philippines":'Local'}).index, y=data2[data2.columns[0]].values.tolist(),name="Bad", opacity=0.9, marker_color="#AB5474",showlegend=False,),row=1, col=1)


        #cf.layout_v1(fig,"Local vs Foreign<br>Comparing Proportions (%)",400,400,order)
        #g.annotate_subplot_text(fig,'Foreign',65,"55%",0,0,"x1","y1",bgcolor="grey",)
        #g.annotate_subplot_text(fig,'Philippines',50.5,"45%",0,0,"x1","y1",bgcolor="grey",)

        new_order=[i.replace('Philippines', 'Local') for i in order]
        cf.update_layout(fig,"Comparing Proportions",180,500,bgcolor="#2D3B6A",font_color="white",title_font_size=15,show_ygrid=False)
        cf.update_layout_order(fig,new_order)
        cf.update_layout_legend(fig,0.25,-0.15,orientation="h")
        cf.update_layout_margin(fig,20,0,0,50)
        st.plotly_chart(fig, use_container_width=True)

        # Stacked Histplot (Compare Proportions)
        mapping_dict={1:"Good Review",0: "Bad Review"}
        countries_to_include = ["Philippines"]



        list_for_data=cf.categorical_eda_plots_plotly(df_og,"occupant_type",
                                            target_mapping=mapping_dict,
                                            #column_mapping_list=countries_to_include,
                                            hue="good_review", 
                                            time_series=False,  
                                                )

        data1,data2,data3,order,order_green, order_red=list_for_data


        df_ns=df_og.copy()
        df_ns["nights_stayed"]=df_ns["nights_stayed_"].apply(lambda x: str(x))

        mapping_dict={1:"Good Review",0: "Bad Review"}
        values_to_include = ["1","2","3"]



        list_for_data=cf.categorical_eda_plots_plotly(df_ns,"nights_stayed",
                                            target_mapping=mapping_dict,
                                            column_mapping_list=values_to_include,others_name="4+",
                                            hue="good_review", 
                                            time_series=False,  
                                            )

        data1_,data2_,data3_,order_,order_green_, order_red_=list_for_data


        fig = make_subplots(rows=1, cols=2,
                            #vertical_spacing = 0.04,
        subplot_titles=("Traveller","Nights"))

        fig.add_trace(go.Bar(x=data3.rename(index={"Solo traveler": "Solo"}).index, y=data3[data3.columns[0]].values.tolist(),name="", opacity=0.8, marker_color="white",showlegend=False,),row=1, col=1)
        fig.add_trace(go.Bar(x=data1.rename(index={"Solo traveler": "Solo"}).index, y=data1[data1.columns[0]].values.tolist(),name="Good", opacity=0.9, marker_color="#448299",showlegend=False,),row=1, col=1)
        fig.add_trace(go.Bar(x=data2.rename(index={"Solo traveler": "Solo"}).index, y=data2[data2.columns[0]].values.tolist(),name="Bad", opacity=0.9, marker_color="#AB5475",showlegend=False,),row=1, col=1)


        fig.add_trace(go.Bar(x=data3_.index, y=data3_[data3_.columns[0]].values.tolist(),name="", opacity=0.8, marker_color="white",showlegend=False,),row=1, col=2)
        fig.add_trace(go.Bar(x=data1_.index, y=data1_[data1_.columns[0]].values.tolist(),name="Good", opacity=0.9, marker_color="#448299",showlegend=False,),row=1, col=2)
        fig.add_trace(go.Bar(x=data2_.index, y=data2_[data2_.columns[0]].values.tolist(),name="Bad", opacity=0.9, marker_color="#AB5475",showlegend=False,),row=1, col=2)


        new_order=[i.replace("Solo traveler", "Solo") for i in order]
        cf.update_layout(fig,"",180,500,bgcolor="#2D3B6A",font_color="white",font_size=10,show_ygrid=False,title_font_size=1,title_y=0.93)
        cf.update_layout_order(fig,order_)
        fig.update_xaxes(categoryorder='array', categoryarray=new_order, row=1,col=1 )
        fig.update_xaxes(categoryorder='category ascending',row=1,col=2)
        #cf.update_layout_legend(fig,0.5,-1,orientation="v")
        cf.update_layout_margin(fig,20,0,50,20)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig=g.plot_reviews_timeseries_v2(line_color1="#448299",line_color2="#AB5474",height=450,width=500)
        cf.update_layout_legend(fig, 0.15,1)
        cf.update_layout_margin(fig,80,40,100,80)
        st.plotly_chart(fig, use_container_width=True) 

        
    #col1_, col2_= st.columns([0.7,0.3], gap="small")

    #with col1_:
    pio.renderers.default = 'iframe'
    ncr_cities = json.load(open('../all_charts/data/MetropolitantManila.json', 'r'))


    cities_map = {}
    for feature in ncr_cities['features']:
        feature['id'] = feature['properties']['ID_2']
        cities_map[feature['properties']['NAME_2'].replace(" City","")] = feature['id']
        
    cities_map['Las Piñas'] = cities_map['Las PiÃ±as']
    del cities_map['Las PiÃ±as']

    cities_map['Parañaque'] = cities_map['ParaÃ±aque']
    del cities_map['ParaÃ±aque']



    df_for_mapping=pickle.load(open("../data/df_for_mapping_2.pkl", "rb"))


    map_column='Review_Rating'


    # colorscale_ = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
    #     "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
    #     "#08519c", "#0b4083", "#08306b"
    # ]

    colorscale_ = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef","#8fbdce","#6ca8be",g.navy_green,
    ]

    colorscale_ = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef","#8fbdce","#6ca8be",g.navy_green,g.maroon,
    ]

    option = st.selectbox(
    'Select Filter For Map',
    ('Review_Rating', 'Price', 'Nearby_Attractions','Nearest_Resto_Bar','Nearest_Subway','Nearest_Airport',
    "Nearest_Ocean","Total_Hotels"))

    fig = px.choropleth(df_for_mapping, 
                        locations = 'id', 
                        geojson = ncr_cities, 
                        #color = 'avg_price',
                        color = option,
                        hover_name = 'city',
                        color_continuous_scale=colorscale_,

                    hover_data = ['Review_Rating',"Price","Total_Hotels"],
                    )





    fig.update_geos(fitbounds = 'locations', visible = False)

    #445899- light blue
    #384C83- Best fit
    #deebf7 Light Grey
    #1e2746 Darker blue
    cf.update_layout(fig,"Manila Hotels-<br> Mapped by {}".format(option),400,700,bgcolor="#384C83",font_color="white",show_ygrid=False,
                        font_size=15,title_font_size=22,title_x=0.4,title_y=0.93)
    cf.update_layout_margin(fig,0,0,0,0)

    fig.update_layout(geo=dict(bgcolor= 'rgba(0,0,0,0)'))
    #fig.update_layout(height=550, margin={"r":0,"t":0,"l":0,"b":0})

    fig.update_layout(
        title_font_family="Montserrat",
        #title_font_color=g.maroon,
    )
    fig.update_traces(marker_line_color='grey', marker_line_width=1)
    

    st.plotly_chart(fig, use_container_width=False) 
        

    
elif selection == "Clusters":
    st.markdown("<h1 style='text-align: center; font-size: 28px;'>Customer Segmentation</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; font-size: 15px;color: lightgrey;'> \
                <em>-Using K-Means<br>Prototype</em> </h3>"
                , unsafe_allow_html=True) 
    st.markdown("<h3 style='text-align: left; font-size: 20px;color: lightgrey;'><u>5 Clusters</u>:</h3>",unsafe_allow_html=True)
    st.markdown("""---""")
    #st.text("")
    #st.text("")
    

    col1,col2,col3=st.columns(3) 
    with col1:
        st.write("1. Solo Traveler")  
        st.image("pictures/solo_traveler_icon_.svg", use_column_width=True,) 
        st.image("pictures/solo_traveler_info.png", use_column_width=True) 
    with col2:
        st.write("2. Low Budget Couple")
        st.image("pictures/low_budget_couple_iconv2_.svg", use_column_width=True,) 
        st.image("pictures/low_budget_couple_info.png", use_column_width=True) 
    with col3:
        st.write("3. Mid Budget Couple")
        st.image("pictures/mid_budget_couple_icon_.svg", use_column_width=True,) 
        st.image("pictures/mid_budget_couple_info.png", use_column_width=True) 

    st.text("")
    st.text("")

    col1,col2,col3,col4=st.columns([0.12,0.38,0.38,0.12],gap="large") 
    with col1:
        pass
    with col2:
        st.write("4. Mid Budget Family")
        st.image("pictures/mid_budget_family_icon_.svg", use_column_width=True,)
        st.image("pictures/mid_budget_family_info.png", use_column_width=True) 
    with col3:
        st.write("5. High Budget Family")
        st.image("pictures/high_budget_family_icon_.svg", use_column_width=True,)
        st.image("pictures/high_budget_family_info.png", use_column_width=True) 
    with col4:
        pass
            

    
elif selection == "Model":
    #Pages.page_four()
    pass

