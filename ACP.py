weather = input("Pick a Weather(Say 'sunny' or 'rainy')")
weatherl = weather.lower()

if weatherl == "sunny":
    print("So Rohan would just wear a t-shirt")
elif weather == "rainy":
    print("So Rohan would take an umbrella and wear a jacket.")
else:
    print("Say sunny or rainy but don't worry about it being lower or upper case")