## predict.py
import pandas as pd
import joblib
import os
from feature_engineering import add_features
from configuration import BASE_DIR
## we make the following predict method as will be called in main method
def predict(test_path, model_path):
    ## test path is separate as our test data is different and we have a separate hidden test dataset given to us by kaggle itself
    test_path = os.path.join(BASE_DIR, test_path)
    ## model path same as before idea, its in the base directory's subfolder src
    model_path = os.path.join(BASE_DIR, model_path)
    ## we load up the model
    model = joblib.load(model_path)
    ## read test data
    df_test = pd.read_csv(test_path)
    ## read the id numbers from the dataframe 
    ids = df_test["Id"] if "Id" in df_test.columns else None
    ## run it by feature engineerinh
    df_test = add_features(df_test)
    ## predict the values
    preds = model.predict(df_test)
    ## we now move on to making our submission file using data frames
    submission = pd.DataFrame({
        "Id": ids,
        "SalePrice": preds
    })
    ## output path is to define a directory to submission to kaggle website to
    output_path = os.path.join(BASE_DIR, "submission.csv")
    ## we convert the data frame into a new csv in  the given kaggle format for the sample submission file available on the page for the problem
    ## basically its just the index and sales price listed
    submission.to_csv(output_path, index=False)
    ## final update to user regarding the process completion
    print(f"Predictions saved to {output_path}")