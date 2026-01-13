### Exercise 5: Travel Itinerary Planner

""" 
Plan travel itineraries. Destinations are a dict {city (str): list of attractions (str)}. Take a city, loop through destinations, use conditionals to select attractions starting with 'M' (e.g., museums), handle errors if city not found, store selected attractions in a set (unique), and return a tuple of (selected_attractions_set, all_cities_list). 
"""

def plan_itinerary(destinations, target_city):
    # Error handling for city not found
    # Loop through destinations
    # Conditional for attraction selection
    # Use set for selected attractions
    # Return tuple of (selected_attractions_set, all_cities_list)
    pass

print(plan_itinerary(destinations, "Paris"))  # Example call

def plan_itinerary(destinations, target_city):
    # set to store selected attractions
    selected_attractions = set()

    # error handling: city not found
    if target_city not in destinations:
        raise KeyError("Target city is not in destinations")

    # list of all cities
    all_cities_list = list(destinations.keys())

    # loop through attractions of the target city
    for attraction in destinations[target_city]:
        if attraction.startswith("M"):
            selected_attractions.add(attraction)

    # return required tuple
    return selected_attractions, all_cities_list


# example data
destinations = {
    "Paris": ["Museum of Louvre", "Eiffel Tower", "Montmartre", "Museum d'Orsay"],
    "Rome": ["Museum Vatican", "Colosseum"],
    "London": ["Museum British", "London Eye"]
}

print(plan_itinerary(destinations, "Paris"))
