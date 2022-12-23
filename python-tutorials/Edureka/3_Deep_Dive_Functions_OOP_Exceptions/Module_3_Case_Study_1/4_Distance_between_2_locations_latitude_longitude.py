import math

# distance function uses Haversine formula


def distance(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude to spherical coordinates in radians.
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Calculate the difference in latitude and longitude.
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Calculate the distance using the Haversine formula.
    a = math.sin(dlat/2)**2 + math.cos(lat1) * \
        math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))

    # Return the distance in kilometers.
    return 6371 * c


# example: Distance between London and  New York in kilometers
print(
    f"Distance between London and NY: {distance(40.7128, -74.0060, 51.5074, -0.1278)} kilometers.")
