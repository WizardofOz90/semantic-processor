import streamlit as st
from typing import List
import json
import sympy as sp

axioms = {
    0: "Void – potential",
    1: "Monad – distinction",
    2: "Duality – relation",
    3: "Triad – transformation",
    4: "Pattern – recurrence",
    5: "Growth – identity",
    6: "Recursion – memory",
    7: "Self-awareness",
    8: "Interconnection",
    9: "Unity – integration",
    10: "Rebirth – next scale",
}

axiom_colors = {
    0: "⚪", 1: "🔴", 2: "🔵", 3: "🟡", 4: "🟠",
    5: "🟢", 6: "🟣", 7: "🟤", 8: "🟥", 9: "🟦", 10: "⬜"
}

def semantic_add(a: int, b: int) -> (int, str):
    total = a + b
    result = total % 11
    meaning = axioms.get(result, "Unknown")
    return total, f"Axiom {result}: {axiom_colors[result]} {meaning}"

def semantic_subtract(a: int, b: int) -> (int, str):
    difference = a - b
    result = difference % 11
    meaning = axioms.get(result, "Unknown")
    return difference, f"Axiom {result}: {axiom_colors[result]} {meaning}"

def semantic_multiply(a: int, b: int) -> (int, str):
    product = a * b
    result = product % 11
    meaning = axioms.get(result, "Unknown")
    return product, f"Axiom {result}: {axiom_colors[result]} {meaning}"

def semantic_divide(a: int, b: int) -> (str, str):
    if b == 0:
        return "Undefined", "Division by zero is undefined."
    quotient = a / b
    result = int(quotient) % 11
    meaning = axioms.get(result, "Unknown")
    return f"{quotient:.2f}", f"Axiom {result}: {axiom_colors[result]} {meaning}"

def compose_idea(path: List[int]) -> str:
    trace = []
    for value in path:
        concept = axioms.get(value % 11, "Unknown")
        symbol = axiom_colors.get(value % 11, "")
        trace.append(f"{symbol} {value} → {concept}")
    return " →→→ ".join(trace)

def semantic_derivative(expr: str, var: str) -> str:
    try:
        x = sp.Symbol(var)
        parsed_expr = sp.sympify(expr)
        derivative = sp.diff(parsed_expr, x)
        return f"d/d{var}({expr}) = {sp.pretty(derivative)}"
    except Exception as e:
        return f"Error computing derivative: {e}"

def semantic_integral(expr: str, var: str) -> str:
    try:
        x = sp.Symbol(var)
        parsed_expr = sp.sympify(expr)
        integral = sp.integrate(parsed_expr, x)
        return f"∫ {expr} d{var} = {sp.pretty(integral)} + C"
    except Exception as e:
        return f"Error computing integral: {e}"

# rest of your code follows...