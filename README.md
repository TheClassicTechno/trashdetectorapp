# DebriDetec: Trash and Debris Detector App

Bringing individuals and communities together to decrease environmental pollution around the world by utilizing AI. <br>
Created by Julia and Justin Huang

# Benefits
- Our app utilizes the latest technology, including AI <br>
- Our AI model is 95% accurate for 4 different debris types <br>
- Our web app is both mobile and web friendly for all users around the world <br>
- Our solution is free for individuals <br>

# What this Github Repo Includes
- Model (.h5 format) <br>
- Streamlit web app (Python file) <br>
- Model training, accuracy results, and data processing (Jupyter Notebook file) <br>
- Process Diagram of How We Built our Product (PNG format) <br>
- Try out our web app here: https://theclassictechno-trashdetectorapp-debridetec-ekpzzi.streamlitapp.com/

# About Our Model
Our model classifies four of the most common and critical types of trash, debris, etc. from the TACO Custom dataset, which we adapted/sourced from the original Taco dataset. This original Taco dataset was created for object detection, so we modified it to be used for classification. See original Taco dataset (1.6K images) here: http://tacodataset.org/

Our Cleansea Model was trained and optimized to reach >95% accuracy consistently on Taco Custom 1.0 and ~90% accuracy consistently on Taco Custom 2.0 (bigger dataset). Of course, due to the time-consuming work of relabeling data and adding augmentations to increase dataset size, our custom Taco datasets are smaller than the original Taco dataset.

# About Our Datasets 
TACO Custom dataset published on Kaggle: https://www.kaggle.com/datasets/julesh7/taco-dataset-revised-230-imgs

TACO Custom 2.0 dataset published on Kaggle: https://www.kaggle.com/datasets/julesh7/taco-dataset-revised-922-imgs

To create these 2 datasets, we labeled images of 4 important debris types and placed original TACO dataset files into four folders - cans, bottles, plastics, containers. Images were resized and rescaled to match our tasks. In addition, we performed data cleaning due to noisy images and images that contained two classes. Further, we performed data augmentations such as rotations to increase amount of data. Note: there are not many publicly available ocean debris datasets - the most comprehensive one we could find was TACO.
