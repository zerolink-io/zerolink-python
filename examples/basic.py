import zerolink as zl

kg = zl.get_kg("demo")

e1 = kg.add_entity("Alice", type=zl.EntityType.PERSON)
e2 = kg.add_entity("Bob", type=zl.EntityType.PERSON)
e3 = kg.add_entity("Charlie", type=zl.EntityType.PERSON)

kg.add_fact(e1, "spouse", e2)
kg.add_fact(e2, "child", e3)

print("Knowledge graph:", kg.session_id)
print("Done.")

for e in kg.entities:
    print(e)

for f in kg.facts:
    print(f)
