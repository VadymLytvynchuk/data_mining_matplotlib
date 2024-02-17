from pathlib import Path
import json

def reading_json_geo():
    # Read data as a string and convert to a Python object.
    path = Path('data/all_month.geojson_2024.geojson')

    # Specify the encoding as 'utf-8'
    contents = path.read_text(encoding='utf-8')
    all_eq_data = json.loads(contents)

    # Create a more readable version of the data file.
    path = Path('data/readable_eq_data.json')
    readable_contents = json.dumps(all_eq_data, indent=4, ensure_ascii=False)

    # Specify the encoding as 'utf-8'
    path.write_text(readable_contents, encoding='utf-8')

    # Examine all earthquakes in the dataset.
    all_eq_dicts = all_eq_data['features']
    my_layout = all_eq_data['metadata'] ['title']
    print(len(all_eq_dicts))
    mags, lons, lats, hover_texts = [], [], [], []
    for eq_dict in all_eq_dicts:
        mags.append(eq_dict['properties'] ['mag'])
        lons.append(eq_dict['geometry'] ['coordinates'] [0])
        lats.append(eq_dict['geometry'] ['coordinates'] [1])
        hover_texts.append(eq_dict['properties'] ['title'])
    return lons, lats, mags, hover_texts, my_layout

#print(mags[:10])
#print(lons[:5])
#print(lats[:5])