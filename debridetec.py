from datetime import datetime
import keras
from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import streamlit as st
import numpy as np
import glob
import pandas as pd
import tensorflow as tf
from PIL import Image, ImageOps

from datetime import date
from st_btn_select import st_btn_select

selection = st_btn_select(('CHECK YOUR DEBRIS', 'ABOUT OUR APP','DEBRIS TYPE INFO', 'CLEANUP TIPS',  'CONTACT US'))



    

if selection == 'CHECK YOUR DEBRIS':
  
    import base64
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"PNG"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('beachbackground.jpg')    
      

                              
    st.markdown(""" <style> .font {
    font-size:50px ; font-weight: 800; color: #2e0a06; background-color: #ff958a;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font"> DebriDetec</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font2 {
    font-size:20px; color: ##0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Created by Julia & Justin Huang</p>', unsafe_allow_html=True)
    
    
   


 


    

    st.markdown(""" <style> .font3 {
    font-size:35px ; font-weight: 600; color: #ff958a; background-color: #FFF8F6;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">Classify and detect your debris/trash via AI technology: receive a quick & convenient result within seconds!</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font5 {
    font-size:25px ; font-weight: 600; color: #2e0a06; } 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font5">Instructions</p>', unsafe_allow_html=True)
    st.markdown('<p class="font2">Walk into any outside area, such as a beach, sidewalk, city street, etc. and once you find a bottle, container, plastic wrapping, or soda can, take a picture of it and then click the button below to upload your image. See the Debris Type Info tab for more info on the types of trash DebriDetec detects.</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="font5">Upload Trash/Debris Image Below:</p>', unsafe_allow_html=True)
    image = st.file_uploader(label = " ", type = ['png','jfif', 'jpg', 'jpeg', 'tif', 'tiff', 'raw', 'webp'])
       
    predictionText = "Prediction: Waiting for an image upload"
    def import_and_predict(image_data, model):
        size = (256, 256)
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        img = tf.keras.utils.img_to_array(image)
        img = tf.expand_dims(img, 0)
        probs = model.predict(img)
        score = tf.nn.softmax(probs[0])
        text = ("DebriDetec predicts that this is an image of **{}."
        .format(class_names[np.argmax(score)], 100 * np.max(score)))
        return text

    
  

    loaded_model = tf.keras.models.load_model('model.h5')
    class_names = [
    'BOTTLES',
    'CANS',
    'CONTAINERS',
    'PLASTIC']
    
    if image is not None:
        st.image(image)
        predictionText = (import_and_predict(Image.open(image), loaded_model))

    st.markdown(predictionText)   
    st.subheader('Count # items collected so far')
    
    st.markdown('<p class="font2">Note: we use this information in order to keep track of how many items of trash were scanned so we can also send this information to organizations and data scientists to detect any patterns in amount and type of trash in a certain area. For each image you scan into our web app, click the corresponding button to add the correct image type to our system. </p>', unsafe_allow_html=True)
    
   
    if 'p_count' not in st.session_state:
        st.session_state.p_count = 20
    if 'b_count' not in st.session_state:
        st.session_state.b_count = 18
    if 'c_count' not in st.session_state:
        st.session_state.c_count = 25
    if 'co_count' not in st.session_state:
        st.session_state.co_count = 14
        

    p_increment = st.button('Add Plastic')
    if p_increment:
        st.session_state.p_count += 1
        
    b_increment = st.button('Add Bottles')
    if b_increment:
        st.session_state.b_count += 1  
        
    c_increment = st.button('Add Cans')
    if c_increment:
        st.session_state.c_count += 1
    co_increment = st.button('Add Containers')
    if co_increment:
        st.session_state.co_count += 1

  
    
    todays_date = date.today()
    st.subheader('Amount of Items Detected since: ')
    st.write(todays_date)
    st.write('Number of Plastics: ', st.session_state.p_count)
    st.write('Number of Bottles: ', st.session_state.b_count)
    st.write('Number of Cans since: ', st.session_state.c_count)
    st.write('Number of Containers: ', st.session_state.co_count)
   
    
    
    
    


    
    
    #st.markdown('<p class="font2">predictionText</p>', unsafe_allow_html=True)
    st.markdown(""" <style> .fontSub {
    font-size:30px ; font-weight: 800; color: #2e0a06; background-color: #ff958a;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="fontSub"> Providing More Info On Uploaded Image</p>', unsafe_allow_html=True)
    with st.form(key="form1"):
        st.subheader("Debris Type")
        debris = ('Select a debris type', 'can', 'bottle', 'container', 'plastic')
        actual_type = st.selectbox("Select the debris type you think the image is:", debris)
        predicted_type = st.selectbox("Select the debris type the model predicted it as:", debris)

        st.subheader("Location")
        countries = ('Select a country', 'Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'Vietnam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe')
        states = ("Select a state", "Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming")
        country = st.selectbox("Select the country where the image was taken:", countries)
        if country == 'United States':
            state = st.selectbox('Select the state where the image was taken:', states)
        city = st.text_area("Provide the city/town where the image was taken, if known. Otherwise, put N/A:")
        area = st.text_area("Best describe the area in which the image was taken (ex: road, city street, sidewalk, beach, etc.):")

        st.subheader("Date")
        st.date_input("Select the date the image was taken on:", max_value = date.today())

        st.subheader("Personal Information")
        st.markdown("This is for in case any receiving cleanup organizations have questions about your submission and need to contact you for further information or questions.")
        last_name = st.text_input("Last Name:")
        first_name = st.text_input("First Name:")
        birth_date = st.date_input("Date of Birth:", min_value = date(1900, 1, 1), max_value = date.today())
        email_address = st.text_input("Email Address:")
        phone_number = st.text_input("Phone Number:")
        submit = st.form_submit_button(label="Submit")    
    if submit:

        st.write("**Your information provided has been sent to DebriDetec creators, who will then evaluate and analyze it before sending it over to cleanup organizations.**")
 

    
if selection == 'ABOUT OUR APP':
    import base64
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"PNG"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('beachbackground.jpg')    
    
    st.markdown(""" <style> .font {
    font-size:50px ; font-weight: 800; color: #ff958a; background-color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About DebriDetec</p>', unsafe_allow_html=True)

    st.image("debrideteclogo.png", width = 170)
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">About the Creators</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">The web app, dataset, and AI model are built by Julia and Justin Huang, passionate high school coders.</p>', unsafe_allow_html=True)
  
    
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">The Problem</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font3 {
    font-size:20px ;  color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">Due to the urgent problem of environmental pollution, according to nonprofits like Surfers Against Sewage and government agencies like the National Institute of Environmental Health Sciences, 8.3 billion plastic straws pollute beaches around the world, 100,000 marine animals are killed from plastic pollution annually, and 1 in 3 fish caught for human consumption contain microplastics. As human pollution negatively harms the environment, animals, and ourselves,  it is essential to spread awareness and encourage both individuals and organizations to help clean the beaches and other areas to rid of trash and debris. </p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Our Mission</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ;  color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">Therefore, the goal of DebriDetec is to provide individual citizens an opportunity to aid the cleanup process by using our app to clean up trash they see around them and provide information about trash they find to aid cleanup and environmental organizations and data scientists to determine conclusions and patterns about the type of trash in each area.</p>', unsafe_allow_html=True)
    
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">How DebriDetec was Built</p>', unsafe_allow_html=True)
    st.image("ProcessDiagram.png", caption='Diagram Detailing the Process of DebriDetec, from data input to web app deployment.')
    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">DebriDetec aims to make the data gathering process simpler and more convenient by utilizing AI & machine learning. DebriDetec has two parts: the AI model and web app. We built the AI model using the TensorFlow-Keras framework in the Python Language while the web app is built using Streamlit using HTMl/CSS formatting. We trained the model in Google Colab on a custom dataset we created consisting of 4 types of trash/debris sourced from the TACO dataset. After training and model evaluation, we converted the model into .h5 format and deployed the model into the web app with Streamlit. This web app is free and both mobile and web friendly for all users. </p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Future of DebriDetec</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">The accuracy of our CNN model is currently 90-95%, but we plan to improve the accuracy of the AI model even more. Besides sending data about trash to organizations, we also plan to partner with as many organizations and nonprofits as possible to maximize the impact of DebriDetec.</p>', unsafe_allow_html=True)
    
if selection == 'DEBRIS TYPE INFO':
    import base64
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"PNG"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('beachbackground.jpg')    
    
    st.markdown(""" <style> .font {
    font-size:50px ; font-weight: 800; color: #ff958a; background-color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Common Debris/Trash Types</p>', unsafe_allow_html=True)
   

    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">About Our Dataset</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">To train our AI model to detect different types of trash, we created 2 datasets based on the TACO dataset, labeling images of 4  of the most important debris types- cans, bottles, plastics, containers. Images were resized and rescaled to match our tasks and used as both training and testing. As you are on the lookout for trash, be sure to pay attention to the info about each type below.</p>', unsafe_allow_html=True)
  
    
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Cans</p>', unsafe_allow_html=True)
    st.image("cans.jpg", width = 250)
    st.markdown(""" <style> .font3 {
    font-size:20px ;  color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">These are mostly soda cans, with a smooth cylinder shape made of aluminum alloy.</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Bottles</p>', unsafe_allow_html=True)
    st.image("bottles.jpg", width = 250)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">These are mostly long, plastic bottles or wine bottles made of glass. </p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Containers</p>', unsafe_allow_html=True)
    st.image("container.jpg", width = 250)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">These are either styrofoam food containers or large cardboard containers.</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Plastics</p>', unsafe_allow_html=True)
    st.image("plastics.jpg", width = 250)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">These can be flat plastic bottle caps, food wrappings, or plastic chip bags. </p>', unsafe_allow_html=True)
if selection == 'CLEANUP TIPS':
    import base64
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"PNG"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('beachbackground.jpg')    
    
    st.markdown(""" <style> .font {
    font-size:50px ; font-weight: 800; color: #ff958a; background-color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Tips to Keep the Earth Clean</p>', unsafe_allow_html=True)
   

    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Use single-use items as less as possible.</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">When possible, invest in reusable items, such as water bottles, food containers, coffee mugs, silverware, etc. and bring them wherever you go instead of using plastic ones for example. </p>', unsafe_allow_html=True)
  
    
    
   
    st.markdown('<p class="font2">For the waste that you do have, make sure to dispose of them properly.</p>', unsafe_allow_html=True)

  
    st.markdown('<p class="font3">For example, recycle materials that are recyclable in your area and keep your lid on your garbage cans when taking them outside so nothing gets blown out.</p>', unsafe_allow_html=True)
    
  
    st.markdown('<p class="font2">Utilize composting.</p>', unsafe_allow_html=True)

    
    st.markdown('<p class="font3">Composting your food waste can help reduce the amount of garbage sent to landfills. To get started, gather an equal amount of browns and green organic materials - the brown provides carbon and the green provides nitrogen. This can be used as nutrients for plants to help them grow faster. </p>', unsafe_allow_html=True)
    
   
    st.markdown('<p class="font2">Reduce the amount of water you use on a daily basis.</p>', unsafe_allow_html=True)

    
    st.markdown('<p class="font3"> When not needed, turn off all faucets in your home, making sure they are turned off all the way with no dripping, as dripping over long periods of time can result in a ton of water being wasted. In addition, when you are cooking or doing other activities with water, instead of throwing away the excess water, use it to water your plants, clean your cars etc.</p>', unsafe_allow_html=True)
    
   
    st.markdown('<p class="font2">Make your travel habits more environmentally-friendly.</p>', unsafe_allow_html=True)

   
    st.markdown('<p class="font3"> If you are driving, try run errands (shopping, etc) at a time where there is less traffic so less gas can be wasted. In addition, try to plan and combine several trips into one to not only save gas but also save time. </p>', unsafe_allow_html=True)

   

  
    st.markdown('<p class="font2">Sources Used</p>', unsafe_allow_html=True)
    st.write("[NOAA](https://response.restoration.noaa.gov/about/media/8-ways-keep-earth-clean.html)") 
    st.write("[EPA](https://www.epa.gov/recycle/composting-home)") 
    st.write("[Green Child Magazine](https://www.greenchildmagazine.com/7-eco-friendly-tips-to-keep-the-environment-safe-and-clean/)") 
   
    
    
if selection == 'CONTACT US':
    import base64
    def add_bg_from_local(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"PNG"};base64,{encoded_string.decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    add_bg_from_local('beachbackground.jpg')    
    
    st.markdown(""" <style> .font {
    font-size:50px ; font-weight: 800; color: #ff958a; background-color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact PlantDoc Creators</p>', unsafe_allow_html=True)
   

    

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3"> Have a question? Feel free to contact us for questions, website bugs, or concerns.</p>', unsafe_allow_html=True)
  
    if st.button('Email Us'):

        st.write("[Click to send us an email](mailto:juliah6169@gmail.com)") #displayed when the button is clicked

    
         
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Other Information</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">Streamlit Website Developed By Julia and Justin Huang. Established since Summer/Fall 2022.</p>', unsafe_allow_html=True)

    
    
    if st.button('Subscribe to Our Newsletter'):

        st.write("[Click to subscribe](https://forms.gle/TGaYxoS68bRQrwzv5)") 
        
    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3"> Copyright © 2022 United States</p>', unsafe_allow_html=True)
