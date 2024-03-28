import requests
import re

api_key = "" # https://steamcommunity.com/dev/apikey

page = 1
offset = 0
result = []

print("1. Your input = Game (* - Random Symbol)\n2. By word in Game Name (* - Random Symbol)\n3. First symbols of Game Name\n")
search_type = int(input("Enter how want you to search: "))
print("\n")
if search_type == 1:
    search_input = input("Enter game name (* - Random Symbol): ")
elif search_type == 2:
    search_input = input("Enter word in game name (* - Random Symbol): ")
elif search_type == 3:
    starts_with = []
    while True:
        start_with = input("Enter symbol(s) with from start word: ")
        if not start_with: break
        starts_with.append(start_with.lower())

print("\n")

while True:
    print("[INFO] Requesting Page #" + str(page)) 
    page += 1

    data = requests.get(f"https://api.steampowered.com/IStoreService/GetAppList/v1/?include_games=true&max_results=50000&last_appid={offset}&key={api_key}").json()
    products = data['response']['apps']

    for product in products:
        product_name = product['name']
        product_id = product['appid'] # For DEBUG

        if product_name == "":
            continue

        words = product_name.split()
        if search_type == 1:
            pattern = "^" + re.sub(r'\*', '.', search_input) + "$" # Replace all * for . | Because . is any symbol | Add ^ Because that start of line | Add $ because that end of line | https://regex101.com/r/FsuHFN/1
        elif search_type == 2:
            pattern = re.sub(r'\*', '.', search_input)
        elif search_type == 3:
            product_name_words = product_name.split()

            end = False

            for i in range(len(product_name_words)):
                if len(product_name_words) != len(starts_with) or not product_name_words[i].lower().startswith(starts_with[i]):
                    end = True
                    break

            if not end:
                result.append(product_name)

        if search_type == 3:
            continue

        match = re.search(pattern, product_name, flags=re.IGNORECASE)

        if match:
            result.append(product_name)

    if 'last_appid' in data['response'] and data['response']['last_appid'] is not None:
        offset = data['response']['last_appid']
    else: break

print(result)
