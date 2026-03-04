## preprocessing.py
## I performed rather standard preprocessing steps here. Passed the numeric features through the simple imputer, replacing nul/na values with the median as house prices do have some really high values which can skew the mean 
## And ofcourse I use OneHotEncoder for the categorica features. I also use the handle_unknown="ignore" parameter to ensure that if there are any categories in the test set that were not present in the training set, the encoder will simply ignore them instead of throwing an error.
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
def create_preprocessor(X):
    ## we group numeric and categorical features separately to apply the different transformations to them.
    numeric_features = X.select_dtypes(include=["int64", "float64"]).columns
    ## I could have used include and exclude parameters here but I decide to use include for int and float to be more explicit
    categorical_features = X.select_dtypes(include=["object"]).columns
    ## We use the pipeline function to "guide" our features through the changes we wish to apply to them
    numeric_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ])
    ## We thwn create a separate pipeline for categorical variable processing by replacing unknown values with mpost frequently occuring category and one hot encoding
    categorical_pipeline = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])
    ## Now that we have defined our pipelines for numeric and categorical features, we define our preprocessor method by having be an object of class Column Transformer where categorical feature columns are transformed using categorical pipeline and same for numerical features
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_pipeline, numeric_features),
            ("cat", categorical_pipeline, categorical_features)
        ]
    )
    ## we return the preprocessor (column transformer object) that will then be used in our final pipeline for the data
    return preprocessor