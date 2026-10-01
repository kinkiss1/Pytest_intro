FACTS_URL = "https://catfact.ninja/fact"


def get_cat_fact(http_client):
    response = http_client.get(FACTS_URL, timeout=5)
    response.raise_for_status()

    data = response.json()
    return data["fact"]
