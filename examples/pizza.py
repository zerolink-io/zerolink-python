import zerolink as zl

# ------------------------------------------------------------------------
# Ontology Construction
# ------------------------------------------------------------------------

# Create a knowledge graph
kg = zl.create_kg("Pizza Knowledge Graph")

# Inherit pizza and pizza style from Foundation ontology so we derive all
# the related food ontology automatically
pizza = zl.foundation.entity("pizza")
pizza_style = zl.foundation.entity("pizza style")

# Top level class disjoint from the rest of the ontology
ice_cream = kg.add_entity("Ice cream", zl.EntityType.FOOD)

# Create classes for pizza subentities
pizza_topping = kg.add_entity("Pizza topping", zl.EntityType.CLASS)
pizza_base = kg.add_entity("Pizza base", zl.EntityType.CLASS)

# Add entities as classes
named_pizza = kg.add_entity("Named Pizza", pizza_style)
spiciness = kg.add_entity("Spiciness", zl.EntityType.CLASS)

# Properties of pizza
intereresting_pizza = kg.add_entity("Interesting pizza", zl.EntityType.QUALITY)
meaty_pizza = kg.add_entity("Meaty pizza", zl.EntityType.QUALITY)
vegetarian_pizza = kg.add_entity("Non-vegetarian pizza", zl.EntityType.QUALITY)
real_itallian_pizza = kg.add_entity("Real Itallian pizza", zl.EntityType.QUALITY)
spicy_pizza = kg.add_entity("Spicy pizza", zl.EntityType.QUALITY)
thin_and_crispy_pizza = kg.add_entity("Thin and crispy pizza", zl.EntityType.QUALITY)
cheesy_pizza = kg.add_entity("Cheesy pizza", zl.EntityType.QUALITY)

# Base classes
thin_and_crispy_base = kg.add_entity("Thin and crispy base", pizza_base)
deep_pan_base = kg.add_entity("Deep pan base", pizza_base)

# Spice classes
mild_spice = kg.add_entity("Mild spice", spiciness)
medium_spice = kg.add_entity("Medium spice", spiciness)
hot_spice = kg.add_entity("Hot spice", spiciness)

# Topping Properties
spicy_topping = kg.add_entity("Spicy topping", zl.EntityType.QUALITY)
vegetarian_topping = kg.add_entity("Vegetarian topping", zl.EntityType.QUALITY)

# Topping classes
cheese_topping_class = kg.add_entity("Cheese topping", pizza_topping)
vegetable_topping_class = kg.add_entity("Vegetable topping", pizza_topping)
meat_topping_class = kg.add_entity("Meat topping", pizza_topping)
pepper_topping_class = kg.add_entity("Pepper topping", pizza_topping)
fish_topping_class = kg.add_entity("Fish topping", pizza_topping)
herb_spice_topping_class = kg.add_entity("Herb spice topping", pizza_topping)
tomato_topping_class = kg.add_entity("Tomato topping", pizza_topping)
fruit_topping_class = kg.add_entity("Fruit topping", pizza_topping)

# Cheese toppings
mozzarella_topping = kg.add_entity("Mozzarella", cheese_topping_class)
parmesan_topping = kg.add_entity("Parmesan", cheese_topping_class)
goats_cheese_topping = kg.add_entity("Goats Cheese", cheese_topping_class)
gorgonzola_topping = kg.add_entity("Gorgonzola", cheese_topping_class)
four_cheese_topping = kg.add_entity("Four Cheese", cheese_topping_class)

# Fruit toppings
sultana_topping = kg.add_entity("Sultana", fruit_topping_class)

