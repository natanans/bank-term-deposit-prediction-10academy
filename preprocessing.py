
import imports
def fetch_data (path):
    import imports
    isFile = os.path.isfile(path) 
    print(isFile)                           
    data = pd.read_csv(path, sep=';'  , engine='python')
    return data

def check_integrity(data):
   for i in data[:]:
    print("===============================================================================")
    print(i)
    print( "Has "+str(data[i].isnull().sum())+" missing values")
    print(data[i].dtypes)
    print("===============================================================================")
    print(data[i].unique())
    
    
    
    
def percentage(part, whole):
  return 100 * float(part)/float(whole)

def clean(x1,y1,remove_na,low=.15,high=.90):
    print(x1[y1].value_counts())
    total=len(x1['y'])
    target_before=len(x1[x1['y'] == 'yes'])
    target_before=percentage(target_before,total)
    x1.loc[x1[y1] < x1[y1].quantile(low), y1] =x1[y1].quantile(low)
    
    x1.loc[x1[y1] > x1[y1].quantile(high), y1] =x1[y1].quantile(high)
    if remove_na:
         x1= x1[x1[y1].notnull()]
   
    print(x1[y1].value_counts(dropna=False))
    target_after=len(x1[x1['y'] == 'yes'])
    target_after=percentage(target_after,total)
    print("Change in target variable is from  "+str(target_before)+"%  to  "+str(target_after)+"%")
    return x1