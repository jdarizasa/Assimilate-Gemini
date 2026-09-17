#!/usr/bin/env python3

from genilib.solutions import generate_code
import click

@click.command()
@click.option("--prompt", prompt="Enter your prompt to generate code", help="The prompt to generate code from")
def main(prompt):
    """
    Main function to generate code from a given prompt.
    """
    code = generate_code(prompt)
    print(f"Generated Code:\n{code}")

if __name__ == "__main__":
    main()