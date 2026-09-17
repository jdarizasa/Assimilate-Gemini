#!/usr/bin/env python3

from genilib.solutions import generate_solution
import click
    
@click.command()
@click.option("--question", prompt="Enter your question", help="The question to generate a solution for")
def main(question):
    """
    Main function to generate a solution for a given question.
    """
    solution = generate_solution(question)
    print(f"Solution: {solution}")

if __name__ == "__main__":
    main()