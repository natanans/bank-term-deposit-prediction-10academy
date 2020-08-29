from sklearn.feature_extraction.text import CountVectorizer
from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold
def add_onehot_to_dataframe(sparse, df, vectorizer, name):
  '''
      This function will add the one hot encoded to the dataframe.

  '''
  for i, col in enumerate(vectorizer.get_feature_names()):
    colname = name+"_"+col
    # df[colname] = pd.SparseSeries(sparse[:, i].toarray().flatten(), fill_value=0)
    df[colname] = sparse[:, i].toarray().ravel().tolist()
  
  return df
columnTransformer = ColumnTransformer([
                                       ('drop_columns' , 'drop', ['duration']),
                                       ('scaler', StandardScaler(),
                                        ['age','pdays','previous','emp.var.rate','cons.price.idx',
                                         'cons.conf.idx','euribor3m','nr.employed','year']),
                                       ], 
                                      remainder='passthrough')
def OneHotEncoder(categorical_cols, X_train, X_test=None, X_cv=None, include_cv=False,include_test=False):
  '''
    This function takes categorical column names as inputs. The objective
    of this function is to take the column names iteratively and encode the 
    features using One hot Encoding mechanism and also adding the encoded feature
    to the respective dataframe.

    The include_cv parameter indicates whether we should include CV dataset or not.
    This is added specifically because when using GridSearchCV or RandomizedSearchCV,
    we only split the dataset into train and test to give more data to training purposes.
    This is done because GridSearchCV splits the data internally anyway.
  '''

  for i in categorical_cols:
    Vectorizer = CountVectorizer(token_pattern="[A-Za-z0-9-.]+")
    print("Encoding for feature: ", i)
    # Encoding training dataset 
    temp_cols = Vectorizer.fit_transform(X_train[i])
    X_train = add_onehot_to_dataframe(temp_cols, X_train, Vectorizer, i)

    # Encoding Cross validation dataset
    if include_cv:
      temp_cols = Vectorizer.transform(X_cv[i])
      X_cv = add_onehot_to_dataframe(temp_cols, X_cv, Vectorizer, i)
    if include_test:
    # Encoding Test dataset
        temp_cols = Vectorizer.transform(X_test[i])
        X_test = add_onehot_to_dataframe(temp_cols, X_test, Vectorizer, i)




columnTransformer = ColumnTransformer([
                                       ('drop_columns' , 'drop', ['duration']),
                                       ('scaler', StandardScaler(),
                                        ['age','pdays','previous','emp.var.rate','cons.price.idx',
                                         'cons.conf.idx','euribor3m','nr.employed','year']),
                                       ], 
                                      remainder='passthrough')

def validator (model,stratified=False):
  
  target = data['y']
  features = data.drop(['y'], axis=1)
  if(stratified):
    kfold = StratifiedKFold(n_splits=5, random_state=7)
  else:
    kfold= KFold(n_splits=5, random_state=7)

  results = cross_val_score(model, features, target,scoring='f1', cv=kfold)
  print("Accuracy: %.4f%% (%.4f%%)" % (results.mean()*100, results.std()*100))
  return (results.mean()*100, results.std()*100)