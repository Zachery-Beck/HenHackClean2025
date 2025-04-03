"""
This module provides functions to interact with the 
NPPES API to search for healthcare providers based on 
location and taxonomy.

Functions:
    search_providers(postal_code, taxonomy_description): 
        Searches for providers using the NPPES API. 
    get_healthcare_info(location, taxonomy): 
    Retrieves healthcare provider information based on location and taxonomy.
"""

import requests

def search_providers(postal_code: str, taxonomy_description: str):
    """
    Searches for providers using the NPPES API given a postal_code and taxonomy description.

    Args:
        postal_code (str): The postal code to search for providers.
        taxonomy_description (str): The taxonomy description to search for providers.

    Returns:
        dict: The JSON response from the NPPES API if the request is successful.
        None: If an error occurs during the request.
    """
    url = "https://npiregistry.cms.hhs.gov/api/"
    params = {
        "version": "2.1",
        "postal_code": postal_code,
        "taxonomy_description": taxonomy_description,
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raises an HTTPError if the HTTP request returned an unsuccessful status code.
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def get_healthcare_info(location: str, taxonomy: str):
    """
    Get healthcare provider information based on location and taxonomy.

    Args:
        location (str): The location to search for providers.
        taxonomy (str): The taxonomy to search for providers.

    Returns:
        str: A formatted string containing the provider 
        information, or a message indicating no providers were found.
    """
    taxonomy = taxonomy.strip("\n")
    data = search_providers(location, taxonomy)
    if not data or "results" not in data or not data["results"]:
        return "No providers found."

    provider_list = []
    for prov in data["results"]:
        basic_info = prov.get("basic", {})
        full_name = f"{basic_info.get('first_name', 'Not available')} " \
                    f"{basic_info.get('last_name', 'Not available')}".strip()
        if not full_name.strip():
            continue  # Skip if name is not available

        addresses = prov.get("addresses", [])
        if addresses:
            primary = addresses[0]
            location_info = f"{primary.get('address_1', 'Not available')}, " \
                            f"{primary.get('city', 'Not available')}, " \
                            f"{primary.get('state', 'Not available')} " \
                            f"{primary.get('postal_code', 'Not available')}"
            telephone_number = primary.get("telephone_number", "Not available")
        else:
            location_info = "No address provided."
            telephone_number = "Not available"

        endpoints = prov.get("endpoints", [])
        if endpoints:
            email = endpoints[0].get("endpoint", "Not available")
        else:
            email = "Not available"

        provider_info = f"""
        Name: {full_name}
        Location: {location_info}
        Phone: {telephone_number}
        Email: {email}
        """
        provider_list.append(provider_info.strip())
    # Join the provider list into one big string with new lines
    provider_string = "\n\n".join(provider_list)
    return provider_string

# Example usage
if __name__ == "__main__":
    PROVIDERS = get_healthcare_info("16870", "Orthopedics")
    print(PROVIDERS)
