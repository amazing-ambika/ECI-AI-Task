import streamlit as st
import pandas as pd
import plotly.express as plx
from streamlit_option_menu import option_menu
import random


st.set_page_config(layout="wide",page_title='Election Results')
#st.image("./eci.jpg", width = 80)

# Create two columns
col1, col2 = st.columns([1, 20])

# Display an image in the first column
with col1:
    st.image('./eci.jpg', width=80)

# Display text in the second column
with col2:
    st.header('Election Commission Of India')

#st.markdown('<h1 style="float: right;">Election Commission of India</h1><img style="float: right;" src="./eci.jpg" />', unsafe_allow_html=True)
# st.write('Election Commission of India')

#with open("designing.css") as source_des:
 #   st.markdown(f"<style>{source_des.read()}</style>", unsafe_allow_html=True)

st.markdown("<div style = 'background-color:#e1eb34';'>Disclaimer: ECI is displaying the information as being filled in the system by the Returning Officers from their respective Counting Centres. The final data for each AC/PC will be shared in Form-20.</div>", unsafe_allow_html=True)



st.write("")



tab = option_menu(None, ["Parliament Constituency General", "Assembly Constituency General", "Assembly Constituency Bye"], orientation="horizontal", styles={
        "container": {"padding": "10!important", "background-color": "red"},
        "icon": {"color": "white", "font-size": "25px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "color": "white",
            "background-color": "red",
        },
        "nav-link-selected": {"background-color": "darkred"},
    }
)
if tab == 'Parliament Constituency General':
    col1, col2 = st.columns([2, 3])

    with col1:
        st.markdown('General Election to Parliamentary Constituencies: Trends & Results June-2024 :')

    with col2:
        options = ["Select State Wise", 
               "Andaman & Nicobar Islands", "Andhra Pradesh", "Arunachal Pradesh","Assam", "Bihar", 
               "Chandigarh", "Chhattisgarh", "Dadra & Nagar Haveli and Daman & Diu", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Ladakh", "Lakshadweep", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "NCT OF Delhi", "Odisha", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
        selected_option = st.selectbox('Select State Wise', options)
    col3, col4, col5 = st.columns([3, 4, 1])
    with col3:
        st.empty()
    with col4:
        first_data = pd.read_csv('chartgauging.csv')
        second_data = pd.read_csv('tablepage1.csv')
        color_discrete_map = {
    "Bharatiya Janata Party - BJP": "#ff8331",
    "Indian National Congress - INC": "#17aaed",
    "Samajwadi Party - SP": "#ff0000",
    "All India Trinamool Congress - AITC": "#aebedf",
    "Dravida Munnetra Kazhagam - DMK": "#o5f89e",
    "Telugu Desam - TDP":"#204795",
    "Janata Dal  (United) - JD(U)":"#39ac57",
    "Shiv Sena (Uddhav Balasaheb Thackrey) - SHSUBT":"#61da8c",
    "Nationalist Congress Party - Sharadchandra Pawar - NCPSP":"#457a8b",
    "Shiv Sena ":"#d2691e",
    "Others":"#b3b3b3",
    "Total":"transparent"
    }
        fig = plx.pie(first_data, values=first_data['Won'], names=first_data['Party'], title='Votes Distribution by State',color='Party', color_discrete_map=color_discrete_map)
        fig.update_traces(hole=0.6, hoverinfo="label+name", sort=False)
        fig.update_layout(height=700, width=800)
        fig.update_traces(rotation=67)
        st.plotly_chart(fig)
    with col5:
        st.empty()


    col6,col7 = st.columns([3,3])
    with col6:
        st.subheader('Party Wise Vote Share')
        fig2 = plx.pie(second_data, values=second_data['Won'], names=second_data['Party'],color='Party',labels=None)
        fig2.update_traces(hole=0.4, sort=False)
        fig2.update_layout(height=700, width=800)
        st.plotly_chart(fig2)

    with col7:
        st.subheader('Party Wise Results Status')
        st.dataframe(second_data,use_container_width=True,height=600,hide_index=True)

elif tab == 'Assembly Constituency General':
    st.subheader('General Election to Assembly Constituencies: Trends & Results June-2024', divider='rainbow')

    andhra = ['TDP', 'JnP', 'YSRCP', 'BJP']
    wandhra = [135, 21, 11, 8]

    odi = ['BJP', 'BJD', 'INC', 'IND', 'CPI(M)']
    wodi = [78, 51, 14, 1, 3]

    col8, col9 = st.columns([2, 2])
    with col8:
        st.markdown(f"""
        <div style="background-color: teal; border: solid 2px teal; border-radius: 10px; overflow: hidden; max-width: 600px; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        <div style="background-color: white; color: teal;font-size:18.4px;font-weight:500; text-align: center; padding: 10px; border-bottom: solid 2px teal;">
            <b>Andhra Pradesh</b>
        </div>
        <div style="padding: 20px; color: white; display: flex; justify-content: space-between; align-items: center;">
            <p style="margin: 10px 0; font-size: 1.2em;">Assembly Constituencies</p>
            <p style="background-color: #2ab7d4; color: white; padding: 10px; font-size: 1.5em; border-radius: 5px; margin: 0;">175</p>
        </div>
            <p style="font-size:12px;color:white;padding-left:15px"> <b> *Status of Top Five Parties </b></p>
        <div style="background-color: white; padding: 20px; border-radius: 5px; margin-top: 20px;">
            <table style="width: 80%;color:black;border-collapse: collapse;">
                <tr style="text-align: left; padding: 8px; background-color: teal; color: white;">
                    <th style="text-align: left; padding: 12px;">Parties</th>
                    <th style="text-align: left; padding: 12px;">Leading/Won</th>
                </tr>
                <tr style="background-color: #f2f2f2;">
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{andhra[0]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wandhra[0]}</td>
                </tr>
                <tr>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{andhra[1]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wandhra[1]}</td>
                </tr>
                <tr style="background-color: #f2f2f2;">
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{andhra[2]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wandhra[2]}</td>
                </tr>
                <tr>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{andhra[3]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wandhra[3]}</td>
                </tr>
            </table>
        </div>
        <div style="text-align:center; margin-top:20px;margin-bottom:20px;">
    <button style="background-color:white;border-radius:7px; color: blue; padding: 10px 20px; border: 1px solid blue;">Details ></button>
</div>
    </div>
    """, unsafe_allow_html=True)
    with col9:
        st.markdown(f"""
            <div style="background-color: maroon; border: solid 2px maroon; border-radius: 10px; overflow: hidden; max-width: 600px; margin: 0 auto; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
            <div style="background-color: white;font-size:18.4px;font-weight:500 ;color: maroon; text-align: center; padding: 10px; border-bottom: solid 2px maroon;">
            <b>Odisha</b>
            </div>
            <div style="padding: 20px; color: white; display: flex; justify-content: space-between; align-items: center;">
            <p style="margin: 10px 0; font-size: 1.2em;">Assembly Constituencies</p>
            <p style="background-color: #ab391d; color: white; padding: 10px; font-size: 1.5em; border-radius: 5px; margin: 0;">147</p>
            </div>
            <p style="font-size:12px;color:white;padding-left:15px">  <b>*Status of Top Five Parties</p>
            <div style="background-color: white; padding: 20px; border-radius: 5px; margin-top: 20px;">
                <table style="width: 100%;color:black;border-collapse: collapse;">
                    <tr style="text-align: left; padding: 8px; background-color: maroon; color: white;">
                    <th style="text-align: left; padding: 12px;">Parties</th>
                    <th style="text-align: left; padding: 12px;">Leading/Won</th>
                    </tr>
                    <tr style="background-color: #f2f2f2;">
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{odi[0]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wodi[0]}</td>
                    </tr>
                <tr>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{odi[1]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wodi[1]}</td>
                </tr>
                <tr style="background-color: #f2f2f2;">
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{odi[2]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wodi[2]}</td>
                </tr>
                <tr>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{odi[3]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wodi[3]}</td>
                </tr>
                <tr>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{odi[4]}</td>
                    <td style="text-align: left;font-size:13.6px;font-weight:600; padding: 12px;">{wodi[4]}</td>
                </tr>
            </table>
        </div>
    <div style="text-align:center; margin-top:20px;margin-bottom:20px">
    <button style="background-color: white;border-radius:7px; color: blue; padding: 10px 20px; border: 1px solid blue;">Details ></button>
    </div>
    </div>
    """, unsafe_allow_html=True)
        


elif tab == 'Assembly Constituency Bye':
    st.write('Disclaimer: ECI is displaying the information as being filled in the system by the Returning Officers from their respective Counting Centres. The final data for each AC/PC will be shared in Form-20.')
    st.header('Bye Election to Assembly Constituencies: Results June-2024', divider='green')

    data = pd.read_csv('lastpage.csv')

# Allocating the colors for each of the parties
    party_colors = {
    "Bharatiya Janata Party": "#488cfa",
    "All India Trinamool Congress": "yellow",
    "Communist Party of India  (Marxist-Leninist)  (Liberation)": "orange",
    "Indian National Congress": "pink",
    "Jharkhand Mukti Morcha":"purple",
    "Samajwadi Party":"linen",
    "Bharat Adivasi Party":"green"

}
    
    def random_color():
        return "#{:02x}{:02x}{:02x}".format(random.randint(128, 255), random.randint(128, 255),  random.randint(128, 255))    

    num_columns = 4
    num_rows = (len(data) + num_columns - 1) // num_columns 

    for i in range(num_rows):
        columns = st.columns(num_columns)
        for j in range(num_columns):
            index = i * num_columns + j
            if index < len(data):
                cityname, statename, result, particpantname, partyname = data.iloc[index]
                color = party_colors.get(partyname)
                participant_color = random_color()
                with columns[j]:
                    st.markdown(
                    f"""
                    <div style="padding: 20px; margin: 10px;border-radius: 15px; box-shadow:  0 4px 12px rgba(0, 0, 0, 0.2); border: solid {color} 4px;">
                        <p style="color:#004274;font-size:40px;text-align:center;font-weight:700"><b>{cityname}</b></p>
                        <p style="color:#0187ec;font-size:20px;text-align:center;font-weight:500">{statename}</p>
                        <p style="color:#02a560;font-size:29.6px;text-align:center;font-weight:700">{result}</p>
                        <p style="text-align:center;font-size:21.6px;font-weight:500;color:{participant_color}">{particpantname}</p>
                        <p style="color:#73aafe;font-size:16px;text-align:center;font-weight:500">{partyname}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                with columns[j]:
                    st.empty()


