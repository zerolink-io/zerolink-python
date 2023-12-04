import zerolink as zl

# zl.api_key = zl.get_user_id()

kg = zl.create_kg("demo")

print("What does Taylor Swift do?")

answers = kg.ask("What does Taylor Swift do?")
for i, answer in enumerate(answers):
    print(i, answer)

print("Who are the siblings of George Bush?")

answers = kg.ask("Who are the siblings of George Bush?")
for i, answer in enumerate(answers):
    print(i, answer)

print("Done.")
