import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
from sklearn.metrics import roc_curve, auc
from matplotlib.patches import Patch
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

def performance_plots(set4_gene):
    gene = set4_gene.split('_')[1]
    performance_df = pd.read_csv(set4_gene + '.csv')
    
    # directory to save the plots
    plot_dir = f'{gene}_performance_plots'
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
    
    palette = sns.color_palette("RdBu", n_colors=len(performance_df))

    # ACC: Barplot with color coding and legend for predictors
    print("Generating Accuracy plot...")
    plt.figure(figsize=(10, 6))
    acc_sorted = performance_df.sort_values(by='Accuracy', ascending=False)
    sns.barplot(x='Predictor', y='Accuracy', data=acc_sorted, palette=palette)
    plt.title('Accuracy', fontsize=15)
    plt.ylabel('Accuracy', fontsize=15)
    plt.xticks(rotation=90, fontsize=15)
    plt.xlabel('')
    legend_elements = [Patch(color=palette[i], label=acc_sorted['Predictor'].iloc[i]) for i in range(len(acc_sorted))]
    plt.legend(handles=legend_elements, title='Predictors', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=15, title_fontsize=15)
    plt.tight_layout()
    plt.savefig(f'{plot_dir}/accuracy_barplot.pdf')
    plt.close()

    # MCC: Barplot with color coding and legend for predictors
    print("Generating MCC plot...")
    plt.figure(figsize=(10, 6))
    mcc_sorted = performance_df.sort_values(by='MCC', ascending=False)
    sns.barplot(x='Predictor', y='MCC', data=mcc_sorted, palette=palette)
    plt.title('MCC', fontsize=15)
    plt.ylabel('MCC', fontsize=15)
    plt.xticks(rotation=90, fontsize=15)
    plt.xlabel('')
    legend_elements = [Patch(color=palette[i], label=mcc_sorted['Predictor'].iloc[i]) for i in range(len(mcc_sorted))]
    plt.legend(handles=legend_elements, title='Predictors', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=15, title_fontsize=15)
    plt.tight_layout()
    plt.savefig(f'{plot_dir}/mcc_barplot.pdf')
    plt.close()
    

    # SN-SP scatter plot: where x axis is the Sensitivity, y axis is the Specificity, and dots are the predictors.
    print("Generating SN-SP scatter plot...")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Sensitivity', y='Specificity', hue='Predictor', data=performance_df, s=300)
    plt.title('SN-SP', fontsize=15)
    plt.xlabel('Sensitivity', fontsize=15)
    plt.ylabel('Specificity', fontsize=15)
    plt.legend(title='Predictors', fontsize=11, title_fontsize=12, loc='upper left')
    plt.tight_layout()
    plt.savefig(f'{plot_dir}/sn_sp_scatterplot.pdf')
    plt.close()
    



if __name__ == "__main__":
    # If the user does not write py script name + set4 file name, then some usage help is output
    if len(sys.argv) != 2:
        print("Usage: python3 performance_plots.py <set4_gene> ")
        sys.exit(1)

    set4_gene = sys.argv[1]
    
    performance_plots(set4_gene)