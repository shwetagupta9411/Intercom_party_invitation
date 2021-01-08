# Intercom Party Invitation

## Problem

We have some customer records in a text file (customers.txt) -- one customer per line, JSON
lines formatted. We want to invite any customer within 100km of our Dublin office for some food
and drinks on us. Write a program that will read the full list of customers and output the names
and user ids of matching customers (within 100km), sorted by User ID (ascending).

* You must use the first formula from this Wikipedia article to calculate distance. Don't
forget, you'll need to convert degrees to radians.
* The GPS coordinates for our Dublin office are 53.339428, -6.257664.

## Set-up

**Pre-requisites :**
* `Python3` should be installed.
* `pytest` is been used to write the testcases.

**Set-up with the virtual environment :**
1. `git clone https://github.com/shwetagupta9411/intercom_party_invitation.git`
3. `pip3 install virtualenv` (if you don't have virtualenv installed)
4. `virtualenv intercom`
5. `source intercom/bin/activate`
6. `cd intercom_party_invitation/`
5. `pip install -r requirements.txt`

#### OR

**Set-up without the virtual environment :**
1. `git clone https://github.com/shwetagupta9411/intercom_party_invitation.git`
2. `pip3 install pytest`
3. `cd intercom_party_invitation/`

## Run
**Command to Run the script :**
* `python3 customer_party_list.py`

It will print the list of customers within the 100km of given Intercom office coordinates. It will also generate the output.txt file with the filtered customers.

## Test
**Command to Test the script :**
* `python3 -m pytest tests/test_customer_party_list.py`

Test cases are located inside the tests/test_customer_party_list.py. There are 8 testcases which tests the functionaly of the entire script. The folder test_data has the files which are used in the testcases.

**The Answer to the `Proudest Achievement` is inside the file `proudest_achievement.txt`.**
