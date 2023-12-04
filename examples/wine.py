import os
import re

import pandas as pd

import zerolink as zl


def clean_wine_title(title) -> str:
    """Remove text within parentheses from wine titles using regex."""
    return re.sub(r"\([^)]*\)", "", title)


def build_kg(dataframe, kg) -> None:
    """Iterate through the DataFrame to add entities and relationships to the knowledge kg."""

    # Attach to the foundation ontology so we inherit the basic entities.
    wine = zl.foundation.entity("wine")
    winery = zl.foundation.entity("winery")
    grape_variety = zl.foundation.entity("grape variety")

    for index, row in dataframe.iterrows():
        wine_title = clean_wine_title(row["title"])
        country = row["country"]
        province = row["province"]
        variety = row["variety"]
        winery = row["winery"]
        region = row["region_1"]
        subregion = row["region_2"]
        description = row["description"]

        # Add entities if they don't exist yet.
        wine_entity = kg.add_entity(wine_title, wine)
        variety_entity = kg.add_entity(variety, grape_variety)
        country_entity = kg.add_entity(country, zl.EntityType.COUNTRY)
        winery_entity = kg.add_entity(winery, winery)
        region_entity = kg.add_entity(region, zl.EntityType.LOCATION)

        # Add facts to the knowledge kg
        kg.add_fact(variety_entity, "instance of", grape_variety)
        kg.add_fact(wine_entity, "instance of", variety_entity)
        kg.add_fact(wine_entity, "country of origin", country_entity)
        kg.add_fact(winery_entity, "product or material produced", variety_entity)
        kg.add_fact(
            winery_entity,
            "located in the administrative territorial entity",
            region_entity,
        )

        # Use the text extraction API to extract the description of the wine
        # and attach the reuslting facts to the wine in the knowledge kg.
        zl.extract_text(description, kg, attach=wine_entity)
        print("Added: ", wine_title)


def main() -> None:
    # Load the dataset
    # Get the folder of the current file
    folder = os.path.dirname(os.path.abspath(__file__))
    wine_data = pd.read_csv(os.path.join(folder, "winemag-data-130k-v2.csv"))

    # Create the knowledge kg
    kg = zl.create_kg("Wine Knowledge Graph")

    # Process the first 100 rows and add to the knowledge kg
    # create_kg(wine_data.head(100), kg)
    build_kg(wine_data, kg)


if __name__ == "__main__":
    main()
