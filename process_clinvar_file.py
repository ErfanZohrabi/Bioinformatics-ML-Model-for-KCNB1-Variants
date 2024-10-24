import pandas as pd
import re
import sys

def process_clinvar_file(gene):
    # Just some message for the user
    print(f"Processing data for gene:")

    # Create a dictionary to map three-letter amino acid codes to one-letter codes
    three_to_one = {
        'Ala': 'A', 'Cys': 'C', 'Asp': 'D', 'Glu': 'E', 'Phe': 'F', 'Gly': 'G',
        'His': 'H', 'Ile': 'I', 'Lys': 'K', 'Leu': 'L', 'Met': 'M', 'Asn': 'N',
        'Pro': 'P', 'Gln': 'Q', 'Arg': 'R', 'Ser': 'S', 'Thr': 'T', 'Val': 'V',
        'Trp': 'W', 'Tyr': 'Y'
    }

    # Function to extract the protein change from the "Name" column and convert to one-letter code
    def extract_variant(name):
        match = re.search(r'p\.([A-Za-z]+)(\d+)([A-Za-z]+)', name)  # Look for the pattern p.Arg1793Gln
        if match:
            ref_aa = match.group(1)  # Three-letter code for reference amino acid
            position = match.group(2)  # Position of the amino acid change
            alt_aa = match.group(3)  # Three-letter code for altered amino acid
            
            # Convert three-letter codes to one-letter codes
            ref_aa_one = three_to_one.get(ref_aa, ref_aa)
            alt_aa_one = three_to_one.get(alt_aa, alt_aa)
            
            # Return the variant in one-letter format
            return f"{ref_aa_one}{position}{alt_aa_one}"
        return None

    # Step 1: Load the ClinVar file into a pandas DataFrame (assuming it's tab-delimited)
    clinvar_df = pd.read_csv(f'{gene}.txt', sep='\t')

    # Step 2: Apply the function to the "Name" column to create a new "Variant" column
    clinvar_df['variant'] = clinvar_df['Name'].apply(extract_variant)
    clinvar_df= clinvar_df.dropna(subset=['variant'])

    # Step 3: Remove duplicates based on key columns (like VariationID, GRCh38Chromosome, GRCh38Location)
    clinvar_df = clinvar_df.drop_duplicates(subset=['VariationID', 'GRCh38Chromosome', 'GRCh38Location'])

    # Step 4: Filter for missense variants in the "Molecular consequence" column
    missense_df = clinvar_df[clinvar_df['Molecular consequence'].str.contains('missense variant', na=False)]
    missense_df = missense_df[missense_df['Gene(s)']==gene]

    # Step 5: Filter out variants that end with 'Ter' or any start/stop codon variants
    missense_df = missense_df[~missense_df['variant'].str.contains('Ter', na=False)]
    
    # Step 6: Create a new column "Unified_Class" to unify Likely Pathogenic/Pathogenic (LP/P) and Likely Benign/Benign (LB/B)
    def unify_classification(germline_classification):
        if 'Pathogenic' in germline_classification or 'Likely pathogenic' in germline_classification:
            return 'LP/P'
        elif 'Benign' in germline_classification or 'Likely benign' in germline_classification:
            return 'LB/B'
        else:
            return 'Other'

    missense_df['Clinical_Label'] = missense_df['Germline classification'].apply(unify_classification)
    
    
    # Step 7: Count the number of LP/P and LB/B variants
    lp_p_count = missense_df[missense_df['Clinical_Label'] == 'LP/P'].shape[0]
    lb_b_count = missense_df[missense_df['Clinical_Label'] == 'LB/B'].shape[0]

    # Print counts
    print(gene,'\n')
    print(f"LP/P variants: {lp_p_count}")
    print(f"LB/B variants: {lb_b_count}")

    # Return the cleaned DataFrame
    missense_df[['Gene(s)', 'variant', 'Clinical_Label']].reset_index(drop=True).to_csv(f'SET1_{gene}.csv', index=0)
    
    print(f'\nCleaned version of the data is saved as SET1_{gene}.csv')
    
    return None



if __name__ == "__main__":
    # If the user does not write py script name + gene name, then some usage help is output
    if len(sys.argv) != 2:
        print("Usage: python3 process_clinvar_file.py <gene>")
        sys.exit(1)
    
    gene = sys.argv[1]
    process_clinvar_file(gene)