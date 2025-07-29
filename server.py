import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/wirefreethought/api/geodb-cities'

mcp = FastMCP('geodb-cities')

@mcp.tool()
def admin_divisions(location: Annotated[Union[str, None], Field(description='Only divisions near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD')] = None,
                    radius: Annotated[Union[int, float, None], Field(description='The location radius within which to find divisions Default: 0')] = None,
                    distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance to use: MI | KM')] = None,
                    countryIds: Annotated[Union[str, None], Field(description='Only divisions in these countries (comma-delimited country codes or WikiData ids)')] = None,
                    excludedCountryIds: Annotated[Union[str, None], Field(description='Only divisions NOT in these countries (comma-delimited country codes or WikiData ids)')] = None,
                    timeZoneIds: Annotated[Union[str, None], Field(description='Only divisions in these time-zones')] = None,
                    minPopulation: Annotated[Union[int, float, None], Field(description='Only divisions having at least this population Default: 0')] = None,
                    maxPopulation: Annotated[Union[int, float, None], Field(description='Only divisions having no more than this population Default: 0')] = None,
                    namePrefix: Annotated[Union[str, None], Field(description='Only divisions whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                    namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                    languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                    asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                    hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                    includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                    limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
                    offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results Default: 0')] = None,
                    sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = countryCode | elevation | name | population')] = None) -> dict: 
    '''Find administrative divisions, filtering by optional criteria. If no criteria are set, you will get back all known divisions with a population of at least 1000'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'location': location,
        'radius': radius,
        'distanceUnit': distanceUnit,
        'countryIds': countryIds,
        'excludedCountryIds': excludedCountryIds,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def admin_divisions_near_division(radius: Annotated[Union[int, float], Field(description='The location radius within which to find divisions Default: 100')],
                                  distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance to use: MI | KM')] = None,
                                  countryIds: Annotated[Union[str, None], Field(description='Only divisions in these countries (comma-delimited country codes or WikiData ids)')] = None,
                                  excludedCountryIds: Annotated[Union[str, None], Field(description='Only divisions NOT in these countries (comma-delimited country codes or WikiData ids)')] = None,
                                  timeZoneIds: Annotated[Union[str, None], Field(description='Only divisions in these time-zones')] = None,
                                  minPopulation: Annotated[Union[int, float, None], Field(description='Only divisions having at least this population Default: 0')] = None,
                                  maxPopulation: Annotated[Union[int, float, None], Field(description='Only divisions having no more than this population Default: 0')] = None,
                                  namePrefix: Annotated[Union[str, None], Field(description='Only divisions whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                                  namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                                  languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                                  asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                                  hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                                  includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                                  limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
                                  offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results Default: 0')] = None,
                                  sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = countryCode | elevation | name | population')] = None) -> dict: 
    '''Get divisions near the given administrative division, filtering by optional criteria.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions/Q104994/nearbyDivisions'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'radius': radius,
        'distanceUnit': distanceUnit,
        'countryIds': countryIds,
        'excludedCountryIds': excludedCountryIds,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def admin_divisions_near_location(radius: Annotated[str, Field(description='The location radius within which to find divisions')],
                                  distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance to use: MI | KM')] = None,
                                  countryIds: Annotated[Union[str, None], Field(description='Only divisions in these countries (comma-delimited country codes or WikiData ids)')] = None,
                                  excludedCountryIds: Annotated[Union[str, None], Field(description='Only divisions NOT in these countries (comma-delimited country codes or WikiData ids)')] = None,
                                  timeZoneIds: Annotated[Union[str, None], Field(description='Only divisions in these time-zones')] = None,
                                  minPopulation: Annotated[Union[int, float, None], Field(description='Only divisions having at least this population Default: 0')] = None,
                                  maxPopulation: Annotated[Union[int, float, None], Field(description='Only divisions having no more than this population Default: 0')] = None,
                                  namePrefix: Annotated[Union[str, None], Field(description='Only divisions whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                                  namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                                  languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                                  asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                                  hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                                  includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any divisions marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                                  limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
                                  offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results Default: 0')] = None,
                                  sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = countryCode | elevation | name | population')] = None) -> dict: 
    '''Get administrative divisions near the given location, filtering by optional criteria.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/locations/33.832213-118.387099/nearbyDivisions'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'radius': radius,
        'distanceUnit': distanceUnit,
        'countryIds': countryIds,
        'excludedCountryIds': excludedCountryIds,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def admin_division_details(languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                           asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None) -> dict: 
    '''Get the details for a specific administrative division, including location coordinates, population, and elevation above sea-level (if available).'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions/Q104994'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'languageCode': languageCode,
        'asciiMode': asciiMode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def countries(currencyCode: Annotated[Union[str, None], Field(description='Only countries supporting this currency')] = None,
              namePrefix: Annotated[Union[str, None], Field(description='Only countries whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
              namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
              languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
              asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
              hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
              limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve')] = None,
              offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset index into the results')] = None,
              sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD where SORT_FIELD = code | name')] = None) -> dict: 
    '''Find countries, filtering by optional criteria. If no criteria are set, you will get back all known countries.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/countries'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'currencyCode': currencyCode,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def country_details(languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                    asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None) -> dict: 
    '''Get the details for a specific country, including number of regions.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'languageCode': languageCode,
        'asciiMode': asciiMode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def country_places(types: Annotated[Union[str, None], Field(description='Only cities for these types (comma-delimited): ADM2 | CITY | ISLAND')] = None,
                   timeZoneIds: Annotated[Union[str, None], Field(description='Only places in these time-zones')] = None,
                   minPopulation: Annotated[Union[int, float, None], Field(description='Only places having at least this population')] = None,
                   maxPopulation: Annotated[Union[int, float, None], Field(description='Only places having no more than this population Default: 0')] = None,
                   namePrefix: Annotated[Union[str, None], Field(description='Only places whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                   namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                   languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                   asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                   hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                   includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any cities marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                   limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve')] = None,
                   offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results')] = None,
                   sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = elevation | name | population')] = None) -> dict: 
    '''Get the places in the given country.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US/places'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'types': types,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def country_regions(namePrefix: Annotated[Union[str, None], Field(description='Only regions whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                    namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                    languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                    asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                    hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                    limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
                    offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset index into the results Default: 0')] = None,
                    sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD where SORT_FIELD = fipsCode | isoCode | name')] = None) -> dict: 
    '''Find regions in a specific country, filtering by optional criteria. Regions can be states, provinces, districts, or otherwise major political divisions.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US/regions'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def country_region_details(languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                           asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None) -> dict: 
    '''Get the details of a specific country region, including number of cities.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US/regions/CA'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'languageCode': languageCode,
        'asciiMode': asciiMode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def country_region_cities(types: Annotated[Union[str, None], Field(description='Only cities for these types (comma-delimited): CITY | ADM2')] = None,
                          timeZoneIds: Annotated[Union[str, None], Field(description='Only cities in these time-zones')] = None,
                          minPopulation: Annotated[Union[int, float, None], Field(description='Only cities having at least this population')] = None,
                          maxPopulation: Annotated[Union[int, float, None], Field(description='Only cities having no more than this population Default: 0')] = None,
                          namePrefix: Annotated[Union[str, None], Field(description='Only cities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                          namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                          languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                          asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                          hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                          includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any cities marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                          limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve')] = None,
                          offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results')] = None,
                          sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = elevation | name | population')] = None) -> dict: 
    '''Get the cities in the given region.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US/regions/CA/cities'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'types': types,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def country_region_divisions(minPopulation: Annotated[Union[int, float, None], Field(description='Only cities having at least this population')] = None,
                             maxPopulation: Annotated[Union[int, float, None], Field(description='Only divisions having no more than this population Default: 0')] = None,
                             namePrefix: Annotated[Union[str, None], Field(description='Only divisions whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                             namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                             languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                             asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                             hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                             includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any cities marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                             limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve')] = None,
                             offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results')] = None,
                             sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = elevation | name | population')] = None) -> dict: 
    '''Get the administrative divisions in the given region.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US/regions/CA/adminDivisions'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def country_region_places(types: Annotated[Union[str, None], Field(description='Only cities for these types (comma-delimited): ADM2 | CITY | ISLAND')] = None,
                          timeZoneIds: Annotated[Union[str, None], Field(description='Only places in these time-zones')] = None,
                          minPopulation: Annotated[Union[int, float, None], Field(description='Only places having at least this population')] = None,
                          maxPopulation: Annotated[Union[int, float, None], Field(description='Only places having no more than this population Default: 0')] = None,
                          namePrefix: Annotated[Union[str, None], Field(description='Only places whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                          namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                          languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                          asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                          hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                          includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any cities marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                          limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve')] = None,
                          offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results')] = None,
                          sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = elevation | name | population')] = None) -> dict: 
    '''Get the places in the given region.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/countries/US/regions/CA/places'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'types': types,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def cities(types: Annotated[Union[str, None], Field(description='Only cities for these types (comma-delimited): CITY | ADM2')] = None,
           location: Annotated[Union[str, None], Field(description='Only cities near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD')] = None,
           radius: Annotated[Union[int, float, None], Field(description='The location radius within which to find cities Default: 0')] = None,
           distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance to use: MI | KM')] = None,
           countryIds: Annotated[Union[str, None], Field(description='Only cities in these countries (comma-delimited country codes or WikiData ids)')] = None,
           excludedCountryIds: Annotated[Union[str, None], Field(description='Only cities NOT in these countries (comma-delimited country codes or WikiData ids)')] = None,
           timeZoneIds: Annotated[Union[str, None], Field(description='Only cities in these time-zones')] = None,
           minPopulation: Annotated[Union[int, float, None], Field(description='Only cities having at least this population Default: 0')] = None,
           maxPopulation: Annotated[Union[int, float, None], Field(description='Only cities having no more than this population Default: 0')] = None,
           namePrefix: Annotated[Union[str, None], Field(description='Only cities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
           namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested.')] = None,
           languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
           asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
           hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
           includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any cities marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
           limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
           offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results Default: 0')] = None,
           sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = countryCode | elevation | name | population')] = None) -> dict: 
    '''Find cities, filtering by optional criteria. If no criteria are set, you will get back all known cities with a population of at least 1000.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/cities'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'types': types,
        'location': location,
        'radius': radius,
        'distanceUnit': distanceUnit,
        'countryIds': countryIds,
        'excludedCountryIds': excludedCountryIds,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def cities_near_city(radius: Annotated[Union[int, float], Field(description='The location radius within which to find cities Default: 100')],
                     types: Annotated[Union[str, None], Field(description='Only cities for these types (comma-delimited): CITY | ADM2')] = None,
                     distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance to use: MI | KM')] = None,
                     countryIds: Annotated[Union[str, None], Field(description='Only cities in these countries (comma-delimited country codes or WikiData ids)')] = None,
                     excludedCountryIds: Annotated[Union[str, None], Field(description='Only cities NOT in these countries (comma-delimited country codes or WikiData ids)')] = None,
                     timeZoneIds: Annotated[Union[str, None], Field(description='Only cities in these time-zones')] = None,
                     minPopulation: Annotated[Union[int, float, None], Field(description='Only cities having at least this population Default: 0')] = None,
                     maxPopulation: Annotated[Union[int, float, None], Field(description='Only cities having no more than this population Default: 0')] = None,
                     namePrefix: Annotated[Union[str, None], Field(description='Only cities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                     namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                     languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                     asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                     hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                     includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any cities marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                     limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
                     offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results Default: 0')] = None,
                     sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = countryCode | elevation | name | population')] = None) -> dict: 
    '''Get cities near the given city, filtering by optional criteria.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q60/nearbyCities'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'radius': radius,
        'types': types,
        'distanceUnit': distanceUnit,
        'countryIds': countryIds,
        'excludedCountryIds': excludedCountryIds,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def cities_near_division(radius: Annotated[Union[int, float], Field(description='The location radius within which to find cities Default: 100')],
                         types: Annotated[Union[str, None], Field(description='Only cities for these types (comma-delimited): CITY | ADM2')] = None,
                         distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance to use: MI | KM')] = None,
                         countryIds: Annotated[Union[str, None], Field(description='Only cities in these countries (comma-delimited country codes or WikiData ids)')] = None,
                         excludedCountryIds: Annotated[Union[str, None], Field(description='Only cities NOT in these countries (comma-delimited country codes or WikiData ids)')] = None,
                         timeZoneIds: Annotated[Union[str, None], Field(description='Only cities in these time-zones')] = None,
                         minPopulation: Annotated[Union[int, float, None], Field(description='Only cities having at least this population Default: 0')] = None,
                         maxPopulation: Annotated[Union[int, float, None], Field(description='Only cities having no more than this population Default: 0')] = None,
                         namePrefix: Annotated[Union[str, None], Field(description='Only cities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                         namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                         languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                         asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                         hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                         includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any cities marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                         limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
                         offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results Default: 0')] = None,
                         sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = countryCode | elevation | name | population')] = None) -> dict: 
    '''Get cities near the given administrative division, filtering by optional criteria.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions/Q104994/nearbyCities'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'radius': radius,
        'types': types,
        'distanceUnit': distanceUnit,
        'countryIds': countryIds,
        'excludedCountryIds': excludedCountryIds,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def cities_near_location(radius: Annotated[str, Field(description='The location radius within which to find cities')],
                         types: Annotated[Union[str, None], Field(description='Only cities for these types (comma-delimited): CITY | ADM2')] = None,
                         distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance to use: MI | KM')] = None,
                         countryIds: Annotated[Union[str, None], Field(description='Only cities in these countries (comma-delimited country codes or WikiData ids)')] = None,
                         excludedCountryIds: Annotated[Union[str, None], Field(description='Only cities NOT in these countries (comma-delimited country codes or WikiData ids)')] = None,
                         timeZoneIds: Annotated[Union[str, None], Field(description='Only cities in these time-zones')] = None,
                         minPopulation: Annotated[Union[int, float, None], Field(description='Only cities having at least this population Default: 0')] = None,
                         maxPopulation: Annotated[Union[int, float, None], Field(description='Only cities having no more than this population Default: 0')] = None,
                         namePrefix: Annotated[Union[str, None], Field(description='Only cities whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                         namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                         languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                         asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                         hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                         includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any cities marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                         limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
                         offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results Default: 0')] = None,
                         sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = countryCode | elevation | name | population')] = None) -> dict: 
    '''Get cities near the given location, filtering by optional criteria.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/locations/33.832213-118.387099/nearbyCities'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'radius': radius,
        'types': types,
        'distanceUnit': distanceUnit,
        'countryIds': countryIds,
        'excludedCountryIds': excludedCountryIds,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def city_details(languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                 asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None) -> dict: 
    '''Get the details for a specific city, including location coordinates, population, and elevation above sea-level (if available).'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q60'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'languageCode': languageCode,
        'asciiMode': asciiMode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def city_located_in() -> dict: 
    '''Get the details for the containing populated place (e.g., its county or other administrative division), including location coordinates, population, and elevation above sea-level (if available). Currently, this data is highly dependent on whether the Wikidata **locatedIn** relation is properly defined. If you see an issue, please propose a change to the corresponding Wikidata entry.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q65/locatedIn'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def city_date_time() -> dict: 
    '''Get the city current date-time in ISO-6801 format: yyyyMMdd'T'HHmmssZ'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q60/dateTime'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def city_distance(fromCityId: Annotated[Union[str, None], Field(description='The distance from this city ')] = None,
                  distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance: KM | MI [default] ')] = None,
                  toCityId: Annotated[Union[str, None], Field(description='The distance to this city ')] = None) -> dict: 
    '''Gets the distance to the given city.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/cities/Q65/distance'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'fromCityId': fromCityId,
        'distanceUnit': distanceUnit,
        'toCityId': toCityId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def city_time() -> dict: 
    '''Get the city current time in ISO-8601 format: HHmmss.SSSZ'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/cities/%7Bcityid%7D/time'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def places(types: Annotated[Union[str, None], Field(description='Only places for these types (comma-delimited): ADM2 | CITY | ISLAND')] = None,
           location: Annotated[Union[str, None], Field(description='Only places near this location. Latitude/longitude in ISO-6709 format: ±DD.DDDD±DDD.DDDD')] = None,
           radius: Annotated[Union[int, float, None], Field(description='The location radius within which to find places Default: 0')] = None,
           distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance to use: MI | KM')] = None,
           countryIds: Annotated[Union[str, None], Field(description='Only places in these countries (comma-delimited country codes or WikiData ids)')] = None,
           excludedCountryIds: Annotated[Union[str, None], Field(description='Only places NOT in these countries (comma-delimited country codes or WikiData ids)')] = None,
           timeZoneIds: Annotated[Union[str, None], Field(description='Only places in these time-zones')] = None,
           minPopulation: Annotated[Union[int, float, None], Field(description='Only places having at least this population Default: 0')] = None,
           maxPopulation: Annotated[Union[int, float, None], Field(description='Only places having no more than this population Default: 0')] = None,
           namePrefix: Annotated[Union[str, None], Field(description='Only places whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
           namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested.')] = None,
           includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any places marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
           languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
           asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
           hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
           limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
           offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results Default: 0')] = None,
           sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = countryCode | elevation | name | population')] = None) -> dict: 
    '''Find places, filtering by optional criteria. If no criteria are set, you will get back all known places.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/places'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'types': types,
        'location': location,
        'radius': radius,
        'distanceUnit': distanceUnit,
        'countryIds': countryIds,
        'excludedCountryIds': excludedCountryIds,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'includeDeleted': includeDeleted,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def places_near_location(radius: Annotated[str, Field(description='The location radius within which to find places')],
                         types: Annotated[Union[str, None], Field(description='Only places for these types (comma-delimited): ADM2 | CITY | ISLAND')] = None,
                         distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance to use: MI | KM')] = None,
                         countryIds: Annotated[Union[str, None], Field(description='Only places in these countries (comma-delimited country codes or WikiData ids)')] = None,
                         excludedCountryIds: Annotated[Union[str, None], Field(description='Only places NOT in these countries (comma-delimited country codes or WikiData ids)')] = None,
                         timeZoneIds: Annotated[Union[str, None], Field(description='Only places in these time-zones')] = None,
                         minPopulation: Annotated[Union[int, float, None], Field(description='Only places having at least this population Default: 0')] = None,
                         maxPopulation: Annotated[Union[int, float, None], Field(description='Only places having no more than this population Default: 0')] = None,
                         namePrefix: Annotated[Union[str, None], Field(description='Only places whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                         namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                         languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                         asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                         hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                         includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any places marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                         limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
                         offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results Default: 0')] = None,
                         sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = countryCode | elevation | name | population')] = None) -> dict: 
    '''Get places near the given location, filtering by optional criteria.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/locations/33.832213-118.387099/nearbyPlaces'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'radius': radius,
        'types': types,
        'distanceUnit': distanceUnit,
        'countryIds': countryIds,
        'excludedCountryIds': excludedCountryIds,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'limit': limit,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def places_near_place(radius: Annotated[Union[int, float], Field(description='The location radius within which to find places Default: 0')],
                      types: Annotated[Union[str, None], Field(description='Only places for these types (comma-delimited): ADM2 | CITY | ISLAND')] = None,
                      distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance to use: MI | KM')] = None,
                      countryIds: Annotated[Union[str, None], Field(description='Only places in these countries (comma-delimited country codes or WikiData ids)')] = None,
                      excludedCountryIds: Annotated[Union[str, None], Field(description='Only places NOT in these countries (comma-delimited country codes or WikiData ids)')] = None,
                      timeZoneIds: Annotated[Union[str, None], Field(description='Only places in these time-zones')] = None,
                      minPopulation: Annotated[Union[int, float, None], Field(description='Only places having at least this population Default: 0')] = None,
                      maxPopulation: Annotated[Union[int, float, None], Field(description='Only places having no more than this population Default: 0')] = None,
                      namePrefix: Annotated[Union[str, None], Field(description='Only places whose names start with this prefix. If languageCode is set, the prefix will be matched on the name as it appears in that language.')] = None,
                      namePrefixDefaultLangResults: Annotated[Union[bool, None], Field(description='When name-prefix matching, whether or not to match on names in the default language if a non-default language is requested')] = None,
                      languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                      asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None,
                      hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
                      includeDeleted: Annotated[Union[str, None], Field(description='Whether to include any places marked deleted: ALL | SINCE_YESTERDAY | SINCE_LAST_WEEK | NONE')] = None,
                      offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset into the results Default: 0')] = None,
                      sort: Annotated[Union[str, None], Field(description='How to sort the results. Format: ±SORT_FIELD,±SORT_FIELD where SORT_FIELD = countryCode | elevation | name | population')] = None) -> dict: 
    '''Get places near the given place, filtering by optional criteria.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/places/%7BplaceId%7D/nearbyPlaces'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'radius': radius,
        'types': types,
        'distanceUnit': distanceUnit,
        'countryIds': countryIds,
        'excludedCountryIds': excludedCountryIds,
        'timeZoneIds': timeZoneIds,
        'minPopulation': minPopulation,
        'maxPopulation': maxPopulation,
        'namePrefix': namePrefix,
        'namePrefixDefaultLangResults': namePrefixDefaultLangResults,
        'languageCode': languageCode,
        'asciiMode': asciiMode,
        'hateoasMode': hateoasMode,
        'includeDeleted': includeDeleted,
        'offset': offset,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def place_details(languageCode: Annotated[Union[str, None], Field(description='Display results in this language')] = None,
                  asciiMode: Annotated[Union[bool, None], Field(description='Display results using ASCII characters')] = None) -> dict: 
    '''Get the details for a specific place, including location coordinates, population, and elevation above sea-level (if available).'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/places/%7BplaceId%7D'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'languageCode': languageCode,
        'asciiMode': asciiMode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def place_located_in() -> dict: 
    '''Get the details for the containing populated place (e.g., its county or other administrative division), including location coordinates, population, and elevation above sea-level (if available). Currently, this data is highly dependent on whether the Wikidata **locatedIn** relation is properly defined. If you see an issue, please propose a change to the corresponding Wikidata entry.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/places/%7BplaceId%7D/locatedIn'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def place_date_time() -> dict: 
    '''Get this place's current date-time in ISO-6801 format: yyyyMMdd'T'HHmmssZ'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/places/%7BplaceId%7D/dateTime'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def place_distance(distanceUnit: Annotated[Union[str, None], Field(description='The unit of distance: KM | MI [default] ')] = None,
                   toPlaceId: Annotated[Union[str, None], Field(description='The distance to this place ')] = None) -> dict: 
    '''Gets this place's distance to the given place.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/places/%7BplaceId%7D/distance'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'distanceUnit': distanceUnit,
        'toPlaceId': toPlaceId,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def place_time() -> dict: 
    '''Get this place's current time in ISO-8601 format: HHmmss.SSSZ'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/geo/places/%7BplaceId%7D/time'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def currencies(countryId: Annotated[Union[str, None], Field(description='Only currencies supported by this country')] = None,
               limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
               offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset index into the results Default: 0')] = None,
               hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None) -> dict: 
    '''Get currencies, filtering by optional criteria. If no criteria are set, you will get back all known currencies.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/locale/currencies'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'countryId': countryId,
        'limit': limit,
        'offset': offset,
        'hateoasMode': hateoasMode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def languages(offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset index into the results')] = None,
              hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
              limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None) -> dict: 
    '''Get all supported languages'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/locale/languages'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'offset': offset,
        'hateoasMode': hateoasMode,
        'limit': limit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def locales(limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve')] = None,
            hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None,
            offset: Annotated[Union[int, float, None], Field(description='The zero-ary offset index into the results')] = None) -> dict: 
    '''Get all known locales.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/locale/locales'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'hateoasMode': hateoasMode,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_zones(limit: Annotated[Union[int, float, None], Field(description='The maximum number of results to retrieve Default: 0')] = None,
               offset: Annotated[Union[str, None], Field(description='The zero-ary offset index into the results')] = None,
               hateoasMode: Annotated[Union[bool, None], Field(description='Include HATEOAS-style links in results')] = None) -> dict: 
    '''Get all known time-zones.'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/locale/timezones'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'offset': offset,
        'hateoasMode': hateoasMode,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_zone() -> dict: 
    '''Get the time-zone current time in ISO-6801 format: HHmmss.SSSZ'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/locale/timezones/America__Los_Angeles'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_zone_date_time() -> dict: 
    '''Get the timezone current date-time in ISO-6801 format: yyyyMMdd'T'HHmmssZ'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/locale/timezones/America__Los_Angeles/dateTime'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def time_zone_time() -> dict: 
    '''Get the time-zone current time in ISO-6801 format: HHmmss.SSSZ'''
    url = 'https://wft-geo-db.p.rapidapi.com/v1/locale/timezones/America__Los_Angeles/time'
    headers = {'x-rapidapi-host': 'wft-geo-db.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
