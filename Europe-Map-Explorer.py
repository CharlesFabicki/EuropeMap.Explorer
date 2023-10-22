import cv2
import numpy as np

# Dictionary with country information
countries_data = {
    "Poland": "Capital: Warsaw, Population: 41 million, Currency: Polish Zloty (PLN), Area: 322,575 sq km, Languages: Polish, Tourist Attractions: Wawel Castle, Old Town of Krakow.",
    "Germany": "Capital: Berlin, Population: 83 million, Currency: Euro (EUR), Area: 357,022 sq km, Languages: German, Tourist Attractions: Brandenburg Gate, Neuschwanstein Castle.",
    "Italy": "Capital: Rome, Population: 60 million, Currency: Euro (EUR), Area: 302,073 sq km, Languages: Italian, Tourist Attractions: Colosseum, Leaning Tower of Pisa.",
    "Iceland": "Capital: Reykjavik, Population: 0.4 million, Currency: Icelandic Krona (ISK), Area: 103,000 sq km, Languages: Icelandic, Tourist Attractions: Blue Lagoon, Gullfoss Waterfall.",
    "Turkey": "Capital: Ankara, Population: 84 million, Currency: Turkish Lira (TRY), Area: 783,562 sq km, Languages: Turkish, Tourist Attractions: Hagia Sophia, Cappadocia.",
    "Russia": "Capital: Moscow, Population: 146 million, Currency: Russian Ruble (RUB), Area: 17,098,242 sq km, Languages: Russian, Tourist Attractions: Red Square, Hermitage Museum.",
    "Russia Kaliningrad Oblast": "Capital: Kaliningrad, Population: 1 million, Currency: Russian Ruble (RUB), Area: 15,100 sq km, Languages: Russian, Tourist Attractions: Konigsberg Cathedral, Curonian Spit.",
    "Ukraine": "Capital: Kyiv, Population: 37 million, Currency: Ukrainian Hryvnia (UAH), Area: 603,500 sq km, Languages: Ukrainian, Tourist Attractions: Kyiv Pechersk Lavra, Lviv Old Town.",
    "Belarus": "Capital: Minsk, Population: 9.5 million, Currency: Belarusian Ruble (BYN), Area: 207,600 sq km, Languages: Belarusian, Russian, Tourist Attractions: Mir Castle, Bialowieza Forest.",
    "Spain": "Capital: Madrid, Population: 47 million, Currency: Euro (EUR), Area: 505,990 sq km, Languages: Spanish, Tourist Attractions: Sagrada Familia, Alhambra.",
    "Albania": "Capital: Tirana, Population: 2.8 million, Currency: Albanian Lek (ALL), Area: 28,748 sq km, Languages: Albanian, Tourist Attractions: Gjirokaster, Butrint National Park.",
    "United Kingdom": "Capital: London, Population: 66 million, Currency: British Pound (GBP), Area: 243,610 sq km, Languages: English, Tourist Attractions: Buckingham Palace, Tower of London.",
    "Austria": "Capital: Vienna, Population: 9 million, Currency: Euro (EUR), Area: 83,879 sq km, Languages: German, Tourist Attractions: Schönbrunn Palace, Belvedere Palace.",
    "Belgium": "Capital: Brussels, Population: 11 million, Currency: Euro (EUR), Area: 30,528 sq km, Languages: Dutch, French, German, Tourist Attractions: Grand Place, Atomium.",
    "Bulgaria": "Capital: Sofia, Population: 7 million, Currency: Bulgarian Lev (BGN), Area: 110,879 sq km, Languages: Bulgarian, Tourist Attractions: Rila Monastery, Plovdiv Old Town.",
    "Croatia": "Capital: Zagreb, Population: 4 million, Currency: Euro (EUR), Area: 56,594 sq km, Languages: Croatian, Tourist Attractions: Dubrovnik Old Town, Plitvice Lakes.",
    "Cyprus": "Capital: Nicosia, Population: 1.2 million, Currency: Euro (EUR), Area: 9,251 sq km, Languages: Greek, Turkish, Tourist Attractions: Petra tou Romiou, Kykkos Monastery.",
    "Czech Republic": "Capital: Prague, Population: 10.5 million, Currency: Czech Koruna (CZK), Area: 78,866 sq km, Languages: Czech, Tourist Attractions: Prague Castle, Charles Bridge.",
    "Denmark": "Capital: Copenhagen, Population: 5.8 million, Currency: Danish Krone (DKK), Area: 42,952 sq km, Languages: Danish, Tourist Attractions: Tivoli Gardens, The Little Mermaid.",
    "Estonia": "Capital: Tallinn, Population: 1.3 million, Currency: Euro (EUR), Area: 45,227 sq km, Languages: Estonian, Tourist Attractions: Tallinn Old Town, Lahemaa National Park.",
    "Finland": "Capital: Helsinki, Population: 5.5 million, Currency: Euro (EUR), Area: 338,462 sq km, Languages: Finnish, Tourist Attractions: Suomenlinna, Rovaniemi (Santa Claus Village).",
    "France": "Capital: Paris, Population: 67 million, Currency: Euro (EUR), Area: 551,695 sq km, Languages: French, Tourist Attractions: Eiffel Tower, Louvre Museum.",
    "Greece": "Capital: Athens, Population: 10 million, Currency: Euro (EUR), Area: 131,957 sq km, Languages: Greek, Tourist Attractions: Acropolis of Athens, Santorini.",
    "Netherlands": "Capital: Amsterdam, Population: 17.5 million, Currency: Euro (EUR), Area: 41,850 sq km, Languages: Dutch, Tourist Attractions: Rijksmuseum, Keukenhof Gardens.",
    "Ireland": "Capital: Dublin, Population: 5 million, Currency: Euro (EUR), Area: 84,421 sq km, Languages: English, Irish, Tourist Attractions: Cliffs of Moher, Guinness Storehouse.",
    "Lithuania": "Capital: Vilnius, Population: 2.7 million, Currency: Euro (EUR), Area: 65,300 sq km, Languages: Lithuanian, Tourist Attractions: Trakai Island Castle, Hill of Crosses.",
    "Luxembourg": "Capital: Luxembourg, Population: 0.6 million, Currency: Euro (EUR), Area: 2,586 sq km, Languages: Luxembourgish, French, German, Tourist Attractions: Luxembourg City, Vianden Castle.",
    "Latvia": "Capital: Riga, Population: 2 million, Currency: Euro (EUR), Area: 64,589 sq km, Languages: Latvian, Tourist Attractions: Riga Old Town, Jurmala Beach.",
    "Malta": "Capital: Valletta, Population: 0.5 million, Currency: Euro (EUR), Area: 316 sq km, Languages: Maltese, English, Tourist Attractions: Valletta's historic sites, Blue Grotto.",
    "Portugal": "Capital: Lisbon, Population: 10 million, Currency: Euro (EUR), Area: 92,090 sq km, Languages: Portuguese, Tourist Attractions: Belem Tower, Douro Valley.",
    "Romania": "Capital: Bucharest, Population: 19 million, Currency: Romanian Leu (RON), Area: 238,397 sq km, Languages: Romanian, Tourist Attractions: Bran Castle, Peles Castle.",
    "Slovakia": "Capital: Bratislava, Population: 5.5 million, Currency: Euro (EUR), Area: 49,036 sq km, Languages: Slovak, Tourist Attractions: Bratislava Castle, High Tatras.",
    "Slovenia": "Capital: Ljubljana, Population: 2 million, Currency: Euro (EUR), Area: 20,273 sq km, Languages: Slovenian, Tourist Attractions: Lake Bled, Postojna Cave.",
    "Sweden": "Capital: Stockholm, Population: 10 million, Currency: Swedish Krona (SEK), Area: 450,295 sq km, Languages: Swedish, Tourist Attractions: Vasa Museum, Stockholm Archipelago.",
    "Hungary": "Capital: Budapest, Population: 9.7 million, Currency: Hungarian Forint (HUF), Area: 93,030 sq km, Languages: Hungarian, Tourist Attractions: Buda Castle, Hungarian Parliament.",
    "Norway": "Capital: Oslo, Population: 5.4 million, Currency: Norwegian Krone (NOK), Area: 385,207 sq km, Languages: Norwegian, Tourist Attractions: Geirangerfjord, Northern Lights.",
    "Switzerland": "Capital: Bern, Population: 8.5 million, Currency: Swiss Franc (CHF), Area: 41,290 sq km, Languages: German, French, Italian, Romansh, Tourist Attractions: Matterhorn, Lake Geneva.",
    "Serbia": "Capital: Belgrade, Population: 7 million, Currency: Serbian Dinar (RSD), Area: 88,361 sq km, Languages: Serbian, Tourist Attractions: Belgrade Fortress, Studenica Monastery.",
    "Montenegro": "Capital: Podgorica, Population: 0.6 million, Currency: Euro (EUR), Area: 13,812 sq km, Languages: Montenegrin, Tourist Attractions: Bay of Kotor, Sveti Stefan.",
    "North Macedonia": "Capital: Skopje, Population: 2 million, Currency: Macedonian Denar (MKD), Area: 25,713 sq km, Languages: Macedonian, Tourist Attractions: Lake Ohrid, Matka Canyon.",
    "Kosovo": "Capital: Pristina, Population: 1.8 million, Currency: Euro (EUR), Area: 10,908 sq km, Languages: Albanian, Serbian, Tourist Attractions: Gračanica Monastery, Bear Sanctuary.",
    "San Marino": "Capital: San Marino, Population: 33,000, Currency: Euro (EUR), Area: 61 sq km, Languages: Italian, Tourist Attractions: Guaita Tower, Basilica of San Marino.",
    "Bosnia and Herzegovina": "Capital: Sarajevo, Population: 3.3 million, Currency: Bosnian Convertible Mark (BAM), Area: 51,197 sq km, Languages: Bosnian, Croatian, Serbian, Tourist Attractions: Mostar Old Bridge, Sarajevo's Old Bazaar.",
    "Moldova": "Capital: Chisinau, Population: 2.6 million, Currency: Moldovan Leu (MDL), Area: 33,846 sq km, Languages: Romanian, Tourist Attractions: Milestii Mici Winery, Soroca Fortress.",
    "Andorra": "Capital: Andorra la Vella, Population: 0.1 million, Currency: Euro (EUR), Area: 468 sq km, Languages: Catalan, Tourist Attractions: Vallnord Ski Resort, Caldea Spa Complex.",
    "Monaco": "Capital: Monaco, Population: 0.04 million, Currency: Euro (EUR), Area: 2.02 sq km, Languages: French, Tourist Attractions: Casino de Monte-Carlo, Prince's Palace.",
    "Liechtenstein": "Capital: Vaduz, Population: 0.04 million, Currency: Swiss Franc (CHF), Area: 160 sq km, Languages: German, Tourist Attractions: Vaduz Castle, Gutenberg Castle",
    "Armenia": "Capital: Yerevan, Population: 3 million, Currency: Armenian Dram (AMD), Area: 29,743 sq km, Languages: Armenian, Tourist Attractions: Tatev Monastery, Lake Sevan.",
    "Georgia": "Capital: Tbilisi, Population: 4 million, Currency: Georgian Lari (GEL), Area: 69,700 sq km, Languages: Georgian, Tourist Attractions: Svetitskhoveli Cathedral, Uplistsikhe Cave Town."
}


