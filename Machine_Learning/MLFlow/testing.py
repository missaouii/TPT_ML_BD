from pprint import pprint

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import xgboost as xgb
import mlflow
from utils import fetch_logged_data
import xgboost as xgb
from sklearn.preprocessing import LabelEncoder 



def main():
    # enable autologging
    mlflow.sklearn.autolog()

    # prepare training data
    data = pd.read_pickle("data_smpl.pkl")
    y = data['categorie']
    X = data.drop(columns=['categorie'])
    

    lc = LabelEncoder() 

    lc = lc.fit(y) 

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.9, test_size=0.1, random_state=0)
    lc_y_train = lc.transform(y_train)

    lc_y_test = lc.transform(y_test)
    experiment = mlflow.get_experiment_by_name("classification models")
    if experiment is None:
        experiment_id = mlflow.create_experiment("classification models")
    else:
        experiment_id = experiment.experiment_id


    models_test = {
        "logistic regression": LogisticRegression(solver='liblinear'),
        "random forest": RandomForestClassifier(n_estimators=100, 
                                criterion='gini',
                                max_features='sqrt',
                                max_depth=11, 
                                n_jobs=2,
                                random_state=0),
                        "xgb": xgb.XGBClassifier(objective='multi:softmax', \
                         num_class=4, \
                         colsample_bytree=1.0, \
                         gamma=0, \
                         learning_rate=0.01, \
                         max_depth=9, \
                         min_child_weight=10, \
                         n_estimators=100, \
                         reg_alpha=0.1, \
                         subsample=0.5),
        "svc": SVC(kernel='rbf',gamma='scale',C=10)
    }
    for run_name, model in models_test.items():
        with mlflow.start_run(run_name=run_name, experiment_id=experiment_id) as run:
            # train a model
            model.fit(X_train, lc_y_train)
            run_id = run.info.run_id
            print("Logged data and model in run {}".format(run_id))

            mlflow.log_param("model", run_name)
            # evaluate the model on test data
            test_score=model.score(X_test, lc_y_test)
            mlflow.log_metric("test_accuracy", test_score)

            # show logged data
            for key, data in fetch_logged_data(run_id).items():
                print("\n---------- logged {} ----------".format(key))
                pprint(data)


if __name__ == "__main__":
    main()
