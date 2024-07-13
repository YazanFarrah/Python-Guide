#  Users can access only if they have those codes:
# 69, 420, 888, 6912, or if they enter a 4-digit number

access_list = [69, 420, 888, 6912]

user_code = int(input("Please enter a code to access our wowzi system\n"))

is_valid_code = 1000 <= user_code <= 9999

# Or convert to string and check if the length is 4

is_member = access_list.__contains__(user_code)

is_granted_access = is_valid_code or is_member

is_denied_access = not is_granted_access

print("Access Granted. Welcome back" * is_granted_access + "Access Denied" * is_denied_access)

# When multiplying a string with *, it is available only when the bool variable is true


text = "Hello"

print(text[::-1])