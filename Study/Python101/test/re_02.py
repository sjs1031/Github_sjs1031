import csv
import os.path

BASE = os.path.dirname(os.path.abspath(__file__))
'''
# Path to your input CSV file
input_csv_file_path = os.path.join(BASE,'re.csv')

# Path to your output CSV file
output_csv_file_path = os.path.join(BASE,'output.csv')

# List to store the first attribute values
first_attributes = []

# Open the input CSV file and read its contents
with open(input_csv_file_path, mode='r', encoding='utf-8') as input_file:
    csv_reader = csv.reader(input_file)
    for row in csv_reader:
        # Append the first attribute to the list
        first_attributes.append(row[0])

# Open the output CSV file and write the first attributes
with open(output_csv_file_path, mode='w', encoding='utf-8', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    for attribute in first_attributes:
        csv_writer.writerow([attribute])

print(f'First attributes saved to {output_csv_file_path}')
'''


# Path to your CSV file
input_csv_file_path = os.path.join(BASE,'re.csv')

# Path to your output CSV file
output_csv_file_path = os.path.join(BASE,'output.csv')

# List to store the first attribute values
first_attributes = []

# Open the CSV file and read its contents
with open(input_csv_file_path, mode='r', encoding='utf-8') as input_file:
    csv_reader = csv.reader(input_file)
    for row in csv_reader:
        # Append the first attribute to the list
        first_attributes.append(row[0])

# Open the output CSV file and write the first attributes
with open(output_csv_file_path, mode='w', encoding='utf-8', newline='') as output_file:
    csv_writer = csv.writer(output_file)
    for attribute in first_attributes:
        csv_writer.writerow([attribute])

# Print the first attributes
for attribute in first_attributes:
    print(attribute)
