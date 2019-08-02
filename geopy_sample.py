from geopy.geocoders import Nominatim

locator = Nominatim(user_agent="geopy_sample")
address, (latitude, longitude) = locator.geocode("Lengericher Landstr. 11b, 49078 Osnabrück")

print(f'{address}: lat={latitude}, lng={longitude}')
