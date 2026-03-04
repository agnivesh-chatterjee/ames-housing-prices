## configuration.py
## This function helps to centralize all the configuration settings for the project, making it easier to manage paths, parameters, and other constants in one place. This way, if you need to change any of these settings, you can do so in a single file without having to search through the entire codebase.
## I got the idea for creating this file from one of my seniors working on a model fitting project using XGBoost
import os
## Base directory of the project is set to the folder on my computer where I had stored the project files for my own personal storage/running the code.
## This way I can have my files more neatly organized under source code and data folders separately instead of it be a giant list of files like in my EDA project before this
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
## The data path is set to location of the training data csv file stored in the "data" subfolder.
DATA_PATH=os.path.join(BASE_DIR, "data", "train.csv")
## I just made the model directory a subfolder to have it be separate and be able to dump the trained model there without it being mixed with the source code files. It could have just been left there within the base directory with src and data subfolders 
MODEL_DIR = os.path.join(BASE_DIR, "models")
## our target column for prediction is obviosusly SalesPrice Column in the dataset
TARGET_COLUMN = "SalePrice"
## Set it to 26 because I like that number, nothing beyond that really
RANDOM_STATE = 26
