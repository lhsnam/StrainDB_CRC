import os
import csv
import argparse

def extract_name_and_first_row(fna_file):
    with open(fna_file, 'r') as file:
        first_line = file.readline().strip()
        
        # Find the first space
        first_space_index = first_line.find(' ')
        first_comma_index = first_line.find(',')

        if first_space_index != -1:
            if first_comma_index != -1:
                # Extract the string between the first space and the first comma
                extracted_string = first_line[first_space_index + 1:first_comma_index].strip()
            else:
                # Extract the string after the first space if no comma exists
                extracted_string = first_line[first_space_index + 1:].strip()
        else:
            extracted_string = ''
    
    filename = os.path.basename(fna_file)
    
    # Get the part before the second underscore
    name_part = '_'.join(filename.split('_')[:2])  # Concatenate first two parts before the second underscore
    return f"{name_part} {extracted_string}", filename  # Add space between the two parts

def create_csv(input_folder, output_file='output.csv'):
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['name', 'genome_filename', 'protein_filename'])  # Write header

        for root, _, files in os.walk(input_folder):
            for file in files:
                if file.endswith('.fna'):
                    fna_file_path = os.path.join(root, file)
                    name, genome_filename = extract_name_and_first_row(fna_file_path)
                    csv_writer.writerow([name, genome_filename, ''])  # Write data row

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a CSV from .fna files.')
    parser.add_argument('-i', '--input', required=True, help='Path to the folder containing .fna files')
    
    args = parser.parse_args()
    create_csv(args.input)
