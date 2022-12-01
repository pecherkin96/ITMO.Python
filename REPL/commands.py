import zip_util
from geopy.distance import geodesic

zip_codes = zip_util.read_zip_all()


def write_loc():
    zip_code = input("Enter a ZIP Code to lookup: ")
    if isinstance(loc(zip_code), tuple):
        print("ZIP Code", zip_code, "is in", ", ".join(loc(zip_code)[1]), "\ncoordinates:",
              " ".join(map(str, (loc(zip_code)[0]))))
        return
    else:
        print(loc(zip_code))


def loc(zip_code):
    flag = False
    for i in range(len(zip_codes) - 1):
        if zip_code == zip_codes[i][0]:
            flag = True
            zip_code_location = zip_codes[i][1:3]
            loc_name = zip_codes[i][3:5]
            return zip_code_location, loc_name
    if not flag:
        return "Invalid or unknown ZIP Code"


def zip():
    flag = False
    city_name = input("Enter a city name to lookup: ").title()
    state_name = input("Enter the state name to lookup: ").upper()
    city_name_zips = []
    for i in range(len(zip_codes) - 1):
        if city_name == zip_codes[i][3] and state_name == zip_codes[i][4]:
            flag = True
            city_name_zips.append(zip_codes[i][0])
            print("The following ZIP Code(s) found for", city_name, state_name, ":", ", "
                  .join(city_name_zips))
            break
    if not flag:
        print("No ZIP Code found for: ", city_name, state_name)


def dist():
    zip_code_1 = input("Enter the first ZIP Code: ")
    zip_code_2 = input("Enter the second ZIP Code: ")
    if isinstance(loc(zip_code_1), tuple) \
            and isinstance(loc(zip_code_2), tuple):
        coordinate_zip_code_1 = loc(zip_code_1)[0]
        coordinate_zip_code_2 = loc(zip_code_2)[0]
        distance_miles = round(geodesic(coordinate_zip_code_1, coordinate_zip_code_2).miles, 2)
        print("The distance between", zip_code_1, "and", zip_code_2, "is", distance_miles, "miles")
        return
    else:
        print("The distance between", zip_code_1, "and", zip_code_2, "cannot be determined")
