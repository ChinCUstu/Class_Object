first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

first_name = first_name.upper()
last_name = last_name.upper()
initial_name = f"{first_name[0]}.{last_name[0]}."

address_book = first_name.capitalize() + " " + last_name.upper()

username = first_name[0].lower() + last_name.lower()
print(f"\"{initial_name}\",\"{address_book}\", and \"{username}\"")
