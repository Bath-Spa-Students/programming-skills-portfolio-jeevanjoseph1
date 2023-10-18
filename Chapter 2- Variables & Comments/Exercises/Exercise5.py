usb_stick_price = 6
budget = 50

# Calculate the no of USB sticks she can buy
num_usb_sticks = budget // usb_stick_price

# Calculate the money left after buying USB sticks
pounds_left = budget % usb_stick_price

print("She can buy", num_usb_sticks, "USB sticks.")
print("She will have £", pounds_left, "left.")