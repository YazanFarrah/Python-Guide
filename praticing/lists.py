friends = ["Amr", "Abd", "Lety", "Hussam", "Mohannad"]

print(friends[1:])  # This gives us the element at index 1 and up "1 is included"

print(friends[:1])  # This gives us all the elements below index 1 "1 isn't included"

print(friends[1:3])  # This gives us all the elements from 1 until the last element before 3

friends.append("Hello")

print(friends)

friends.insert(0, "AHA")

print(friends)

friends[4] = "Yaz"

print(friends)

friends.pop()

friends.pop(0)

print(friends)
