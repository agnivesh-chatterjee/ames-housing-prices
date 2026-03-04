## main.py
## we import all the necessary methods from the remaining files
from data_loader import load_data
from feature_engineering import add_features
from train import train_model
from predict import predict

## Idk what to say main method where it all comes together
def main():
    ## real time updates when the main method runs
    ## we load data first
    print("Loading training data...")
    df=load_data()
    ## we apply feature engineering next
    print("Applying feature engineering...")
    df=add_features(df)
    ## we then train our model
    print("Training model...")
    train_model(df, model_type="ridge")
    ## we finally move onto making the model pickle file as well as predicting the sales prices for the test.csv file given to us
    print("Generating predictions on test set...")
    predict("data/test.csv", "models/model.pkl")

if __name__ == "__main__":
    main()