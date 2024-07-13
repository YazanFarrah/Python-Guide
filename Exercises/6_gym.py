# Need some work, maybe do an infinite for loop as long as the number 8 for example or q aren't pressed

# Write a program to manage two gyms.
# 1. Add or Remove members
# 2. Display common members in both Gyms
# 3. Check if a gym is subset or superset of the other.
# 4. Display a combined list of all members
# 5. Find exclusive members in each gym.

fire_gym = {1, 2, 3, 4}
ice_gym = {1, 2, 5, 6, 7}

print("Welcome to our gym management system!, We have two gyms!, Fire Gym and Ice Gym!\n")

show_add_message = input("Wanna add members to one of the gyms? Yes/No ").lower() == "yes"

if show_add_message:
    is_fire = input("Choose gym, Fire or Ice, Gym ").lower() == "fire"
    if is_fire:
        fire_gym.add(input(f"Add a member to Fire gym "))
    else:
        ice_gym.add(input(f"Add a member to Ice gym "))

res = input("Check if Fire gym is subset or superset of Ice gym? Yes/No ").lower() == "yes"

if res:
    print(f"Is Fire Gym subset? {fire_gym.issubset(ice_gym)}")
    print(f"Is Fire Gym superset? {fire_gym.issuperset(ice_gym)}")

common_members = fire_gym & ice_gym

print(f"All common members from both gyms are: {common_members}")
