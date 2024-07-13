# Scopes
# In loops and Conditions, the variables can be accessed even if they are not initialized outside of them
# But in functions, they are not accessible from outside.

if True:
    yaz = "Yaz"

while True:
    zac = "Zack"
    break

print(yaz)
print(zac)

for e in ["zack"]:
    var = e + " Farrah"

print(var)

# If we want to modify a global variable:

x = 100


def my_func():
    global x  # And even if x wasn't initialized, here we do initialize it as well
    x = 300


my_func()
print(x)
