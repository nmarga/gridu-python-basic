import json
import os
from pathlib import Path
import xml.etree.ElementTree as ET
from typing import Tuple, Dict

def city_summary_stats(json_dict: Dict) -> Tuple:
    """Returns the summary stats for a json dictionary"""
    temps = [item['temp'] for item in json_dict['hourly']]
    wind_speeds = [item['wind_speed'] for item in json_dict['hourly']]

    temp_stats = {"min_temp": round(min(temps), 2),
                  "max_temp": round(max(temps), 2),
                  "mean_temp": round(sum(temps)/len(temps), 2)}

    wind_speed_stats = {"min_wind_speed": round(min(wind_speeds), 2),
                        "max_wind_speed": round(max(wind_speeds), 2),
                        "mean_wind_speed": round(sum(wind_speeds)/len(wind_speeds), 2)}

    return temp_stats, wind_speed_stats

def country_summary_stats(summary_cities: Dict) -> Tuple:
    """Returns the summary stats for a list of tuple summaries"""

    temp_stats, wind_stats = zip(*summary_cities.values())

    # Sort the dictionary by the coresponding item values and exctract the first key
    coldest_place = sorted(summary_cities.items(),
                           key=lambda item: item[1][0]['min_temp'])[0][0]
    warmest_place = sorted(summary_cities.items(),
                           key=lambda item: item[1][0]['max_temp'], reverse=True)[0][0]
    windiest_place = sorted(summary_cities.items(),
                            key=lambda item: item[1][1]['max_wind_speed'], reverse=True)[0][0]

    temp_means = [temp_stat["mean_temp"] for temp_stat in temp_stats]

    wind_speed_means = [wind_stat["mean_wind_speed"] for wind_stat in wind_stats]

    country_temp_stats = {"coldest_place": coldest_place,
                          "warmest_place": warmest_place,
                          "mean_temp": round(sum(temp_means)/len(temp_means), 2)}

    country_wind_speed_stats = {"windiest_place": windiest_place,
                                "mean_wind_speed": round(sum(wind_speed_means)/len(wind_speed_means), 2)}

    return country_temp_stats, country_wind_speed_stats

def dict_to_summary_xml(date: str, summary_cities: Dict) -> ET.Element:
    """Convert a dictionary to an ElementTree element."""
    temp_country_summary, wind_country_summary = country_summary_stats(summary_cities)

    # Create weather element
    weather_elem = ET.Element('weather')
    weather_elem.set('country', 'Spain')
    weather_elem.set('date', date)

    # Create summary element
    summary_elem = ET.Element('summary')
    summary_elem.set('mean_temp', str(temp_country_summary['mean_temp']))
    summary_elem.set('mean_wind_speed', str(wind_country_summary['mean_wind_speed']))
    summary_elem.set('coldest_place', str(temp_country_summary['coldest_place']))
    summary_elem.set('warmest_place', str(temp_country_summary['warmest_place']))
    summary_elem.set('mean_temp', str(temp_country_summary['mean_temp']))
    summary_elem.set('windiest_place', str(wind_country_summary['windiest_place']))

    weather_elem.append(summary_elem)

    cities_elem = ET.Element('cities')

    # Create elements for each city
    for city, (summary_temp, summary_wind) in summary_cities.items():
        city_elem = ET.Element(city)
        city_elem.set('mean_temp', str(summary_temp['mean_temp']))
        city_elem.set('max_temp', str(summary_temp['max_temp']))
        city_elem.set('min_temp', str(summary_temp['min_temp']))
        city_elem.set('mean_wind_speed', str(summary_wind['mean_wind_speed']))
        city_elem.set('max_wind_speed', str(summary_wind['max_wind_speed']))
        city_elem.set('min_wind_speed', str(summary_wind['min_wind_speed']))
        cities_elem.append(city_elem)

    weather_elem.append(cities_elem)

    return weather_elem

def pretty_format_xml(element: ET.Element) -> str:
    """Returns a pretty-printed XML string for the Element."""
    ET.indent(element, space="  ")
    fomrated_string = ET.tostring(element, encoding='unicode')
    return fomrated_string

def json_to_xml(src_path: str) -> None:
    """Function to create an XML file for Spain for 2021-09-25"""
    city_stats = {}
    date = "2021-09-25"

    # Iterate through each city subfolder
    for dir_path in os.listdir(src_path):
        json_path = Path(os.path.join(src_path, dir_path))
        city_name = str(dir_path).replace(' ', '_')

        for file_path in json_path.rglob("*.json"):

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                data_dict = json.loads(content)

            print(city_summary_stats(data_dict))
            city_stats[city_name] = city_summary_stats(data_dict)

    with open('result.xml', 'w', encoding='utf-8') as f:
        f.write(pretty_format_xml(dict_to_summary_xml(date, city_stats)))

if __name__ == "__main__":
    json_to_xml('./source_data')
