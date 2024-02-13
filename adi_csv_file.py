import csv

#adi_csv_file = "./data/ADI Branch GeoData 2024.csv"

#geodata_csv_file = "./data/ADI Branch GeoData.csv"

#branch_list = []

def read_csv_to_dict(csv_file_path):
    dict_list = []
    # Open CSV file
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        dict_reader = csv.DictReader(file)
    
        for dict in dict_reader:
            dict_list.append(dict)
    
    return dict_list

def write_csv(csv_file_path, dict_list):
    if not dict_list:
        return False
    #Open CSV file
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = dict_list[0].keys()
        
        writer = csv.DictWriter(file, fieldnames)
        
        writer.writeheader()
        
        for item in dict_list:
            writer.writerow(item)
            
    return True

