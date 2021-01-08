import json, os
from math import radians, cos, sin, asin, sqrt

""" To run the script, run the bellow command:
python3 customer_party_list.py 
"""

class CustomerPartyList(object):
    def __init__(self, file, office_lat, office_lon, distance_within, output):
        self.EARTH_RADIUS = 6371 # Radius of earth (mean) in km
        self.file = file
        self.office_lat = office_lat
        self.office_lon = office_lon
        self.distance_within = distance_within
        self.output = output

    """Method to load the customer data"""
    def load_customers(self, file):
        customers = []
        try:
            with open(file) as f:
                for line in f:
                    customers.append(json.loads(line))
            return customers
        except (OSError, IOError) as e:
            print("Opps, Filepath or content is incorrect.\n", str(e))

    """Calculates the distance of customer's house to the office """
    def distance_from_office(self, cust_latitude, cust_longitude):
        try:
            # Converting from degrees to radians.
            lat1 = radians(float(cust_latitude))
            lon1 = radians(float(cust_longitude))
            lat2 = radians(float(self.office_lat))
            lon2 = radians(float(self.office_lon))

            lat_distance = (lat1 - lat2)
            lon_diatance = (lon1 - lon2)
            coordinates = sin(lat_distance/2) * sin(lat_distance/2) + cos(lat1) * cos(lat2) * sin(lon_diatance/2) * sin(lon_diatance/2)
            new_coordinates = 2 * asin(sqrt(coordinates))
            customer_distance = round((self.EARTH_RADIUS * new_coordinates), 2)
            return customer_distance
        except (OSError, IOError) as e:
            print("Opps, Something went wrong in distance_from_office.\n", str(e))

    """Sorts the list according to user ID"""
    def sort(self, customers_list):
        # Key is set to sort in sscending order using User ID of sublist
        return(sorted(customers_list, key = lambda x: x[0]))

    """Generates the output.txt file with the customer names with in the specified range"""
    def generate_invitation_list(self, customers_list, output_file):
        try:
            with open(output_file, "w") as outfile:
                if len(customers_list) != 0:
                    outfile.write("Customers who live in the range of 100 km to the office.\n")
                    outfile.write("\nCustomer_ID \tName \tDistance(km)\n")
                    print("\nCustomer_ID\tName      \tDistance(km) \n")
                    for item in customers_list:
                        print('\t\t'.join(str(e) for e in item))
                        outfile.write('\t\t'.join(str(e) for e in item))
                        outfile.write('\n')
                print("\nOutput file output.txt is generated with the list of customers to invite.\n")
        except (OSError, IOError) as e:
            print("Opps, Filepath or content is incorrect.\n", str(e))

    """Filters the customer who lives in the 100km range to office"""
    def customers_to_invite(self, all_customers):
        customers_list = []
        try:
            if all_customers:
                for cust in all_customers:
                    customer_distance = self.distance_from_office(cust['latitude'], cust['longitude'])
                    if customer_distance <= self.distance_within:
                        customers_list.append([int(cust['user_id']), cust['name'], customer_distance])
            return customers_list
        except (OSError, IOError) as e:
            print("Opps, Something went wrong in customers_to_invite.\n", str(e))

    def run(self):
        try:
            all_customers = self.load_customers(self.file)
            customers_list = self.customers_to_invite(all_customers)
            sorted_cust_list = self.sort(customers_list)
            self.generate_invitation_list(sorted_cust_list, self.output)
        except (OSError, IOError) as e:
            print("Opps, Something went wrong in customers_to_invite.\n", str(e))


# Driver
if __name__ == '__main__':
    file = "customers.txt"
    output_file = "output.txt"
    office_lat = 53.339428
    office_lon = -6.257664
    distance_within = 100 #km
    invitation = CustomerPartyList(file, office_lat, office_lon, distance_within, output_file)
    invitation.run()
