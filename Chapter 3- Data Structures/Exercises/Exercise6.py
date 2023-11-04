#invite people to dinner
guests=["joseph","jojo","uthram"]
name= guests[0].title()
print(name + ", please come to dinner.")
name= guests[1].title()
print(name + ", please come to dinner.")
name= guests[2].title()
print(name + ", please come to dinner.")
#jojo can't make it to dinner
name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
#jojo can't make it to dinner invite ramez instead
del(guests[1])
guests.insert(1,"ramez")
#print invitation again
name= guests[0].title()
print(name + ", please come to dinner.")
name= guests[1].title()
print(name + ", please come to dinner.")
name= guests[2].title()
print(name + ", please come to dinner.")

# Oh no, the table won't arrive on time!
print("\nSorry, we can only invite two people to dinner.")
name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")


# There should be two people left. Let's invite them.
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")

# Empty out the list.
del(guests[0])
del(guests[0])

# Prove the list is empty.
print(guests)
