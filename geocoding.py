import googlemaps
from adi_csv_file import read_csv_to_dict
from adi_csv_file import write_csv

gmaps = googlemaps.Client('AIzaSyBv1hiFGq4PI5tKUOQ_FhXaqHXM4zVunTs')



#print(geocode_result[0]["geometry"]["location"])

adi_branch_csv = "./data/ADI Branch GeoData 2024.csv"
geo_data_csv = "./data/ADI Branch GeoData.csv"

branch_list = []

branch_list = read_csv_to_dict(adi_branch_csv)

def get_geo_code(address):
    location = {}
    # Geocoding an address
    geocode_result = gmaps.geocode(address)
    
    if geocode_result:
        location["Lantitude"] = geocode_result[0]["geometry"]["location"]["lat"]
        location["Longitude"] = geocode_result[0]["geometry"]["location"]["lng"]
    
    return location

def get_branch_geometry(branch_list):
    if not branch_list:
        return
    
    for branch in branch_list:
        full_address = get_full_address(branch)
        location = get_geo_code(full_address)
        if location:
            branch["Latitude"] = location["Latitude"]
            branch["Longitude"] = location["Longitude"]

def get_full_address(branch):
    address_list = []
    if branch and branch["Address"] and branch["City"] and branch["State"] and branch["Zip"]:
        address_list.append(branch["Address"])
        address_list.append(branch["City"])
        address_list.append(branch["State"])
        address_list.append(branch["Zip"])
        
    full_address = ', '.join(address_list)
    
    return full_address

get_branch_geometry(branch_list)

write_csv(geo_data_csv, branch_list)