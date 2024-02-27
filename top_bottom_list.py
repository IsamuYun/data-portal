from adi_csv_file import read_csv_to_dict
from adi_csv_file import write_csv

branch_geo_data_csv = "./data/ADI Branch GeoData.csv"

adi_top_bottom_list_csv = "./data/ADI Top and Bottom List.csv"

adi_tb_geo_data_csv = "./data/Top and Bottom GeoData List.csv"

branch_list = []

branch_list = read_csv_to_dict(branch_geo_data_csv)

adi_top_bottom_list = read_csv_to_dict(adi_top_bottom_list_csv)

def get_geo_data():
    for tb_branch in adi_top_bottom_list:
        get_geo_data_by_dc(tb_branch)
        
    print(tb_branch)
    
    write_csv(adi_tb_geo_data_csv, adi_top_bottom_list)

def get_geo_data_by_dc(top_bottom_branch):
    dc_key = 'DC'
    dc_name = ''
    if 'Branch' in top_bottom_branch:
        if top_bottom_branch["Branch"]:
            dc_name = top_bottom_branch["Branch"].split(" - ")[0]
    
    
    for branch in branch_list:
        if branch['DC'] == dc_name:
            top_bottom_branch["Latitude"] = branch["Latitude"]
            top_bottom_branch["Longitude"] = branch["Longitude"]

get_geo_data()