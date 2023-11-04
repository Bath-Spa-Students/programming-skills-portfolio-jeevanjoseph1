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
