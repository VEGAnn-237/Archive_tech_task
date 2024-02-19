from bs4 import BeautifulSoup
import requests
import json


def get_pokemon_image_url(pokemon):
    img = pokemon.findChild('img')
    dirty_src = img['srcset'].split(', ')[-1]
    src = dirty_src.split(' ')[0]
    return src


def get_next_page_url(soup):
    next_page_nums = soup.findAll('a', class_='next page-numbers')
    if not next_page_nums:
        return None
    else:
        return next_page_nums[0]['href']


def scrape_all_pages(url):
    pokemons_count = 0
    pokemons_list = []

    while True:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        all_pokemons = soup.findAll('ul', class_='products columns-4')
        for pokemon in all_pokemons[0]:
            if pokemon.text.strip():
                pokemons_count += 1
                characteristics = pokemon.text.strip().splitlines()
                pokemon_name = characteristics[0]
                pokemon_price = characteristics[1][1:]
                pokemon_image_url = get_pokemon_image_url(pokemon)

                pokemons_list.append({"id": pokemons_count,
                                      "name": pokemon_name,
                                      "price": pokemon_price,
                                      "image_url": pokemon_image_url})

        url = get_next_page_url(soup)
        if not url:
            break

    # return pokemons_list
    return json.dumps(pokemons_list, indent=4)