# Vegetable toppings
tomato_topping = kg.add_entity("Tomato", vegetable_topping_class)
green_pepper_topping = kg.add_entity("Green Pepper", pepper_topping_class)
jalapeno_pepper_topping = kg.add_entity("Jalapeno Pepper", pepper_topping_class)
hot_green_pepper_topping = kg.add_entity("Hot Green Pepper", pepper_topping_class)
olive_topping = kg.add_entity("Olive", vegetable_topping_class)
mushroom_topping = kg.add_entity("Mushroom", vegetable_topping_class)
onion_topping = kg.add_entity("Onion", vegetable_topping_class)
spinach_topping = kg.add_entity("Spinach", vegetable_topping_class)
artichoke_topping = kg.add_entity("Artichoke", vegetable_topping_class)
asparagus_topping = kg.add_entity("Asparagus", vegetable_topping_class)
leek_topping = kg.add_entity("Leek", vegetable_topping_class)
sundried_tomato_topping = kg.add_entity("Sundried Tomato", vegetable_topping_class)
sweetcorn_topping = kg.add_entity("Sweetcorn", vegetable_topping_class)
red_onion_topping = kg.add_entity("Red Onion", vegetable_topping_class)
sliced_tomato_topping = kg.add_entity("Sliced Tomato", vegetable_topping_class)
rocket_topping = kg.add_entity("Rocket", vegetable_topping_class)
sweet_pepper_topping = kg.add_entity("Sweet Pepper", pepper_topping_class)
pine_kernels_topping = kg.add_entity("Pine Kernels", vegetable_topping_class)

# Meat toppings
pepperoni_topping = kg.add_entity("Pepperoni", meat_topping_class)
sausage_topping = kg.add_entity("Sausage", meat_topping_class)
ham_topping = kg.add_entity("Ham", meat_topping_class)
chicken_topping = kg.add_entity("Chicken", meat_topping_class)
hot_spiced_beef_topping = kg.add_entity("Hot Spiced Beef", meat_topping_class)
parma_ham_topping = kg.add_entity("Parma Ham", meat_topping_class)

# Fish toppings
anchovies_topping = kg.add_entity("Anchovies", fish_topping_class)
prawns_topping = kg.add_entity("Prawns", fish_topping_class)
mixed_seafood_topping = kg.add_entity("Mixed Seafood", fish_topping_class)

# Herb and spice toppings
rosemary_topping = kg.add_entity("Rosemary", herb_spice_topping_class)
garlic_topping = kg.add_entity("Garlic", herb_spice_topping_class)
cajun_spice_topping = kg.add_entity("Cajun Spice", herb_spice_topping_class)
capers_topping = kg.add_entity("Capers", herb_spice_topping_class)

# Countries of origin
america = kg.add_entity("America", zl.EntityType.COUNTRY)
england = kg.add_entity("England", zl.EntityType.COUNTRY)
france = kg.add_entity("France", zl.EntityType.COUNTRY)
germany = kg.add_entity("Germany", zl.EntityType.COUNTRY)
italy = kg.add_entity("Italy", zl.EntityType.COUNTRY)

# Pizza types
american = kg.add_entity("American", named_pizza)
american_hot = kg.add_entity("American Hot", named_pizza)
cajun = kg.add_entity("Cajun", named_pizza)
capricciosa = kg.add_entity("Capricciosa", named_pizza)
caprina = kg.add_entity("Caprina", named_pizza)
fiorentina = kg.add_entity("Fiorentina", named_pizza)
four_seasons = kg.add_entity("Four Seasons", named_pizza)
frutti_di_mare = kg.add_entity("Frutti Di Mare", named_pizza)
giardiniera = kg.add_entity("Giardiniera", named_pizza)
la_reine = kg.add_entity("La Reine", named_pizza)
margherita = kg.add_entity("Margherita", named_pizza)
mushroom = kg.add_entity("Mushroom", named_pizza)
napoletana = kg.add_entity("Napoletana", named_pizza)
parmense = kg.add_entity("Parmense", named_pizza)
pollo_ad_astra = kg.add_entity("Pollo Ad Astra", named_pizza)
prince_carlo = kg.add_entity("Prince Carlo", named_pizza)
quattro_formaggi = kg.add_entity("Quattro Formaggi", named_pizza)
rosa = kg.add_entity("Rosa", named_pizza)
siciliana = kg.add_entity("Siciliana", named_pizza)
sloppy_giuseppe = kg.add_entity("Sloppy Giuseppe", named_pizza)
soho = kg.add_entity("Soho", named_pizza)
unclosed_pizza = kg.add_entity("Unclosed Pizza", named_pizza)
veneziana = kg.add_entity("Veneziana", named_pizza)

# Domain ontology
named_pizza.subclass(pizza)

