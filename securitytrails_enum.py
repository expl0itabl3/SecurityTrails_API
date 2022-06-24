#!/usr/bin/env python3

import requests

apikey = "[APIKEY]"
headers = {
    "accept": "application/json",
    "apikey": apikey
}


def enum_subdomains():
    domain = input("Enter domain name: ")
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"

    # Parse subdomains
    response = requests.get(url, headers=headers)
    results = response.json()
    subdomains = [f"{i}.{domain}" for i in results["subdomains"]]

    # Write to file
    with open("subdomains.txt", "w") as opened_file:
        for i in subdomains:
            opened_file.write(f"{i}\n")

    print("Check your directory for subdomains.txt!")
    return subdomains


if __name__ == '__main__':
    enum_subdomains()
