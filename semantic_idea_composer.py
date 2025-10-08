import streamlit as st
import pandas as pd
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

def semantic_add(a: int, b: int) -> (int, str, int):
    total = a + b
    result = total % 11
    meaning = axioms.get(result, "Unknown")
    return total, f"Axiom {result}: {axiom_colors[result]} {meaning}", result

def semantic_subtract(a: int, b: int) -> (int, str, int):
    difference = a - b
    result = difference % 11
    meaning = axioms.get(result, "Unknown")
    return difference, f"Axiom {result}: {axiom_colors[result]} {meaning}", result

def semantic_multiply(a: int, b: int) -> (int, str, int):
    product = a * b
    result = product % 11
    meaning = axioms.get(result, "Unknown")
    return product, f"Axiom {result}: {axiom_colors[result]} {meaning}", result

def semantic_divide(a: int, b: int) -> (str, str, int):
    if b == 0:
        return "Undefined", "Division by zero is undefined.", None
    quotient = a / b
    result = int(quotient) % 11
    meaning = axioms.get(result, "Unknown")
    return f"{quotient:.2f}", f"Axiom {result}: {axiom_colors[result]} {meaning}", result

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

# --- Streamlit UI ---
st.set_page_config(page_title="Semantic Processor", layout="centered")
st.title("🧠 Semantic Processor & Idea Composer")

# Sidebar legend
with st.sidebar:
    st.subheader("🧬 Axiom Legend")
    for i in range(11):
        st.markdown(f"**{i}**: {axiom_colors[i]} {axioms[i]}")

def axiom_reference_table():
    table_data = {
        "Axiom #": [i for i in range(11)],
        "Symbol": [axiom_colors[i] for i in range(11)],
        "Meaning": [axioms[i] for i in range(11)],
    }
    df = pd.DataFrame(table_data)
    st.dataframe(df, use_container_width=True)

st.header("🔢 Semantic Math Calculator")
a = st.number_input("Enter first number (a):", value=2, step=1)
b = st.number_input("Enter second number (b):", value=3, step=1)

col1, col2 = st.columns([2, 2])  # Output and Table side by side

with col1:
    if st.button("➕ Add (Semantic)"):
        value, meaning, axiom_idx = semantic_add(a, b)
        st.success(f"Result: {value}")
        st.info(meaning)
    if st.button("➖ Subtract (Semantic)"):
        value, meaning, axiom_idx = semantic_subtract(a, b)
        st.success(f"Result: {value}")
        st.info(meaning)
    if st.button("✖ Multiply (Semantic)"):
        value, meaning, axiom_idx = semantic_multiply(a, b)
        st.success(f"Result: {value}")
        st.info(meaning)
    if st.button("➗ Divide (Semantic)"):
        value, meaning, axiom_idx = semantic_divide(a, b)
        st.success(f"Result: {value}")
        st.info(meaning)

with col2:
    st.markdown("### Reference Table")
    axiom_reference_table()

st.markdown("---")
st.header("📈 Semantic Calculus")
expr_input = st.text_input("Enter a mathematical expression (e.g., x**2 + 3*x):")
var_input = st.text_input("Differentiate or integrate with respect to (e.g., x):", value="x")

col1, col2 = st.columns(2)

with col1:
    if st.button("🧮 Derivative"):
        result = semantic_derivative(expr_input, var_input)
        st.info(result)

with col2:
    if st.button("🔄 Integral"):
        result = semantic_integral(expr_input, var_input)
        st.info(result)

with st.expander("ℹ️ How It Works"):
    st.markdown("""
    - Arithmetic operations use modulo 11 to wrap results into one of the 11 axioms.
    - Calculus uses symbolic differentiation and integration for expressions with respect to a variable.
    - This extends the semantic processor to continuous change.
    """)

st.markdown("---")
st.header("🌌 Idea Composer")
idea_input = st.text_input("Enter a sequence of numbers separated by commas (e.g. 0,1,2,3):")

if st.button("🧬 Compose Idea"):
    try:
        path = [int(x.strip()) for x in idea_input.split(",") if x.strip().isdigit()]
        result = compose_idea(path)
        st.info(result)

        # Export options
        if st.button("💾 Export as JSON"):
            json_data = json.dumps({"idea_sequence": path, "semantic_trace": result}, indent=2)
            st.download_button("Download JSON", json_data, file_name="semantic_idea.json")

        if st.button("📄 Export as Text"):
            txt_data = result
            st.download_button("Download Text", txt_data, file_name="semantic_idea.txt")

    except Exception as e:
        st.error(f"Error: {e}")

# Preset Templates
st.markdown("---")
st.subheader("🧠 Try a Semantic Template")
selected_template = st.selectbox("Choose a Template:", [
    "(None)",
    "Big Bang → 0,1,2,3",
    "Mind Emergence → 5,6,7,9",
    "Feedback Loop → 2,4,6,10"
])

if selected_template != "(None)":
    template_map = {
        "Big Bang → 0,1,2,3": [0,1,2,3],
        "Mind Emergence → 5,6,7,9": [5,6,7,9],
        "Feedback Loop → 2,4,6,10": [2,4,6,10]
    }
    path = template_map[selected_template]
    st.info(compose_idea(path))
