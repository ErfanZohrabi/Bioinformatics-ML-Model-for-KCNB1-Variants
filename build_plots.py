import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os
from matplotlib.backends.backend_pdf import PdfPages

def build_plots(set2_gene):
    gene = set2_gene.split('_')[1]
    file = pd.read_csv(set2_gene + '.csv')
    
    # directory to save the plots
    plot_dir = gene + '_features_plots'
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
    
    # list of features to plot
    features_list = ['Blosum62', 'PSSM', 'Shannon\'s entropy',
                     'Shannon\'s entropy of seq. neighbours', 'neco', 'pLDDT', 'pLDDT bin',
                     'colasi', 'fraction cons. 3D neighbor', 'fanc', 'fbnc',
                     'M.J. potential', 'access.dependent vol.', 'laar']
    
    for feature in features_list:
        # just some message for the user
        print(f"Generating plots for {feature}...")
        
        # clean feature name for PDF title
        clean_feature_name = feature.replace('\'', '')
        
        with PdfPages(f'{plot_dir}/{clean_feature_name}.pdf') as pdf:
            
            # KDE plot
            plt.figure(figsize=(10, 5))
            sns.kdeplot(data=file, x=feature, hue='Clinical_Label_binary', fill=True, palette={0: 'blue', 1: 'red'})
            plt.title(f'KDE Plot')
            plt.xlabel(feature)
            plt.ylabel('Density')
            plt.legend(title='Clinical Label', labels=['Pathogenic', 'Benign'])
            pdf.savefig()
            plt.close()

            # Histogram plot
            plt.figure(figsize=(10, 5))
            file[file['Clinical_Label_binary'] == 0][feature].hist(bins=30, alpha=0.5, label='benign', color='blue')
            file[file['Clinical_Label_binary'] == 1][feature].hist(bins=30, alpha=0.5, label='pathogenic', color='red')
            plt.title(f'Histogram')
            plt.xlabel(feature)
            plt.ylabel('Frequency')
            plt.legend(title='Clinical Label', labels=['Benign', 'Pathogenic'])
            pdf.savefig()
            plt.close()




if __name__ == "__main__":
    # If the user does not write py script name + file name to build plots, then some usage help is output
    if len(sys.argv) != 2:
        print("Usage: python3 build_plots.py <file_name>")
        sys.exit(1)
    
    file_name = sys.argv[1]
    build_plots(file_name)
