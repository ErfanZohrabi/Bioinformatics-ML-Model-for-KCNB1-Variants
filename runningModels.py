import pandas as pd
import sys
from sklearn.model_selection import LeaveOneOut, cross_val_predict
from sklearn.ensemble import RandomForestClassifier

def runningModels(set2_gene):
    gene = set2_gene.split('_')[1]
    
    df = pd.read_csv(f'SET2_{gene}.csv')

    features_list = ['Blosum62', 'PSSM', "Shannon's entropy",
                       "Shannon's entropy of seq. neighbours", 'neco', 'pLDDT', 'pLDDT bin',
                       'colasi', 'fraction cons. 3D neighbor', 'fanc', 'fbnc',
                       'M.J. potential', 'access.dependent vol.', 'laar']
    
    # Features and labels
    X = df[features_list]  # Feature columns
    y = df['Clinical_Label_binary']  # Encoded label column
    
    # Initialize the model
    model = RandomForestClassifier()
        
    # Define Leave-One-Out cross-validator
    loo = LeaveOneOut()
    
    # Perform Leave-One-Out cross-validation with cross_val_predict
    print('Running the ML model with the following parameters:\n')
    print('\tModel algorithm: Random forest classifier with leave-one-variant-out cross validation')
    print('\tFeatures:')
    for a in features_list:
        print('\t\t-',a)
    print('\tLabel: 0 (LB/B) and 1 (LP/P) binary classes of variants' )
    
    predictions = cross_val_predict(model, X, y, cv=loo)
    
    # Add predictions to the original dataframe
    df['RandomForest_Predictions'] = predictions
    

    df.to_csv(f'SET3_{gene}.csv',index=0)
    
    print(f'File SET3_{gene}.csv is saved with Predictions column added.')
    
    return None



if __name__ == "__main__":
    # If the user does not write py script name + file name to run ML on, then some usage help is output
    if len(sys.argv) != 2:
        print("Usage: python runningModels.py <file_name>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    runningModels(file_name)