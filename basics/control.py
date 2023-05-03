countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Iceland',
  'Switzerland',
  'Ireland',
  'Belgium',
  'Netherlands',
  'Newzland',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros']

# Loop through the countries and extract all the countries containing the word land.
for country in countries:
    if  'land' in country:
        print (country)


# This is a fruit list, reverse the order using loop.
fruits=['banana', 'orange', 'mango', 'lemon'] 

reversed_fruits = []

for i in range(len(fruits)-1, -1, -1):
   reversed_fruits.append(fruits[i])

print(reversed_fruits)

# Go to the data folder and use the countries_data.py file.
countries_data=[
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
    {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    },
    {
        "name": "Algeria",
        "capital": "Algiers",
        "languages": [
            "Arabic"
        ],
        "population": 40400000,
        "flag": "https://restcountries.eu/data/dza.svg",
        "currency": "Algerian dinar"
    },
    {
        "name": "American Samoa",
        "capital": "Pago Pago",
        "languages": [
            "English",
            "Samoan"
        ],
        "population": 57100,
        "flag": "https://restcountries.eu/data/asm.svg",
        "currency": "United State Dollar"
    }]

# What are the total number of languages in the data
sum=0
for country in countries_data:
        sum+=len(country['languages'])
        print(f"The total number of languages in the data is: {sum}")
# Find the one most spoken languages from the data
language_counts = {}
for country in countries_data:
    for language in country['languages']:
        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1

most_spoken_language = max(language_counts, key=language_counts.get)
print(f"The most spoken language is {most_spoken_language}")




# Find the  2 most populated countries in the world
populations = []
for country in countries_data:
    populations.append(country['population'])

populations.sort(reverse=True)
most_populated_countries = []
for country in countries_data:
    if country['population'] in populations[:2]:
        most_populated_countries.append(country)

print("The two most populated countries are:")
for country in most_populated_countries:
    print(f"{country['name']} (Population: {country['population']})")