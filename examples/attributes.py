import datetime

import zerolink as zl

kg = zl.get_kg("demo")

e1 = kg.add_entity("Alice", type=zl.EntityType.PERSON)

e1.add_attribute("date of death", datetime.datetime(2063, 4, 5))
e1.add_attribute("date of birth", datetime.datetime(1988, 8, 4))

meters = zl.foundation.entity("meter")
e1.add_attribute("height", zl.quantity(1.7, "meter"))

e1.add_fact("place of death", zl.foundation.entity("Beijing"))
e1.add_fact("place of birth", zl.foundation.entity("New York City"))

print("Knowledge graph:", kg.session_id)

result = kg.ask("Where was Alice born?")
print(result.first())

result = kg.ask("How old is Alice?")
print(result.first())

result = kg.ask("How tall is Alice?")
print(result.first())
