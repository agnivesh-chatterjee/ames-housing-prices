##  feature_engineering.py
## This is the method where I wanted to dedicate most of my time. Really took me a long time to sit and figure out what I would group into the same features
## Having so many features and having to read the data description for the codeified headings in my eda notebook really made it difficult to figure out which features would collapse into the same feature
## there is definitely some potential in returning to this project in a week or two and trying to figure out more ways to make the computations more efficient internally
def add_features(df):
    ## Total square footage is the feature I could first think of that would be a better way to deal with the SF features as one would normally look at the total foot area of the house rather than have separate floors determine the prices as I have often seen houses listed as total square footage and number of floors in my own hometown
    ## One may argue there is some merit to keeping the 1stFlrSF separate as often houses may have a larger 1st floor and smaller 2nd floor and typically a house like that would be better preferred over a house with a smaller 1st floor but relatively larger 2nd floor but that may be a personal bias so we dont think of it here
    df["TotalSF"] = (
        df.get("TotalBsmtSF", 0)
        + df.get("1stFlrSF", 0)
        + df.get("2ndFlrSF", 0)
    )
    ## Next we moved onto the bathrooms which was again a little bit of the same idea except I thought of halving the value for half bathrooms and keeping the full value for a full bathroon. The idea od having these values be weighted is obvious in hindsight but I thought of it after worrying about my first and secon floor conundrum in the previous feature
    ## Total bathrooms
    df["TotalBath"] = (
        df.get("FullBath", 0)
        + 0.5 * df.get("HalfBath", 0)
        + df.get("BsmtFullBath", 0)
        + 0.5 * df.get("BsmtHalfBath", 0)
    )
    ## Being short on time owing to my midterms/other mentored projects (which you can find listed on my github), these are the two sets of features I clubbed for now. I am sure there must be other features that I can club together but at this time I am a little scared regarding how well my model might perform upon grouping any other features so we leave it be for now
    ## for example, a feature I did think of was to group garage features together but owing to some houses having a second house listed under miscalleanpus features, I could not think of a computationally efficient way of doing so
    return df