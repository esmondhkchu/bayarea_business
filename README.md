# Yelp
Analysis of Bay Area restaurants. <br>
Total restaurants collected: 19,223 <br>
Total reviews collected: 56,108

Data Source: <br>
Yelp Fusion: [API Link](https://www.yelp.com/fusion) <br>

## Directory Tree
Last Update: 1/2/2020
```base
├── README.md
├── data
│   ├── all_businesses_info.csv
│   ├── all_reviews.csv
│   ├── bay_area_demography.csv
│   └── raw_businesses_data
│       ├── Alameda_CA_businesses_info.json
│       ├── Alameda_CA_reviews.json
│       ├── Albany_CA_businesses_info.json
│       ├── Albany_CA_reviews.json
│       ├── American\ Canyon_CA_businesses_info.json
│       ├── American\ Canyon_CA_reviews.json
│       ├── Antioch_CA_businesses_info.json
│       ├── Antioch_CA_reviews.json
│       ├── Atherton_CA_businesses_info.json
│       ├── Atherton_CA_reviews.json
│       ├── Belmont_CA_businesses_info.json
│       ├── Belmont_CA_reviews.json
│       ├── Belvedere_CA_businesses_info.json
│       ├── Belvedere_CA_reviews.json
│       ├── Benicia_CA_businesses_info.json
│       ├── Benicia_CA_reviews.json
│       ├── Berkeley_CA_businesses_info.json
│       ├── Berkeley_CA_reviews.json
│       ├── Brentwood_CA_businesses_info.json
│       ├── Brentwood_CA_reviews.json
│       ├── Brisbane_CA_businesses_info.json
│       ├── Brisbane_CA_reviews.json
│       ├── Burlingame_CA_businesses_info.json
│       ├── Burlingame_CA_reviews.json
│       ├── Calistoga_CA_businesses_info.json
│       ├── Calistoga_CA_reviews.json
│       ├── Campbell_CA_businesses_info.json
│       ├── Campbell_CA_reviews.json
│       ├── Clayton_CA_businesses_info.json
│       ├── Clayton_CA_reviews.json
│       ├── Cloverdale_CA_businesses_info.json
│       ├── Cloverdale_CA_reviews.json
│       ├── Colma_CA_businesses_info.json
│       ├── Colma_CA_reviews.json
│       ├── Concord_CA_businesses_info.json
│       ├── Concord_CA_reviews.json
│       ├── Corte\ Madera_CA_businesses_info.json
│       ├── Corte\ Madera_CA_reviews.json
│       ├── Cotati_CA_businesses_info.json
│       ├── Cotati_CA_reviews.json
│       ├── Cupertino_CA_businesses_info.json
│       ├── Cupertino_CA_reviews.json
│       ├── Daly\ City_CA_businesses_info.json
│       ├── Daly\ City_CA_reviews.json
│       ├── Danville_CA_businesses_info.json
│       ├── Danville_CA_reviews.json
│       ├── Dixon_CA_businesses_info.json
│       ├── Dixon_CA_reviews.json
│       ├── Dublin_CA_businesses_info.json
│       ├── Dublin_CA_reviews.json
│       ├── East\ Palo\ Alto_CA_businesses_info.json
│       ├── East\ Palo\ Alto_CA_reviews.json
│       ├── El\ Cerrito_CA_businesses_info.json
│       ├── El\ Cerrito_CA_reviews.json
│       ├── Emeryville_CA_businesses_info.json
│       ├── Emeryville_CA_reviews.json
│       ├── Fairfax_CA_businesses_info.json
│       ├── Fairfax_CA_reviews.json
│       ├── Fairfield_CA_businesses_info.json
│       ├── Fairfield_CA_reviews.json
│       ├── Foster\ City_CA_businesses_info.json
│       ├── Foster\ City_CA_reviews.json
│       ├── Fremont_CA_businesses_info.json
│       ├── Fremont_CA_reviews.json
│       ├── Gilroy_CA_businesses_info.json
│       ├── Gilroy_CA_reviews.json
│       ├── Half\ Moon\ Bay_CA_businesses_info.json
│       ├── Half\ Moon\ Bay_CA_reviews.json
│       ├── Hayward_CA_businesses_info.json
│       ├── Hayward_CA_reviews.json
│       ├── Healdsburg_CA_businesses_info.json
│       ├── Healdsburg_CA_reviews.json
│       ├── Hercules_CA_businesses_info.json
│       ├── Hercules_CA_reviews.json
│       ├── Hillsborough_CA_businesses_info.json
│       ├── Hillsborough_CA_reviews.json
│       ├── Lafayette_CA_businesses_info.json
│       ├── Lafayette_CA_reviews.json
│       ├── Larkspur_CA_businesses_info.json
│       ├── Larkspur_CA_reviews.json
│       ├── Livermore_CA_businesses_info.json
│       ├── Livermore_CA_reviews.json
│       ├── Los\ Altos\ Hills_CA_businesses_info.json
│       ├── Los\ Altos\ Hills_CA_reviews.json
│       ├── Los\ Altos_CA_businesses_info.json
│       ├── Los\ Altos_CA_reviews.json
│       ├── Los\ Gatos_CA_businesses_info.json
│       ├── Los\ Gatos_CA_reviews.json
│       ├── Martinez_CA_businesses_info.json
│       ├── Martinez_CA_reviews.json
│       ├── Menlo\ Park_CA_businesses_info.json
│       ├── Menlo\ Park_CA_reviews.json
│       ├── Mill\ Valley_CA_businesses_info.json
│       ├── Mill\ Valley_CA_reviews.json
│       ├── Millbrae_CA_businesses_info.json
│       ├── Millbrae_CA_reviews.json
│       ├── Milpitas_CA_businesses_info.json
│       ├── Milpitas_CA_reviews.json
│       ├── Monte\ Sereno_CA_businesses_info.json
│       ├── Monte\ Sereno_CA_reviews.json
│       ├── Moraga_CA_businesses_info.json
│       ├── Moraga_CA_reviews.json
│       ├── Morgan\ Hill_CA_businesses_info.json
│       ├── Morgan\ Hill_CA_reviews.json
│       ├── Mountain\ View_CA_businesses_info.json
│       ├── Mountain\ View_CA_reviews.json
│       ├── Napa_CA_businesses_info.json
│       ├── Napa_CA_reviews.json
│       ├── Newark_CA_businesses_info.json
│       ├── Newark_CA_reviews.json
│       ├── Novato_CA_businesses_info.json
│       ├── Novato_CA_reviews.json
│       ├── Oakland_CA_businesses_info.json
│       ├── Oakland_CA_reviews.json
│       ├── Oakley_CA_businesses_info.json
│       ├── Oakley_CA_reviews.json
│       ├── Orinda_CA_businesses_info.json
│       ├── Orinda_CA_reviews.json
│       ├── Pacifica_CA_businesses_info.json
│       ├── Pacifica_CA_reviews.json
│       ├── Palo\ Alto_CA_businesses_info.json
│       ├── Palo\ Alto_CA_reviews.json
│       ├── Petaluma_CA_businesses_info.json
│       ├── Petaluma_CA_reviews.json
│       ├── Piedmont_CA_businesses_info.json
│       ├── Piedmont_CA_reviews.json
│       ├── Pinole_CA_businesses_info.json
│       ├── Pinole_CA_reviews.json
│       ├── Pittsburg_CA_businesses_info.json
│       ├── Pittsburg_CA_reviews.json
│       ├── Pleasant\ Hill_CA_businesses_info.json
│       ├── Pleasant\ Hill_CA_reviews.json
│       ├── Pleasanton_CA_businesses_info.json
│       ├── Pleasanton_CA_reviews.json
│       ├── Portola\ Valley_CA_businesses_info.json
│       ├── Portola\ Valley_CA_reviews.json
│       ├── Redwood\ City_CA_businesses_info.json
│       ├── Redwood\ City_CA_reviews.json
│       ├── Richmond_CA_businesses_info.json
│       ├── Richmond_CA_reviews.json
│       ├── Rio\ Vista_CA_businesses_info.json
│       ├── Rio\ Vista_CA_reviews.json
│       ├── Rohnert\ Park_CA_businesses_info.json
│       ├── Rohnert\ Park_CA_reviews.json
│       ├── Ross_CA_businesses_info.json
│       ├── Ross_CA_reviews.json
│       ├── San\ Anselmo_CA_businesses_info.json
│       ├── San\ Anselmo_CA_reviews.json
│       ├── San\ Bruno_CA_businesses_info.json
│       ├── San\ Bruno_CA_reviews.json
│       ├── San\ Carlos_CA_businesses_info.json
│       ├── San\ Carlos_CA_reviews.json
│       ├── San\ Francisco_CA_businesses_info.json
│       ├── San\ Francisco_CA_reviews.json
│       ├── San\ Jose_CA_businesses_info.json
│       ├── San\ Jose_CA_reviews.json
│       ├── San\ Leandro_CA_businesses_info.json
│       ├── San\ Leandro_CA_reviews.json
│       ├── San\ Mateo_CA_businesses_info.json
│       ├── San\ Mateo_CA_reviews.json
│       ├── San\ Pablo_CA_businesses_info.json
│       ├── San\ Pablo_CA_reviews.json
│       ├── San\ Rafael_CA_businesses_info.json
│       ├── San\ Rafael_CA_reviews.json
│       ├── San\ Ramon_CA_businesses_info.json
│       ├── San\ Ramon_CA_reviews.json
│       ├── Santa\ Clara_CA_businesses_info.json
│       ├── Santa\ Clara_CA_reviews.json
│       ├── Santa\ Rosa_CA_businesses_info.json
│       ├── Santa\ Rosa_CA_reviews.json
│       ├── Saratoga_CA_businesses_info.json
│       ├── Saratoga_CA_reviews.json
│       ├── Sausalito_CA_businesses_info.json
│       ├── Sausalito_CA_reviews.json
│       ├── Sebastopol_CA_businesses_info.json
│       ├── Sebastopol_CA_reviews.json
│       ├── Sonoma_CA_businesses_info.json
│       ├── Sonoma_CA_reviews.json
│       ├── St.\ Helena_CA_businesses_info.json
│       ├── St.\ Helena_CA_reviews.json
│       ├── Suisun\ City_CA_businesses_info.json
│       ├── Suisun\ City_CA_reviews.json
│       ├── Sunnyvale_CA_businesses_info.json
│       ├── Sunnyvale_CA_reviews.json
│       ├── Tiburon_CA_businesses_info.json
│       ├── Tiburon_CA_reviews.json
│       ├── Union\ City_CA_businesses_info.json
│       ├── Union\ City_CA_reviews.json
│       ├── Vacaville_CA_businesses_info.json
│       ├── Vacaville_CA_reviews.json
│       ├── Vallejo_CA_businesses_info.json
│       ├── Vallejo_CA_reviews.json
│       ├── Walnut\ Creek_CA_businesses_info.json
│       ├── Walnut\ Creek_CA_reviews.json
│       ├── Windsor_CA_businesses_info.json
│       ├── Windsor_CA_reviews.json
│       ├── Woodside_CA_businesses_info.json
│       ├── Woodside_CA_reviews.json
│       ├── Yountville_CA_businesses_info.json
│       └── Yountville_CA_reviews.json
├── data_analysis
│   └── NLP_model.ipynb
├── data_extraction
│   ├── bay_area_cities_data_extraction.ipynb
│   └── yelp_data_extraction.ipynb
├── data_wrangling
│   └── data_wrangling.ipynb
└── tools
    ├── data_tools.py
    └── yelp_fusion.py
```
