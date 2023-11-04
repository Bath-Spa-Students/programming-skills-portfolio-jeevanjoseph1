places_visit = ["bali", "los angles", "tokyo", "melbourne", "manali"]

# Print the list in its original order
print("Original Order:", places_visit)

# Use sorted() to print the list in alphabetical order without modifying the original list
print("Alphabetical Order:", sorted(places_visit))

# Show that the original list is still in its original order
print("Original Order:", places_visit)

# Use sorted() to print the list in reverse alphabetical order without modifying the original list
print("Reverse Alphabetical Order:", sorted(places_visit, reverse=True))

# Show that the original list is still in its original order
print("Original Order:", places_visit)

# Use reverse() to change the order of the list
places_visit.reverse()
print("Reversed Order:", places_visit)

# Use reverse() again to change the order back to its original order
places_visit.reverse()
print("Original Order:", places_visit)

# change the list to alphabetical order
places_visit.sort()
print("Sorted Alphabetical Order:", places_visit)

#  change the list to reverse alphabetical order
places_visit.sort(reverse=True)
print("Sorted Reverse Alphabetical Order:", places_visit)
