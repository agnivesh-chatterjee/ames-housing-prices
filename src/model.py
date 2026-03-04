## model.py
## This method returns the model we end up using based on our choice. While it is arguable this method is rather pointless, I would like to build a little more project in the coming weeks and try out different models on it
## So while it only has LR and Ridge for now, I might make a comparitive study of different model types into this function
from sklearn.linear_model import LinearRegression, Ridge
def get_model(model_type="linear"):
    if model_type=="linear":
        return LinearRegression()
    elif model_type=="ridge":
        return Ridge(alpha=1.0)
    else:
        raise ValueError("Invalid model type")