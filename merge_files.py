import pandas as pd
from sklearn.preprocessing import LabelEncoder
import sys

def merge_files(set1_gene):
    # Just some message for the user
    print(f"Merging files for: {set1_gene}")

    gene = set1_gene.split('_')[1]
    # open SET1_gene.csv file
    df = pd.read_csv(f'SET1_{gene}.csv')
    
    label_encoder = LabelEncoder()
    label_encoder.fit(['LB/B', 'LP/P'])  # Ensures 'LB/B' is 0 and 'LP/P' is 1
    
    df['Clinical_Label_binary'] = label_encoder.transform(df['Clinical_Label'])
        
    lp_p_count = df[df['Clinical_Label_binary'] == 1].shape[0]
    lb_b_count = df[df['Clinical_Label_binary'] == 0].shape[0]
    print('New column is created: "Clinical_Label_binary"')
    print('# of LP/P are now labeled as 1: number of variants', lp_p_count)
    print('# of LB/B are now labeled as 0: number of variants', lb_b_count)
    
    # open features file
    features = pd.read_csv(f'{gene}_features.csv')
    
    # structural features (7/9)
    columns_to_update = ['colasion takes a set1_gene argument.','fraction cons. 3D neighbor','fanc','fbnc','M.J. potential','access.dependent vol.','laar']
    
    # Update structural features where 'pLDDT bin' is 0
    features.loc[features['pLDDT bin'] == 0, columns_to_update] = 0.0
    
    # merge files
    merged = df.merge(features, on=['variant'], how='left')
    
    merged = merged[['Gene(s)', 'variant', 'Clinical_Label', 'Clinical_Label_binary', 'uniprot', 
                    'Blosum62', 'PSSM', "Shannon's entropy",
                   "Shannon's entropy of seq. neighbours", 'neco', 'pLDDT', 'pLDDT bin',
                   'colasi', 'fraction cons. 3D neighbor', 'fanc', 'fbnc',
                   'M.J. potential', 'access.dependent vol.', 'laar']]
    
    features_list = ['Blosum62', 'PSSM', "Shannon's entropy",
           "Shannon's entropy of seq. neighbours", 'neco', 'pLDDT', 'pLDDT bin',
           'colasi', 'fraction cons. 3D neighbor', 'fanc', 'fbnc',
           'M.J. potential', 'access.dependent vol.', 'laar']
    print('The features are:')
    for a in features_list:
        print('\t -',a)
        
    merged.to_csv(f'SET2_{gene}.csv', index=0)
    print(f'SET2_{gene}.csv is saved.' )
    
    return None



if __name__ == "__main__":
    # If the user does not write py script name + file name to merge, then some usage help is output
    if len(sys.argv) != 2:
        print("Usage: python3 merge_files.py <set1_gene>")
        sys.exit(1)
    
    set1_gene = sys.argv[1]
    merge_files(set1_gene)