# Pizza specifications
kg.add_fact(american, "has topping", mozzarella_topping)
kg.add_fact(american, "has topping", tomato_topping)
kg.add_fact(american, "has topping", pepperoni_topping)
kg.add_fact(american, "has topping", sausage_topping)

kg.add_fact(american_hot, "has topping", hot_green_pepper_topping)
kg.add_fact(american_hot, "has topping", jalapeno_pepper_topping)
kg.add_fact(american_hot, "has topping", mozzarella_topping)
kg.add_fact(american_hot, "has topping", pepperoni_topping)
kg.add_fact(american_hot, "has topping", tomato_topping)

kg.add_fact(veneziana, "has topping", capers_topping)
kg.add_fact(veneziana, "has topping", mozzarella_topping)
kg.add_fact(veneziana, "has topping", olive_topping)
kg.add_fact(veneziana, "has topping", onion_topping)
kg.add_fact(veneziana, "has topping", pine_kernels_topping)
kg.add_fact(veneziana, "has topping", sultana_topping)
kg.add_fact(veneziana, "has topping", tomato_topping)

kg.add_fact(napoletana, "has topping", anchovies_topping)
kg.add_fact(napoletana, "has topping", capers_topping)
kg.add_fact(napoletana, "has topping", mozzarella_topping)
kg.add_fact(napoletana, "has topping", olive_topping)
kg.add_fact(napoletana, "has topping", tomato_topping)

# Specify the origin of the American pizza
kg.add_fact(american, "country of origin", america)
kg.add_fact(american_hot, "country of origin", america)
kg.add_fact(napoletana, "country of origin", italy)
kg.add_fact(margherita, "country of origin", italy)
kg.add_fact(veneziana, "country of origin", italy)

# Spicy toppings
hot_green_pepper_topping.quality(hot_spice)
jalapeno_pepper_topping.quality(hot_spice)
hot_spiced_beef_topping.quality(hot_spice)
cajun_spice_topping.quality(hot_spice)

# ------------------------------------------------------------------------
# Reasoners
# ------------------------------------------------------------------------

# Define the vocabulary of terms to pre-condition the rule inference
ctx = {
    "pizza": pizza,
    "topping": pizza_topping,
    "spicy topping": spicy_topping,
    "vegetarian topping": vegetarian_topping,
    "base": pizza_base,
    "mild": mild_spice,
    "medium": medium_spice,
    "hot": hot_spice,
    "vegetarian": vegetarian_pizza,
    "meaty": meaty_pizza,
    "spicy": spicy_pizza,
    "cheesy": cheesy_pizza,
}

# Define the rules over pizza expressions
rules = [
    "Every topping is a spicy topping if it has quality hot",
    "Every pizza is a spicy pizza if and only if it has a spicy topping.",
    "Every pizza topping is vegetarian topping if it has attribute vegetarian.",
    "Every fish topping is not vegetarian topping.",
    "Every meat topping is not vegetarian topping.",
    "Every vegetable topping is vegetarian topping.",
    "Some pizza is a vegetarian pizza if it does not have meaty topping and does not have a fish topping.",
    "Some pizza is a cheesy pizza if and only if it has a cheese topping.",
    "Some pizza is a meaty pizza if and only if it has a meat topping.",
    "Some pizza is an interesting pizza if and only if it has 3 toppings.",
    "Some pizza is a real Itallian pizza if and only if it has country of origin Italy.",
    "Some pizza is a thin and crispy pizza if and only if it has thin and crispy base.",
    "Some pizza topping has attribute vegetarian if it is a vegetable topping, or cheese topping, or fruit topping, or herb spice topping.",
]

for rule in rules:
    kg.add_rule(rule, ctx=ctx)

# ------------------------------------------------------------------------
# Knowledge Graph Question Answering
# ------------------------------------------------------------------------

# Ask questions
result = kg.ask("What toppings does a Napoletana pizza have?")
for answer in result:
    print(answer)

result = kg.ask("Which types of pizza from Italy are spicy and have mozarella?")
for answer in result:
    print(answer)

result = kg.ask("Which cheesy pizzas from America are vegetarian?")
for answer in result:
    print(answer)

result = kg.ask("Is a Margherita pizza spicy?")
print(result.first().explain())
