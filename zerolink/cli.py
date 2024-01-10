import csv
import json
import os
import sys
import uuid

import click
import click_completion
import click_completion.core

import zerolink as zl
import zerolink.settings

click_completion.init()

# ------------------------------------------------------------------------
# Subcommands
# ------------------------------------------------------------------------


# Create the main command group
@click.group()
@click.version_option()
def main():
    """
    ZeroLink client.
    """
    pass


# Create the embedding group
@click.group()
def embedding():
    """
    Graph query embedding operations.
    """
    pass


# Create the billing group
@click.group()
def billing():
    """
    Billing operations.
    """
    pass


# Create the api command group
@click.group()
def api():
    """
    Direct API calls.
    """
    pass


# Create the config command group
@click.group()
def config():
    """
    Configuration options.
    """
    pass


# Create the connecto command group
@click.group()
def connectors():
    """
    Connector operations.
    """
    pass


# Create the connecto command group
@click.group()
def fine_tune():
    """
    RLHF and fine-tuning operations.
    """
    pass


# ------------------------------------------------------------------------
# Config
# ------------------------------------------------------------------------


# Generate config file
@config.command()
def generate():
    """
    Generate a config file.
    """
    click.echo("Created config file at: " + zerolink.settings.get_config_path())
    zerolink.settings.create_config()
    click.echo("Done.")
    sys.exit(0)


# Get a config variable
@config.command()
@click.argument("var", type=str)
def get(var: str):
    """
    Get a config variable.
    """
    click.echo(zerolink.settings.get_config_var(var))
    sys.exit(0)


# Set a config variable
@config.command()
@click.argument("var", type=str)
@click.argument("value", type=str)
def set(var: str, value: str):
    """
    Set a config variable.
    """
    zerolink.settings.write_config_var(var, value)
    click.echo("Done.")
    sys.exit(0)


# Get the config path
@config.command()
def path():
    """
    Get the config path.
    """
    click.echo(zerolink.settings.get_config_path())
    sys.exit(0)


# ------------------------------------------------------------------------
# Direct API Calls
# ------------------------------------------------------------------------


# Create the ask command which takes a string as an argument
@api.command()
@click.argument("question")
def ask(question):
    """
    Ask a question.
    """
    req = zl.ask(question)
    for answer in req:
        click.echo(answer)
    # If an answer is found, exit code 0, otherwise exit code 1
    sys.exit(0 if req else 1)


@api.command()
@click.argument("entity")
@click.option("--limit", default=10, help="The number of entities to return.")
def entity(entity, limit):
    """
    Search for an entity by name.
    """
    req = zl.find_entity(entity, limit=limit)
    for ent in req:
        click.echo(ent)
    sys.exit(0 if req else 1)


# Search for entity by eid
@api.command()
@click.argument("eid")
def eid(eid):
    """
    Search for an entity by eid.
    """
    req = zl.get_desc_entity(eid)
    if req:
        click.echo(req)
        sys.exit(0)
    else:
        click.echo("No entity found", err=True)
        sys.exit(1)


# Search for property by name
@api.command()
@click.argument("name")
@click.option("--limit", default=10, help="The number of properties to return.")
def relation(name, limit):
    """
    Search for a relation by name.
    """
    req = zl.find_relation(name)
    for prop in req:
        click.echo(prop)
    sys.exit(0 if req else 1)


# Get ontology
@api.command()
@click.argument("entity")
def ontology(entity: str):
    """
    Get the ontology.
    """
    ontology = zl.ontology(entity)
    if ontology:
        click.echo(json.dumps(ontology, indent=4))
        sys.exit(0)
    else:
        click.echo("No ontology found", err=True)
        sys.exit(1)


@api.command()
@click.argument("file")
def extract(file):
    """
    Extract text from a local file.
    """
    # Get the file extension
    ext = os.path.splitext(file)[1][1:]
    click.echo(f"File extension: {ext}")

    # Check if the file exists
    if not os.path.exists(file):
        click.echo(f"File {file} does not exist")
        sys.exit(1)
    else:
        zl.extract_text(file)


@api.command()
@click.argument("stream", default="-")
@click.option("--format", default="json", help="The format of the input stream")
def facts(stream, format):
    """
    Extract facts from a file or stdin.
    """

    if stream == "-":
        # Read from stdin
        # click.echo("Reading from stdin")
        ifile = click.get_text_stream("stdin").read()
    else:
        # Read from a file
        # click.echo(f"Reading from file {stream}")
        with open(stream, "r") as f:
            ifile = f.read()

    # Parse the data
    if format == "json":
        # Parse the json
        try:
            data = json.loads(ifile)
            print(json.dumps(data, indent=4))
        except json.JSONDecodeError:
            click.echo("Invalid JSON", err=True)
            sys.exit(1)
    elif format == "csv":
        # Parse the csv
        try:
            data = []
            rdr = csv.reader(ifile.splitlines(), delimiter=",")
            # read the rows
            for row in rdr:
                data.append(tuple(row))
            print(json.dumps(data, indent=4))
        except csv.Error:
            click.echo("Invalid CSV", err=True)
            sys.exit(1)
    else:
        click.echo("Invalid format", err=True)
        sys.exit(1)


# query triples for a given topic
@api.command()
@click.argument("topic")
@click.option("--limit", default=10, help="The number of entities to return.")
def triples(topic, limit):
    """
    Get the triples of a topic.
    """
    triples = zl.find_triples(topic, limit=limit)
    if triples:
        for triple in triples:
            click.echo(triple)
        sys.exit(0)
    else:
        click.echo("No triples found", err=True)
        sys.exit(1)


# ------------------------------------------------------------------------
# Fine Tuning
# ------------------------------------------------------------------------


# Create the fine-tuning command which takes a filepath as an argument
@fine_tune.command()
@click.argument("filepath")
def create(filepath):
    job_id = zl.fine_tune(filepath)
    print(f"Craeted fine-tuning job with id {job_id}")


# ------------------------------------------------------------------------
# Access Key
# ------------------------------------------------------------------------


# Create the key command which prompts the user for an api key
@main.command()
def key():
    """
    Set the api key.
    """
    key = click.prompt("Enter key")

    # Validate the key
    try:
        uuid.UUID(key)
    except ValueError:
        click.echo("Invalid key")
        sys.exit(1)

    # Write the key to the config file
    zerolink.settings.write_api_key(key)
    click.echo(f"Key saved to {zerolink.settings.get_config_path()}")
    sys.exit(0)


@main.command()
@click.argument("shell", type=click.Choice(click_completion.core.shells))
def completion(shell):
    """
    Generate shell completions.
    """
    # Get the completion script
    click_completion.core.get_code(shell=shell)
    # click.echo(script)
    # install the completion script
    click_completion.core.install()


# Add the api command group to the main command group
main.add_command(api)
main.add_command(completion)
main.add_command(key)
main.add_command(config)
main.add_command(embedding)
main.add_command(connectors)
main.add_command(billing)
main.add_command(fine_tune)

# Run the main command group
if __name__ == "__main__":
    main()
