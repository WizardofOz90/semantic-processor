
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

def semantic_add(a: int, b: int) -> str:
    total = a + b
    result = total % 11
    meaning = axioms.get(result, "Unknown")
    return f"{a} + {b} = {total}\n→ Axiom {result}: {axiom_colors[result]} {meaning}"

def semantic_subtract(a: int, b: int) -> str:
    difference = a - b
    result = difference % 11
    meaning = axioms.get(result, "Unknown")
    return f"{a} - {b} = {difference}\n→ Axiom {result}: {axiom_colors[result]} {meaning}"

def semantic_multiply(a: int, b: int) -> str:
    product = a * b
    result = product % 11
    meaning = axioms.get(result, "Unknown")
    return f"{a} × {b} = {product}\n→ Axiom {result}: {axiom_colors[result]} {meaning}"

def semantic_divide(a: int, b: int) -> str:
    if b == 0:
        return "Division by zero is undefined."
    quotient = a / b
    result = int(quotient) % 11
    meaning = axioms.get(result, "Unknown")
    return f"{a} ÷ {b} = {quotient:.2f}\n→ Axiom {result}: {axiom_colors[result]} {meaning}"

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

# Streamlit UI
st.set_page_config(page_title="Semantic Processor", layout="centered")
st.title("🧠 Semantic Processor & Math Interface")

# Sidebar legend
with st.sidebar:
    st.subheader("🧬 Axiom Legend")
    for i in range(11):
        st.markdown(f"**{i}**: {axiom_colors[i]} {axioms[i]}")

# 🔢 Basic Calculator Interface
st.header("🧮 Basic + Semantic Calculator")
a = st.number_input("First number:", step=1, value=1, key="basic_a")
b = st.number_input("Second number:", step=1, value=1, key="basic_b")
operation = st.selectbox("Operation:", ["+", "-", "×", "÷"])

if st.button("Calculate"):
    if operation == "+":
        st.success(semantic_add(a, b))
    elif operation == "-":
        st.success(semantic_subtract(a, b))
    elif operation == "×":
        st.success(semantic_multiply(a, b))
    elif operation == "÷":
        st.success(semantic_divide(a, b))

st.markdown("---")
st.header("📈 Semantic Calculus")
expr_input = st.text_input("Enter a mathematical expression (e.g., x**2 + 3*x):")
var_input = st.text_input("Differentiate or integrate with respect to (e.g., x):", value="x")

col1, col2 = st.columns(2)
with col1:
    if st.button("🧮 Derivative"):
        st.info(semantic_derivative(expr_input, var_input))
with col2:
    if st.button("🔄 Integral"):
        st.info(semantic_integral(expr_input, var_input))

st.markdown("---")
st.header("🌌 Idea Composer")
idea_input = st.text_input("Enter a sequence of numbers (e.g. 0,1,2,3):")
if st.button("🧬 Compose Idea"):
    try:
        path = [int(x.strip()) for x in idea_input.split(",") if x.strip().isdigit()]
        result = compose_idea(path)
        st.info(result)
    except Exception as e:
        st.error(f"Error: {e}")
