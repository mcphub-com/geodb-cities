# GeoDB Cities MCP Server

Welcome to the GeoDB Cities MCP Server! This server provides comprehensive data about cities, regions, countries, and islands worldwide. You can filter and sort this data in various ways to tailor it to your specific needs.

## Overview

The GeoDB Cities MCP Server offers a RESTful API that provides access to extensive global geographic data. You can retrieve information about over 700,000 towns, cities, counties, and islands, which can be filtered and displayed in multiple languages. This server adheres to industry best practices to ensure a reliable and efficient service.

## Features

- **Global Data Access**: Retrieve data on cities, regions, countries, and islands from around the world.
- **Filtering Options**: Filter data by name prefix, country, location, time zone, or minimum population.
- **Multi-language Support**: Display results in various languages, including English, French, German, Italian, Portuguese, Russian, and Spanish.
- **Sorting Capabilities**: Sort results by name, country code, elevation, population, or any combination of these criteria.
- **Place Details**: Access detailed information about places, including GPS location, time zone, population, elevation, and current time, factoring in daylight savings.
- **Region and Country Data**: Retrieve information about all country regions, states, provinces, and all countries supporting a specific currency.
- **Distance Calculation**: Calculate distances between places to support location-based applications.
- **Infrastructure**: Benefit from a cloud-based load-balanced infrastructure for enhanced performance and resiliency.

## Possible Use Cases

- **User Location**: Determine a user's current place based on GPS location.
- **Autocomplete**: Implement place, region, or country name autocomplete as users type.
- **Dynamic Lists**: Populate lists of regions or cities based on user-selected countries or regions.
- **Flag Display**: Display the flag of a selected country.
- **WikiData Integration**: Use WikiData to implement use cases like retrieving a city's tourist attractions.

## Tools

The server provides a variety of tools to interact with the data:

### Administrative Divisions
- **Admin Divisions**: Find administrative divisions based on optional filters, with a minimum population of 1000.
- **Admin Divisions Near Division/Location**: Retrieve divisions near a specified location or division.
- **Admin Division Details**: Access detailed information for specific divisions, including location, population, and elevation.

### Country and Region Data
- **Countries and Country Details**: Retrieve countries and details, including the number of regions.
- **Country Regions**: Find regions within a specific country, such as states or provinces.
- **Country Region Details**: Obtain details for specific regions, including the number of cities.

### Cities and Places
- **Cities and City Details**: Access cities and their details, including location and population.
- **Cities Near City/Division/Location**: Find cities near a specified city, division, or location.
- **Places and Place Details**: Retrieve places and detailed information, including coordinates and population.

### Locale Information
- **Currencies, Languages, Locales, and Time-Zones**: Access data related to currencies, supported languages, known locales, and time-zones.

## Documentation

For detailed information on each tool and its parameters, please refer to the documentation provided within the server environment. This will guide you through the configuration and usage of each tool to best suit your requirements.

We hope you find the GeoDB Cities MCP Server a powerful and flexible tool for your geographic data needs. Enjoy exploring the world of data with us!