from genilib.solutions import generate_solution
import pytest

def test_generate_solution():
    question = "What is the capital of France?"
    solution = generate_solution(question)
    assert isinstance(solution, str)
    assert "Paris" in solution

def test_generate_code():
    prompt = "Write a function to calculate the area of a circle."
    code = generate_code(prompt)
    assert isinstance(code, str)
    assert "def" in code