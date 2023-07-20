import json
from dataclasses import dataclass
from typing import List

# r.json format
[{
"name": "Bistro Bananas",
"category": "Pizza",
"lng": 18.0752697,
"lat": 59.31179759999999,
"id": "ChIJCSFExvB3X0YRK-RXzK3XnNs"
},]

# Target
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "name": "h",
        "category": "2",
        "id": 4
      },
      "geometry": {
        "coordinates": [
          18.045464678453754,
          59.33260996670475
        ],
        "type": "Point"
      }
    }
  ]
}

@dataclass
class Place:
    name: str
    category: str
    id: int
    lat: float
    lng: float
    

with open("r.json", "r") as f:
    data = json.load(f)
    places: List[Place] = []
    for place in data:
        places.append(Place(place["name"], place["category"], place["id"], place["lat"], place["lng"]))

    geojson = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        geojson["features"].append({
            "type": "Feature",
            "properties": {
                "name": place.name,
                "category": place.category,
                "id": place.id
            },
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            }
        })

    with open("geo.json", "w") as f:
        json.dump(geojson, f, ensure_ascii=False, indent=4)

