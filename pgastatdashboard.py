"""
PGA Statistics Dashboard Streamlit Webapp
"""
# Importing Section #

import streamlit as st
import pandas as pd

##########

# SQL setup
from sqlalchemy import create_engine
# connect to a local database
engine = create_engine("sqlite:///pgastats.db")



# Sidebar
golfer=st.sidebar.text_input("Enter Golfer's Name",'Rory McIlroy')

years=st.sidebar.slider('Select a range of years', 1950, 2022,(1960,2010),step=1)


years=list(range(years[0],years[1]+1))

st.sidebar.write('Years selected:',years[0],'to',years[-1])

scoring=st.sidebar.checkbox('Scoring')
driving=st.sidebar.checkbox('Driving')
approach=st.sidebar.checkbox('Approach')
chipping=st.sidebar.checkbox('Chipping')
putting=st.sidebar.checkbox('Putting')
money=st.sidebar.checkbox('Money')


# Webapp Title
st.title('PGA Tour Statistics Dashboard')




# Scoring Statistics
if scoring:
    st.header('Scoring')
    
    sg_total=st.checkbox('SG: Total')
    scoring_average=st.checkbox('Scoring Average')
    
    # SG: Total
    if sg_total:
        #import original table as dataframe from sql database
        df=pd.read_sql('SG: Total',engine)

        

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]

        
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVERAGE']=df['AVERAGE'].astype(float)

        


        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        

        # Rename the columns
        df.rename(columns={'AVERAGE':'SG: Total','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        
        
        
        st.subheader('SG: Total')
        
        
        st.write(df[['Tournament Number','SG: Total','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='SG: Total')

    # SG: Total
    if scoring_average:
        #import original table as dataframe from sql database
        df=pd.read_sql('Scoring Average',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG']=df['AVG'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'Scoring Average','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Scoring Average')
        
        st.write(df[['Tournament Number','Scoring Average','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Scoring Average')







# Driving Statistics
if driving:
    st.header('Driving')

    apex_height=st.checkbox('Apex Height')
    ball_speed=st.checkbox('Ball Speed')
    carry_distance=st.checkbox('Carry Distance')
    carry_efficiency=st.checkbox('Carry Efficiency')
    club_head_speed=st.checkbox('Club Head Speed')
    distance_to_apex=st.checkbox('Distance to Apex')
    driving_distance_all_drives=st.checkbox('Driving Distance - All Drives')
    hang_time=st.checkbox('Hang Time')
    hit_fairway_percentage=st.checkbox('Hit Fairway Percentage')
    launch_angle=st.checkbox('Launch Angle')
    sg_off_the_tee=st.checkbox('SG: Off-the-Tee')
    sg_tee_to_green=st.checkbox('SG: Tee-to-Green')
    smash_factor=st.checkbox('Smash Factor')
    spin_rate=st.checkbox('Spin Rate')
    total_distance_efficiency=st.checkbox('Total Distance Efficiency')

    # Apex Height
    if apex_height:
        #import original table as dataframe from sql database
        df=pd.read_sql('Apex Height',engine)

        #reverse the order of each column (original is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Apex Height String','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        # Convert the feet/inches to a float number
        for index,row in df.iterrows():
            string_length=row['Apex Height String']
            feet=float(string_length.split("'")[0])
            inches=float(string_length.split("'")[1].split("\"")[0])/12
            float_length=feet+inches
            df.loc[[index],['Apex Height (ft)']]=float_length


        st.subheader('Apex Height (ft)')
        
        st.write(df[['Tournament Number','Apex Height (ft)','Year','Time Period','Tournament']])
        

        st.line_chart(data=df,x='Tournament Number',y='Apex Height (ft)')

    # Ball Speed
    if ball_speed:
        #import original table as dataframe from sql database
        df=pd.read_sql('Ball Speed',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG.']=df['AVG.'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Ball Speed (mph)','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Ball Speed')
        
        st.write(df[['Tournament Number','Ball Speed (mph)','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Ball Speed (mph)')


    # Carry Distance
    if carry_distance:
        #import original table as dataframe from sql database
        df=pd.read_sql('Carry Distance',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG.']=df['AVG.'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Carry Distance (yd)','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Carry Distance')
        
        st.write(df[['Tournament Number','Carry Distance (yd)','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Carry Distance (yd)')


    # Carry Efficiency
    if carry_efficiency:
        #import original table as dataframe from sql database
        df=pd.read_sql('Carry Efficiency',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG.']=df['AVG.'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Carry Efficiency (yd/mph)','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Carry Efficiency')
        
        st.write(df[['Tournament Number','Carry Efficiency (yd/mph)','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Carry Efficiency (yd/mph)')


    # Club Head Speed
    if club_head_speed:
        #import original table as dataframe from sql database
        df=pd.read_sql('Club Head Speed',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG.']=df['AVG.'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Club Head Speed (mph)','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Club Head Speed')
        
        st.write(df[['Tournament Number','Club Head Speed (mph)','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Club Head Speed (mph)')

    # Distance to Apex
    if distance_to_apex:
        #import original table as dataframe from sql database
        df=pd.read_sql('Distance to Apex',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG.']=df['AVG.'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Distance to Apex (yd)','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Distance to Apex')
        
        st.write(df[['Tournament Number','Distance to Apex (yd)','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Distance to Apex (yd)')


    # Driving Distance - All Drives
    if driving_distance_all_drives:
        #import original table as dataframe from sql database
        df=pd.read_sql('Driving Distance - All Drives',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['ALL DRIVES']=df['ALL DRIVES'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'ALL DRIVES':'Driving Distance (yd)','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Driving Distance - All Drives')
        
        st.write(df[['Tournament Number','Driving Distance (yd)','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Driving Distance (yd)')

    # Hang Time
    if hang_time:
        #import original table as dataframe from sql database
        df=pd.read_sql('Hang Time',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG.']=df['AVG.'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Hang Time (s)','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Hang Time')
        
        st.write(df[['Tournament Number','Hang Time (s)','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Hang Time (s)')

    # Hit Fairway Percentage
    if hit_fairway_percentage:
        #import original table as dataframe from sql database
        df=pd.read_sql('Hit Fairway Percentage',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['%']=df['%'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'%':'Hit Fairway Percentage','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Hit Fairway Percentage')
        
        st.write(df[['Tournament Number','Hit Fairway Percentage','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Hit Fairway Percentage')


    # Launch Angle
    if launch_angle:
        #import original table as dataframe from sql database
        df=pd.read_sql('Launch Angle',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG.']=df['AVG.'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Launch Angle','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Launch Angle')
        
        st.write(df[['Tournament Number','Launch Angle','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Launch Angle')

    # SG: Off-the-Tee
    if sg_off_the_tee:
        #import original table as dataframe from sql database
        df=pd.read_sql('SG: Off-the-Tee',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVERAGE']=df['AVERAGE'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVERAGE':'SG: OTT','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('SG: Off-the-Tee')
        
        st.write(df[['Tournament Number','SG: OTT','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='SG: OTT')

    # SG: Tee-to-Green
    if sg_tee_to_green:
        #import original table as dataframe from sql database
        df=pd.read_sql('SG: Tee-to-Green',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVERAGE']=df['AVERAGE'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVERAGE':'SG: Tee-to-Green','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('SG: Tee-to-Green')
        
        st.write(df[['Tournament Number','SG: Tee-to-Green','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='SG: Tee-to-Green')

    # Smash Factor
    if smash_factor:
        #import original table as dataframe from sql database
        df=pd.read_sql('Smash Factor',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG.']=df['AVG.'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Smash Factor','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Smash Factor')
        
        st.write(df[['Tournament Number','Smash Factor','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Smash Factor')

    # Spin Rate
    if spin_rate:
        #import original table as dataframe from sql database
        df=pd.read_sql('Spin Rate',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]

        # Remove the commas
        df['AVG.']=df['AVG.'].str.replace(',','')
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG.']=df['AVG.'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Spin Rate (RPM)','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Spin Rate')
        
        st.write(df[['Tournament Number','Spin Rate (RPM)','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Spin Rate (RPM)')

    # Total Distance Efficiency
    if total_distance_efficiency:
        #import original table as dataframe from sql database
        df=pd.read_sql('Total Distance Efficiency',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG.']=df['AVG.'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG.':'Total Distance Efficiency (yd/mph)','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Total Distance Efficiency')
        
        st.write(df[['Tournament Number','Total Distance Efficiency (yd/mph)','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Total Distance Efficiency (yd/mph)')


# Approach Statistics
if approach:
    st.header('Approach')

    average_distance_to_hole_after_tee_shot=st.checkbox('Average Distance to Hole After Tee Shot')
    greens_in_regulation_percentage=st.checkbox('Greens in Regulation Percentage')
    proximity_to_hole=st.checkbox('Proximity to Hole')
    sg_approach_the_green=st.checkbox('SG: Approach the Green')
    
    # Average Distance to Hole After Tee Shot
    if average_distance_to_hole_after_tee_shot:
        #import original table as dataframe from sql database
        df=pd.read_sql('Average Distance to Hole After Tee Shot',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG']=df['AVG'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'ADTHATS (yd)','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Average Distance to Hole After Tee Shot')
        
        st.write(df[['Tournament Number','ADTHATS (yd)','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='ADTHATS (yd)')

    # Greens in Regulation Percentage
    if greens_in_regulation_percentage:
        #import original table as dataframe from sql database
        df=pd.read_sql('Greens in Regulation Percentage',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['%']=df['%'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'%':'GIR %','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Greens in Regulation Percentage')
        
        st.write(df[['Tournament Number','GIR %','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='GIR %')

    # Proximity to Hole
    if proximity_to_hole:
        #import original table as dataframe from sql database
        df=pd.read_sql('Proximity to Hole',engine)

        #reverse the order of each column (original is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'Proximity to Hole String','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        # Convert the feet/inches to a float number
        for index,row in df.iterrows():
            string_length=row['Proximity to Hole String']
            feet=float(string_length.split("'")[0])
            inches=float(string_length.split("'")[1].split("\"")[0])/12
            float_length=feet+inches
            df.loc[[index],['Proximity to Hole (ft)']]=float_length


        st.subheader('Proximity to Hole (ft)')
        
        st.write(df[['Tournament Number','Proximity to Hole (ft)','Year','Time Period','Tournament']])
        

        st.line_chart(data=df,x='Tournament Number',y='Proximity to Hole (ft)')

    # SG: Approach the Green
    if sg_approach_the_green:
        #import original table as dataframe from sql database
        df=pd.read_sql('SG: Approach the Green',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVERAGE']=df['AVERAGE'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVERAGE':'SG: AppTG','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('SG: Approach the Green')
        
        st.write(df[['Tournament Number','SG: AppTG','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='SG: AppTG')




# Chipping Statistics
if chipping:
    st.header('Chipping')


    proximity_to_hole_arg=st.checkbox('Proximity to Hole (ARG)')
    sg_around_the_green=st.checkbox('SG: Around-the-Green')
    scrambling=st.checkbox('Scrambling')
    scrambling_average_distance_to_hole=st.checkbox('Scrambling Average Distance to Hole')

    # Proximity to Hole (ARG)
    if proximity_to_hole_arg:
        #import original table as dataframe from sql database
        df=pd.read_sql('Proximity to Hole (ARG)',engine)

        #reverse the order of each column (original is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG DTP':'Proximity to Hole (ARG) String','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        # Convert the feet/inches to a float number
        for index,row in df.iterrows():
            string_length=row['Proximity to Hole (ARG) String']
            feet=float(string_length.split("'")[0])
            inches=float(string_length.split("'")[1].split("\"")[0])/12
            float_length=feet+inches
            df.loc[[index],['Proximity to Hole (ARG) (ft)']]=float_length


        st.subheader('Proximity to Hole (ARG) (ft)')
        
        st.write(df[['Tournament Number','Proximity to Hole (ARG) (ft)','Year','Time Period','Tournament']])
        

        st.line_chart(data=df,x='Tournament Number',y='Proximity to Hole (ARG) (ft)')


    # SG: Around-the-Green
    if sg_around_the_green:
        #import original table as dataframe from sql database
        df=pd.read_sql('SG: Around-the-Green',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVERAGE']=df['AVERAGE'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVERAGE':'SG: ArTG','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('SG: Around-the-Green')
        
        st.write(df[['Tournament Number','SG: ArTG','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='SG: ArTG')

    # Scambling
    if scrambling:
        #import original table as dataframe from sql database
        df=pd.read_sql('Scrambling',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['%']=df['%'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'%':'Scrambling %','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Scrambling')
        
        st.write(df[['Tournament Number','Scrambling %','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Scrambling %')



    # Scrambling Average Distance to Hole
    if scrambling_average_distance_to_hole:
        #import original table as dataframe from sql database
        df=pd.read_sql('Scrambling Average Distance to Hole',engine)

        #reverse the order of each column (original is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG DTP':'Scrambling Average Distance to Hole String','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        # Convert the feet/inches to a float number
        for index,row in df.iterrows():
            string_length=row['Scrambling Average Distance to Hole String']
            feet=float(string_length.split("'")[0])
            inches=float(string_length.split("'")[1].split("\"")[0])/12
            float_length=feet+inches
            df.loc[[index],['Scrambling Average Distance to Hole (ft)']]=float_length


        st.subheader('Scrambling Average Distance to Hole (ft)')
        
        st.write(df[['Tournament Number','Scrambling Average Distance to Hole (ft)','Year','Time Period','Tournament']])
        

        st.line_chart(data=df,x='Tournament Number',y='Scrambling Average Distance to Hole (ft)')
    

# Putting Statistics
if putting:
    st.header('Putting')

    putts_per_round=st.checkbox('Putts per Round')
    one_putts_per_round=st.checkbox('1-Putts per Round')
    two_putts_per_round=st.checkbox('2-Putts per Round')
    three_putts_per_round=st.checkbox('3-Putts per Round')
    three_plus_putts_per_round=st.checkbox('3+ Putts per Round')
    average_putting_distance_all_1_putts=st.checkbox('Average Putting Distance - All 1 putts')
    average_putting_distance_all_2_putts=st.checkbox('Average Putting Distance - All 2 putts')
    average_putting_distance_all_3_putts=st.checkbox('Average Putting Distance - All 3 putts')
    putting_average=st.checkbox('Putting Average')
    sg_putting=st.checkbox('SG: Putting')

    # Putts per Round
    if putts_per_round:
        #import original table as dataframe from sql database
        df=pd.read_sql('Putts Per Round',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG']=df['AVG'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'Putts Per Round','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('1-Putts Per Round')
        
        st.write(df[['Tournament Number','Putts Per Round','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Putts Per Round')




    # 1-Putts per Round
    if one_putts_per_round:
        #import original table as dataframe from sql database
        df=pd.read_sql('1-Putts per Round',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG']=df['AVG'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'1PPR','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('1-Putts per Round')
        
        st.write(df[['Tournament Number','1PPR','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='1PPR')

    # 2-Putts per Round
    if two_putts_per_round:
        #import original table as dataframe from sql database
        df=pd.read_sql('2-Putts per Round',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG']=df['AVG'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'2PPR','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('2-Putts per Round')
        
        st.write(df[['Tournament Number','2PPR','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='2PPR')


    # 3-Putts per Round
    if three_putts_per_round:
        #import original table as dataframe from sql database
        df=pd.read_sql('3-Putts per Round',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG']=df['AVG'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'3PPR','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('3-Putts per Round')
        
        st.write(df[['Tournament Number','3PPR','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='3PPR')

    # 3+ Putts per Round
    if three_plus_putts_per_round:
        #import original table as dataframe from sql database
        df=pd.read_sql('3+ Putts per Round',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG']=df['AVG'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'3+PPR','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('3+ Putts per Round')
        
        st.write(df[['Tournament Number','3+PPR','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='3+PPR')

    # Average Putting Distance - All 1 putts
    if average_putting_distance_all_1_putts:
        #import original table as dataframe from sql database
        df=pd.read_sql('Average Putting Distance - All 1 putts',engine)

        #reverse the order of each column (original is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'Average Putting Distance - All 1 putts String','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        # Convert the feet/inches to a float number
        for index,row in df.iterrows():
            string_length=row['Average Putting Distance - All 1 putts String']
            feet=float(string_length.split("'")[0])
            inches=float(string_length.split("'")[1].split("\"")[0])/12
            float_length=feet+inches
            df.loc[[index],['Average Putting Distance - All 1 putts (ft)']]=float_length


        st.subheader('Average Putting Distance - All 1 putts (ft)')
        
        st.write(df[['Tournament Number','Average Putting Distance - All 1 putts (ft)','Year','Time Period','Tournament']])
        

        st.line_chart(data=df,x='Tournament Number',y='Average Putting Distance - All 1 putts (ft)')

    # Average Putting Distance - All 2 putts
    if average_putting_distance_all_2_putts:
        #import original table as dataframe from sql database
        df=pd.read_sql('Average Putting Distance - All 2 putts',engine)

        #reverse the order of each column (original is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'Average Putting Distance - All 2 putts String','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        # Convert the feet/inches to a float number
        for index,row in df.iterrows():
            string_length=row['Average Putting Distance - All 2 putts String']
            feet=float(string_length.split("'")[0])
            inches=float(string_length.split("'")[1].split("\"")[0])/12
            float_length=feet+inches
            df.loc[[index],['Average Putting Distance - All 2 putts (ft)']]=float_length


        st.subheader('Average Putting Distance - All 2 putts (ft)')
        
        st.write(df[['Tournament Number','Average Putting Distance - All 2 putts (ft)','Year','Time Period','Tournament']])
        

        st.line_chart(data=df,x='Tournament Number',y='Average Putting Distance - All 2 putts (ft)')

    # Average Putting Distance - All 3 putts
    if average_putting_distance_all_3_putts:
        #import original table as dataframe from sql database
        df=pd.read_sql('Average Putting Distance - All 3 putts',engine)

        #reverse the order of each column (original is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'Average Putting Distance - All 3 putts String','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        # Convert the feet/inches to a float number
        for index,row in df.iterrows():
            string_length=row['Average Putting Distance - All 3 putts String']
            feet=float(string_length.split("'")[0])
            inches=float(string_length.split("'")[1].split("\"")[0])/12
            float_length=feet+inches
            df.loc[[index],['Average Putting Distance - All 3 putts (ft)']]=float_length


        st.subheader('Average Putting Distance - All 3 putts (ft)')
        
        st.write(df[['Tournament Number','Average Putting Distance - All 3 putts (ft)','Year','Time Period','Tournament']])
        

        st.line_chart(data=df,x='Tournament Number',y='Average Putting Distance - All 3 putts (ft)')

    # Putting Average
    if putting_average:
        #import original table as dataframe from sql database
        df=pd.read_sql('Putting Average',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVG']=df['AVG'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVG':'Putting Average','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Putting Average')
        
        st.write(df[['Tournament Number','Putting Average','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Putting Average')

    # SG: Putting
    if sg_putting:
        #import original table as dataframe from sql database
        df=pd.read_sql('SG: Putting',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]
        
        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['AVERAGE']=df['AVERAGE'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'AVERAGE':'SG: Putting','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('SG: Putting')
        
        st.write(df[['Tournament Number','SG: Putting','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='SG: Putting')



# Money Statistics
if money:
    st.header('Money')
    
    career_earnings=st.checkbox('Career Earnings')

    # Career Earnings
    if career_earnings:
        #import original table as dataframe from sql database
        df=pd.read_sql('Career Earnings',engine)

        #reverse the order of each column ( is most recent to oldest, want oldest to most recent)
        df=df.iloc[::-1]

        # Remove the commas
        df['MONEY']=df['MONEY'].str.replace(',','')
        
        # Remove the $
        df['MONEY']=df['MONEY'].str.replace('$','')

        #Convert datatypes
        df['Year']=df['Year'].astype(int)
        df['MONEY']=df['MONEY'].astype(float)

        # Apply the filters and set new index numbers
        df=df[(df['PLAYER NAME']==golfer)&(df['Year'].isin(years))].reset_index(drop=True).reset_index()
        
        # Rename the columns
        df.rename(columns={'MONEY':'Career Earnings','index':'Tournament Number'},inplace=True)

        # Make tournament numbers make more sense
        df['Tournament Number']=df['Tournament Number']+1
        
        st.subheader('Career Earnings')
        
        st.write(df[['Tournament Number','Career Earnings','Year','Time Period','Tournament']])

        st.line_chart(data=df,x='Tournament Number',y='Career Earnings')
