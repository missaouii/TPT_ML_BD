import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from pprint import pprint
import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

from utils import fetch_logged_data


def main():
    # mlflow.set_tracking_uri("file:" + os.path.abspath(DIR_MLRUNS))
    mlflow.sklearn.autolog()
    data = pd.read_pickle("data_smpl.pkl")
    y = data['categorie']
    X = data.drop(columns=['categorie'])
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.9, test_size=0.1, random_state=0)
    # y = data['categorie']
    # X = data.drop(columns=['categorie'])
    # X_train, X_test, y_train, y_test = train_test_split(X, y, 
    #                                             test_size=0.2,random_state=7)
    model=LogisticRegression(solver='liblinear')
    model.fit(X_train,y_train)
    run_id = mlflow.last_active_run().info.run_id
    print("Logged data and model in run: {}".format(run_id))
    for key, data in fetch_logged_data(run_id).items():
        print("\n---------- logged {} ----------".format(key))
        pprint(data)
        
if __name__ == "__main__":
    main()