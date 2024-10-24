import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, matthews_corrcoef
import sys
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def performance(set3_gene, gene_insilicos):

    gene = set3_gene.split('_')[1]

    predictions = pd.read_csv(f'SET3_{gene}.csv')
    insilicos = pd.read_csv(f'{gene_insilicos}.csv')

    tmp = predictions[['variant','Clinical_Label','Clinical_Label_binary', 'RandomForest_Predictions']].merge(insilicos, on=['variant'], how='left')

    performances = pd.DataFrame(columns=['Predictor', 'TP', 'TN', 'FP', 'FN', 'Total',
                                     'Sensitivity', 'Specificity', 'Accuracy', 'MCC'])

    tools_list = ['RandomForest_Predictions',
                  'SIFT', 'PolyPhen', 'CADD', 'AlphaMissense', 'EVE','BayesDel']


    def calculate_params(tmp, predictor):

        # ensure missing predictons are eliminated
        df = tmp[tmp[predictor].notna()].copy()

        # Compute confusion matrix
        cm = confusion_matrix(df['Clinical_Label_binary'], df[predictor])

        # Extract TN, FP, FN, TP
        TN, FP, FN, TP = cm.ravel()

        # calculate parameters
        sensitivity = TP / (TP + FN)
        specificity = TN / (TN + FP)
        accuracy = accuracy_score(df['Clinical_Label_binary'], df[predictor])
        mcc = matthews_corrcoef(df['Clinical_Label_binary'], df[predictor])
        # New row to add
        new_row = {'Predictor':predictor,
               'TP':TP,
               'TN': TN,
               'FP':FP,
               'FN':FN,
               'Total':TP+TN+FP+FN,
               'Sensitivity':round(sensitivity,2),
               'Specificity':round(specificity,2),
               'Accuracy':round(accuracy,2),
               'MCC':round(mcc,2)}

        print(f'Performance of {predictor} ({len(df)}/{len(predictions)} predictions obtained)\n')
        print(f"\tTrue Positives (TP): {TP}")
        print(f"\tTrue Negatives (TN): {TN}")
        print(f"\tFalse Positives (FP): {FP}")
        print(f"\tFalse Negatives (FN): {FN}\n")

        print(f"\tSensitivity (SN): {round(sensitivity,2)}")
        print(f"\tSpecificity (SP): {round(specificity,2)}")
        print(f"\tAccuracy (ACC): {round(accuracy,2)}")
        print(f"\tMatthews corr. coef. (MCC): {round(mcc,2)}")

        print('____________________________\n')

        return pd.DataFrame([new_row])

    result_frames = []
    for predictor in tools_list:
        new_row=calculate_params(tmp, predictor)
        result_frames.append(new_row)

    performances = pd.concat(result_frames, ignore_index=True)
    
    # save results
    performances.to_csv(f'SET4_{gene}.csv', index=0)
    print(f'File SET4_{gene}.csv is saved with all performances metrics.')

    tmp.to_csv(f'SET5_{gene}.csv', index=0)
    print(f'\nFile SET5_{gene}.csv is saved with all prediction columns, combined in one file.')

    return None



if __name__ == "__main__":
    # If the user does not write py script name + predictions file + insilicos file, then some usage help is output
    if len(sys.argv) != 3:
        print("Usage: python3 performance.py <set3_gene> <gene_insilicos>")
        sys.exit(1)

    set3_gene = sys.argv[1]
    gene_insilicos = sys.argv[2]

    performance(set3_gene, gene_insilicos)