# Mouse event handler function
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        for country, (x1, y1) in countries.items():
            if x1 - 30 <= x <= x1 + 30 and y1 - 30 <= y <= y1 + 30:
                country_info = countries_data.get(country, "No data")

                # Split the country info into lines to fit in the pop-up
                lines = country_info.split(', ')
                line_height = 40
                popup_height = len(lines) * line_height + 80

                # Create a background image for the pop-up
                popup = np.zeros((popup_height, 650, 3), dtype=np.uint8)
                popup[:, :] = (255, 228, 196)  # Background Color

                # Draw title text
                cv2.putText(popup, f"{country}:", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.4,
                            (138, 54, 15), 5)

                # Draw each line of text
                for i, line in enumerate(lines):
                    cv2.putText(popup, line, (10, 110 + i * line_height), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (138, 51, 36),
                                2)

                # Display the pop-up image
                cv2.imshow('Country Information', popup)
                cv2.waitKey(0)
                cv2.destroyWindow('Country Information')


# Load the map of Europe
map_image = cv2.imread('europe_map.jpg')

# Define areas for countries (x1, y1)
countries = {
    "Poland": (613, 562),
    "Germany": (460, 586),
    "Italy": (515, 850),
    "Iceland": (210, 90),
    "Turkey": (955, 900),
    "Russia": (985, 365),
    "Russia Kaliningrad Oblast": (630, 490),
    "Belarus": (750, 530),
    "Hungary": (610, 710),
    "Spain": (150, 820),
    "Andorra": (265, 780),
    "Albania": (630, 880),
    "United Kingdom": (275, 495),
    "Austria": (530, 690),
    "Belgium": (370, 580),
    "Bulgaria": (740, 815),
    "Croatia": (570, 750),
    "Cyprus": (920, 1015),
    "Czech Republic": (550, 625),
    "Denmark": (485, 450),
    "Estonia": (710, 370),
    "Finland": (710, 250),
    "France": (315, 670),
    "Greece": (680, 940),
    "Netherlands": (395, 540),
    "Ireland": (190, 440),
    "Lithuania": (690, 465),
    "Luxembourg": (387, 630),
    "Latvia": (695, 425),
    "Malta": (510, 1015),
    "Monaco": (385, 777),
    "Liechtenstein": (450, 670),
    "San Marino": (480, 785),
    "Portugal": (50, 810),
    "Romania": (720, 735),
    "Slovakia": (625, 650),
    "Slovenia": (530, 730),
    "Sweden": (570, 295),
    "Norway": (495, 285),
    "Switzerland": (390, 700),
    "Serbia": (650, 790),
    "Montenegro": (610, 830),
    "North Macedonia": (665, 860),
    "Kosovo": (650, 830),
    "Bosnia and Herzegovina": (570, 780),
    "Moldova": (785, 691),
    "Ukraine": (830, 615),
    "Armenia": (1130, 800),
    "Georgia": (1090, 760)

}

# Create a window
cv2.namedWindow('Europe Map')
cv2.setMouseCallback('Europe Map', on_mouse)

# Display the map of Europe
cv2.imshow('Europe Map', map_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
