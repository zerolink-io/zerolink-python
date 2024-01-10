from enum import Enum


class EntityType(str, Enum):
    ABSTRACT_ENTITY = "Abstract Entity"
    AIRCRAFT = "Aircraft"
    ALBUM = "Album"
    ANATOMY = "Anatomy"
    ANIMAL = "Animal"
    ARTISTIC_WORK = "Artistic Work"
    ARTWORK = "Artwork"
    ASTRONOMICAL_OBJECT = "Astronomical Object"
    ATTRIBUTE = "Attribute"
    AWARD = "Award"
    BEING = "Being"
    BIOLOGICAL_PROCESS = "Biological Process"
    BODY_OF_WATER = "Body of Water"
    BOOK = "Book"
    CELLULAR_COMPONENT = "Cellular Component"
    CHEMICAL_COMPOUND = "Chemical Compound"
    CITY = "City"
    CLASS = "Class"
    COMPANY = "Company"
    CONCEPT = "Concept"
    CONTINUANT = "Continuant"
    COUNTRY = "Country"
    CREATIVE_WORK = "Creative Work"
    CURRENCY = "Currency"
    DISEASE = "Disease"
    DRINK = "Drink"
    DRUG = "Drug"
    ECONOMIC_ENTITY = "Economic Entity"
    ELEMENT = "Element"
    ENTITY = "Entity"
    EXPOSURE = "Exposure"
    FIELD_OF_WORK = "Field of Work"
    FILM = "Film"
    FINANCIAL_INSTRUMENT = "Financial Instrument"
    FOOD = "Food"
    GENDER_IDENTITY = "Gender Identity"
    GENE = "Gene"
    GENRE = "Genre"
    GOVERNMENT = "Government"
    HISTORICAL_ENTITY = "Historical Entity"
    IMMATERIAL_ENTITY = "Immaterial Entity"
    INDUSTRY = "Industry"
    INFORMATION = "Information"
    LANGUAGE = "Language"
    LAW = "Law"
    LOCATION = "Location"
    MATERIAL_ENTITY = "Material Entity"
    MATHEMATICAL_OBJECT = "Mathematical Object"
    MEDIA = "Media"
    METACLASS = "Metaclass"
    MOLECULAR_FUNCTION = "Molecular Function"
    MUSIC = "Music"
    OCCURRENT = "Occurrent"
    ORGANISM = "Organism"
    ORGANIZATION = "Organization"
    PATHWAY = "Pathway"
    PERSON = "Person"
    PHENOTYPE = "Phenotype"
    PHYSICAL_ENTITY = "Physical Entity"
    PLANT = "Plant"
    PROCESS = "Process"
    PRODUCT = "Product"
    PROFESSION = "Profession"
    PROPERTY = "Property"
    PROTEIN = "Protein"
    QUALIA = "Qualia"
    QUALITY = "Quality"
    QUANTITY = "Quantity"
    RELATIONSHIP = "Relationship"
    RELIGION = "Religion"
    ROLE = "Role"
    SCHOLARLY_ARTICLE = "Scholarly Article"
    SHIP = "Ship"
    SOFTWARE = "Software"
    SONG = "Song"
    SPORT = "Sport"
    STAR = "Star"
    SUBATOMIC_PARTICLE = "Subatomic Particle"
    SUBSTANCE = "Substance"
    TAXON = "Taxon"
    TV_SERIES = "TV Series"
    UNIT = "Unit"
    UNIVERSITY = "University"
    VEHICLE = "Vehicle"
    VIDEO_GAME = "Video Game"
    WEBSITE = "Website"

    def __str__(self) -> str:
        return str(self.value)