import json
import csv

# Load JSON data from file
with open('C:/Users/khushal sharma/PycharmProjects/myproject/venv/dmcctrading.json', 'r') as json_file:
    data = json.load(json_file)

# Create a list to store extracted data
extracted_data = []

# Accessing specific values (Phone_BD__c, Company_Official_Email_Address__c, and Name)
for item in data:
    for entry in item['result']['resultData']['v']:
        # Check if the necessary keys are present
        if 'v' in entry and 'Account__r' in entry['v'] and 'v' in entry['v']['Account__r']:
            phone_bd = entry['v']['Account__r']['v'].get('Phone_BD__c', 'N/A')
            email_address = entry['v']['Account__r']['v'].get('Company_Official_Email_Address__c', 'N/A')
            name = entry['v']['Account__r']['v'].get('Name', 'N/A')

            # Append the extracted data to the list
            extracted_data.append({'Name': name, 'Phone No': phone_bd, 'Email_Address': email_address})

# Specify the CSV file path
csv_file_path = 'C:/Users/khushal sharma/PycharmProjects/myproject/venv/DMCC_consultancy_list_data.csv'

# Write the extracted data to a CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:

    fieldnames = ['Name', 'Phone No', 'Email_Address']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data
    for entry in extracted_data:
        writer.writerow(entry)

print(f"Data has been saved to {csv_file_path}")
