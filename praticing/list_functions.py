lucky_nums = [19, 230, 31, 18, 84, 457]
friends = ["Amr", "Abd", "Lety", "Hussam"]

unordered_list = ["Zack", "Belly", "Mark", "Yaz", "Abu", "Kalb"]

friends.extend(lucky_nums)  # Append a list to a list

friends.append("An individual element")  # Append an itme to a list

friends.insert(3, "Katy")  # Insert item at certain index

friends.remove("Katy")  # Remove item by its value

print(friends)

friends.pop()

print(friends.index("Amr"))

friends.append("Amr")

print(friends.count("Amr"))  # Shows how many times Amr appeared in the list

friends.clear()

print(friends)

unordered_list.sort()

lucky_nums.sort()

print(unordered_list)

print(lucky_nums)

lucky_nums.reverse()

print(lucky_nums)

lucky2 = lucky_nums.copy()

print(lucky2)
