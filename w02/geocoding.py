import geocoder


if __name__ == "__main__":

    # Forward geocoding
    g = geocoder.osm("108 North road, Acton ACT 2602")
    print(g.city, g.latlng, g.street, g.country)

    # Reverse geocoding
    b = geocoder.osm([-35.27528435, 149.12052184576413], method = "reverse")
    print(b.city)