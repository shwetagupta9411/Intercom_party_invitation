import pytest, os
from customer_party_list import CustomerPartyList

FILE = "tests/test_data/test_customers.txt"
OUTPUT_FILE = "tests/test_data/test_output.txt"
OFFICE_LAT = 53.339428
OFFICE_LON = -6.257664
DISTANCE_WITHIN = 100
OUTPUT = ""
LOADED_CUSTOMERS = [{"latitude": "52.2559432", "user_id": 9, "name": "Jack Dempsey", "longitude": "-7.1048927"},
                   {"latitude": "52.240382", "user_id": 10, "name": "Georgina Gallagher", "longitude": "-6.972413"}]
ALL_CCUSTOMER = [{"latitude": "53.008769", "user_id": 11, "name": "Richard Finnegan", "longitude": "-6.1056711"},
                {"latitude": "51.92893", "user_id": 1, "name": "Alice Cahill", "longitude": "-10.27699"},
                {"latitude": "51.8856167", "user_id": 2, "name": "Ian McArdle", "longitude": "-10.4240951"},
                {"latitude": "53.2451022", "user_id": 4, "name": "Ian Kehoe", "longitude": "-6.238335"}]
CUST_LIST_TO_SORT = [[12, 'Christina McArdle', 41.77], [8, 'Eoin Ahearn', 83.53], [26, 'Stephen McArdle', 98.87], [6, 'Theresa Enright', 24.09]]
SORTED_CUST_LIST = [[6, 'Theresa Enright', 24.09], [8, 'Eoin Ahearn', 83.53], [12, 'Christina McArdle', 41.77],  [26, 'Stephen McArdle', 98.87]]

class TestCustomerPartyList(object):
    @pytest.fixture
    def customerPartyList(self):
        return CustomerPartyList(FILE, OFFICE_LAT, OFFICE_LON, DISTANCE_WITHIN, OUTPUT)

    def test_load_customers(self, customerPartyList):
        result = customerPartyList.load_customers(FILE)
        assert result == LOADED_CUSTOMERS

    def test_distance_from_office_within_100km(self, customerPartyList):
        cust_latitude = 53.1229599
        cust_longitude = -6.2705202
        distance = customerPartyList.distance_from_office(cust_latitude, cust_longitude)
        assert distance <= DISTANCE_WITHIN

    def test_distance_from_office_not_within_100km(self, customerPartyList):
        cust_latitude = 52.2559432
        cust_longitude = -7.1048927
        distance = customerPartyList.distance_from_office(cust_latitude, cust_longitude)
        assert distance > DISTANCE_WITHIN

    def test_sort(self, customerPartyList):
        sorted_cust = customerPartyList.sort(CUST_LIST_TO_SORT)
        assert sorted_cust == SORTED_CUST_LIST

    def test_generate_invitation_list_with_no_customers(self, customerPartyList):
        customerPartyList.generate_invitation_list([], OUTPUT_FILE)
        assert os.stat("tests/test_data/test_output.txt").st_size == 0

    def test_generate_invitation_list(self, customerPartyList):
        customerPartyList.generate_invitation_list(SORTED_CUST_LIST, OUTPUT_FILE)
        assert os.stat("tests/test_data/test_output.txt").st_size != 0

    def test_customers_to_invite(self, customerPartyList):
        customers_list = customerPartyList.customers_to_invite(ALL_CCUSTOMER)
        assert customers_list == [[11, "Richard Finnegan", 38.14],[4, "Ian Kehoe", 10.57]]

    def test_customers_to_invite_with_no_customers(self, customerPartyList):
        customers_list = customerPartyList.customers_to_invite(LOADED_CUSTOMERS)
        assert customers_list == []


if __name__ == '__main__':
    main()
