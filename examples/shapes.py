import zerolink as zl

# Create a knowledge graph
kg = zl.create_kg("shapes")

shape = zl.foundation.entity("geometric shape")
quadrilateral = kg.add_entity("quadrilateral", zl.EntityType.QUALITY)

# Add entities
circle = kg.add_entity("circle", shape)
square = kg.add_entity("square", shape)
triangle = kg.add_entity("triangle", shape)
rectangle = kg.add_entity("rectangle", shape)
oval = kg.add_entity("oval", shape)
pentagon = kg.add_entity("pentagon", shape)
hexagon = kg.add_entity("hexagon", shape)
trapezoid = kg.add_entity("trapezoid", shape)

rectangle.quality(quadrilateral)
trapezoid.quality(quadrilateral)

# Add relationships
circle.subclass(oval)
square.subclass(rectangle)

# Use the closed world assumption where we assume that if something is not
# explicitly stated in the graph, then it is false. Since we're dealing with
# mathematical objects.
world = zl.WorldAssumption.CLOSED

# Ask questions
result = kg.ask("Is a square a rectangle?", world=world)
print(result.first().explain())

result = kg.ask("Is a rectangle a square?", world=world)
print(result.first().explain())

result = kg.ask("Is a square a quadrilateral?", world=world)
print(result.first().explain())

result = kg.ask("Is a circle a quadrilateral?", world=world)
print(result.first().explain())
