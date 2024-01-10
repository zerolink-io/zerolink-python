import zerolink as zl

kg = zl.create_kg("Royal Family")

royal_family = [
    ("Queen Elizabeth II", "spouse", "Prince Philip"),
    ("Queen Elizabeth II", "child", "Prince Charles"),
    ("Queen Elizabeth II", "child", "Princess Anne"),
    ("Queen Elizabeth II", "child", "Prince Andrew"),
    ("Queen Elizabeth II", "child", "Prince Edward"),
    ("Prince Charles", "spouse", "Camilla Parker Bowles"),
    ("Prince Charles", "child", "Prince William"),
    ("Prince Charles", "child", "Prince Harry"),
    ("Prince William", "spouse", "Kate Middleton"),
    ("Prince William", "child", "Prince George"),
    ("Prince William", "child", "Princess Charlotte"),
    ("Prince William", "child", "Prince Louis"),
    ("Prince Harry", "spouse", "Meghan Markle"),
    ("Prince Harry", "child", "Archie Mountbatten-Windsor"),
    ("Prince Andrew", "spouse", "Sarah Ferguson"),
    ("Prince Andrew", "child", "Princess Beatrice"),
    ("Prince Andrew", "child", "Princess Eugenie"),
    ("Prince Edward", "spouse", "Sophie Rhys-Jones"),
    ("Prince Edward", "child", "Lady Louise Windsor"),
    ("Prince Edward", "child", "James, Viscount Severn"),
    ("Prince Philip", "spouse", "Queen Elizabeth II"),
    ("Princess Anne", "spouse", "Mark Phillips"),
    ("Princess Anne", "spouse", "Timothy Laurence"),
    ("Princess Anne", "child", "Peter Phillips"),
    ("Princess Anne", "child", "Zara Tindall"),
    ("Catherine Middleton", "child", "Prince George"),
    ("Catherine Middleton", "child", "Princess Charlotte"),
    ("Catherine Middleton", "child", "Prince Louis"),
    ("Meghan Markle", "child", "Archie Mountbatten-Windsor"),
    ("Peter Phillips", "sex or gender", "male"),
    ("Prince William", "sex or gender", "male"),
]

for s, p, o in royal_family:
    e1 = kg.add_entity(s, type=zl.EntityType.PERSON)
    e2 = kg.add_entity(p, type=zl.EntityType.PERSON)
    kg.add_fact(e1, p, e2)

# Use the local knowledge graph only
ctx = zl.ContextAssumption.LOCAL

answer1 = kg.ask("Who is the spouse of Queen Elizabeth II?", context=ctx)
print(answer1)

answer2 = kg.ask("Who are the grandchildren of Queen Elizabeth II?", context=ctx)
print(answer2)

answer3 = kg.ask("Who are male grandchildren of Queen Elizabeth II?", context=ctx)
print(answer3)
