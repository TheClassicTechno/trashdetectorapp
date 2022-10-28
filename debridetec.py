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
    font-size:35px ; font-weight: 600; color: #ff958a; background-color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">Classify and detect your debris/trash via AI technology: receive a quick & convenient result within seconds!</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font5 {
    font-size:25px ; font-weight: 600; color: #2e0a06; } 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font5">Upload Trash/Debris Image Below:</p>', unsafe_allow_html=True)
    
    image = st.file_uploader(label = " ", type = ['png','jfif', 'jpg', 'jpeg', 'tif', 'tiff', 'raw', 'webp'])

    def import_and_predict(image_data, model):
        size = (256, 256)
        image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
        img = tf.keras.utils.img_to_array(image)
        img = tf.expand_dims(img, 0)
        probs = model.predict(img)
        score = tf.nn.softmax(probs[0])
        text = ("DebriDetec predicts that this is an image of **{} with {:.2f}% confidence**."
        .format(class_names[np.argmax(score)], 100 * np.max(score)))
        return text

    
  

    loaded_model = tf.keras.models.load_model('model.h5')
    class_names = [
    'bottles',
    'cans',
    'containers',
    'plastic']


    predictionText = "Prediction: Waiting for an image upload"

    if image is not None:
        st.image(image)
        predictionText = (import_and_predict(Image.open(image), loaded_model))

    st.markdown(predictionText)   
    
    #st.markdown('<p class="font2">predictionText</p>', unsafe_allow_html=True)
    st.markdown(""" <style> .fontSub {
    font-size:30px ; font-weight: 800; color: #2e0a06; background-color: #ff958a;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="fontSub"> Providing More Info On Uploaded Image</p>', unsafe_allow_html=True)
    
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
    submit = st.button("Submit")    
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
    st.markdown('<p class="font">About PlantDoc</p>', unsafe_allow_html=True)
   

    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">About the Creators</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">The web app and model are built by Julia and Justin Huang, high school coders.</p>', unsafe_allow_html=True)
  
    
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Mission</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ;  color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">Due to the high usage of pesticides, many plant diseases have become resilient and more common. In addition, farmers, especially those living in isolated or rural parts of the world, may not know what or if a disease has affected their plant. Therefore it is essential to figure out what diseases are affecting plants so consumers do not get sick. So the goal of **Shoethentic** is to provide the farmers and gardeners an opportunity to check the conditions of each and every plant they tend to. **Shoethentic** aims to make this checking process simpler and more convenient by utilizing AI & machine learning.</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">How PlantDoc was Built</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">PlantDoc has two parts: the AI model and web app. The AI model is built using the TensorFlow framework in the Python Language while the web app is built using Streamlit using HTMl/CSS formatting. We trained the model in Google Colab on a dataset consisting of 15 types of plant conditions sourced from the PlantVillage dataset on Kaggle and deployed the model into the web app with Streamlit.</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Future of PlantDoc</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">The accuracy of our CNN model is currently 92%, but we plan to improve the accuracy of the AI model even more. We also plan to partner with agricultural businesses so we can test out the app with farmers.</p>', unsafe_allow_html=True)
    
    
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
    st.markdown('<p class="font">About Common Plant Disease + How to Prevent Them</p>', unsafe_allow_html=True)
   

    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">About the Creators</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">The information page states relevant information for gardeners and farmers about the details of each disease and tips on how to prevent disease when growing plants. </p>', unsafe_allow_html=True)
  
    
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Mission</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ;  color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">Due to the high usage of pesticides, many plant diseases have become resilient and more common. In addition, farmers, especially those living in isolated or rural parts of the world, may not know what or if a disease has affected their plant. Therefore it is essential to figure out what diseases are affecting plants so consumers do not get sick. So the goal of PlantDoc is to provide the farmers and gardeners an opportunity to check the conditions of each and every plant they tend to. PlantDoc aims to make this checking process simpler and more convenient by utilizing AI & machine learning.</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">How PlantDoc was Built</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #fffafa;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">PlantDoc has two parts: the AI model and web app. The AI model is built using the TensorFlow framework in the Python Language while the web app is built using Streamlit using HTMl/CSS formatting. We trained the model in Google Colab on a dataset consisting of 15 types of plant conditions sourced from the PlantVillage dataset on Kaggle and deployed the model into the web app with Streamlit.</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .font2 {
    font-size:30px ; font-weight: 600; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font2">Future of PlantDoc</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .font3 {
    font-size:20px ; color: #0a0302;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font3">The accuracy of our CNN model is currently 92%, but we plan to improve the accuracy of the AI model even more. We also plan to partner with agricultural businesses so we can test out the app with farmers.</p>', unsafe_allow_html=True)
    
    
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
