import re

mobile_pattern = r'^(0|91)?[6-9][0-9]{9}$'

ifsc_pattern = r'^[A-Z]{4}0[A-Z0-9]{6}$'

vehicle_pattern = r'^[A-Z]{2}\s[0][1-9][0-9]{0,1}\s[A-Z]{1,3}\s[0-9]{1,4}$'

voter_pattern = r'^[A-Z]{3}[0-9]{7}$'

url_pattern = r'^(http|https):\/\/[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(\/.*)?$'

mobile_number = '9876543210'
ifsc_code = 'SBIN0001234'
vehicle_number = 'MH 12 AB 1234'
voter_id = 'ABC1234567'
url = 'https://www.imcc.com'

print(re.match(mobile_pattern, mobile_number))
print(re.match(ifsc_pattern, ifsc_code))
print(re.match(vehicle_pattern, vehicle_number))
print(re.match(voter_pattern, voter_id))
print(re.match(url_pattern, url))

import re

def is_valid_url(url):
    url_pattern = r'^(http|https):\/\/[a-zA-Z0-9]+([\-\.]{1}[a-zA-Z0-9]+)*\.[a-zA-Z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
    return bool(re.match(url_pattern, url))

def is_valid_email(email):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_pattern, email))

def is_valid_password(password):
    password_pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
    return bool(re.match(password_pattern, password))

url = 'https://www.example.com'
email = 'example@example.com'
password = 'Password123'

print(is_valid_url(url))
print(is_valid_email(email))
print(is_valid_password(password))