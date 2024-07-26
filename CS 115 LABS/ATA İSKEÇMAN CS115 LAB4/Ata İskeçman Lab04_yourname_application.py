import Lab04_yourname_module

Lab04_yourname_module.findAuthor("quotes.txt","authors.txt")

cityName = input("Enter city to search: ")
distances = float(input("Enter maximum distance from city center (kms): "))

if Lab04_yourname_module.findAveragePrice("restaurants.txt", cityName, distances) > 0:
    print(f"Average price of hotels less than {distances} km from the city center of {cityName} is:{Lab04_yourname_module.findAveragePrice('restaurants.txt', cityName, distances)}")
else:
    print(f"No restaurant is Found in the the given distance for the {cityName}")

