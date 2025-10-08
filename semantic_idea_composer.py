import streamlit as st
import random
import json
import sympy as sp

from typing import List

# Semantic axioms and colors
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

MAX_PRIME_RANGE = 10000
MAX_NEXT_PRIME_START = 100000

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generate_primes_up_to(n: int) -> List[int]:
    primes = []
    for num in range(2, n+1):
        if is_prime(num):
            primes.append(num)
    return primes

def safe_generate_primes_up_to(n: int) -> List[int] or str:
    if n > MAX_PRIME_RANGE:
        return "Input too large! Try <= 10,000."
    return generate_primes_up_to(n)

def semantic_prime(n: int) -> str:
    prime_status = is_prime(n)
    if prime_status:
        return f"{n} is PRIME! 🚀 Semantic: {axiom_colors[n%11]} {axioms[n%11]}"
    else:
        return f"{n} is not prime. Semantic: {axiom_colors[n%11]} {axioms[n%11]}"

def semantic_primes_trace(n: int) -> str:
    result = safe_generate_primes_up_to(n)
    if isinstance(result, str):
        return result
    trace = [f"{p}: {axiom_colors[p % 11]} {axioms[p % 11]}" for p in result]
    return " → ".join(trace)

def find_next_prime(n: int) -> int or None:
    if n > MAX_NEXT_PRIME_START:
        return None
    candidate = n + 1
    while True:
        if is_prime(candidate):
            return candidate
        candidate += 1

def semantic_next_prime(n: int) -> str:
    next_p = find_next_prime(n)
    if next_p is None:
        return f"Input too large! Try <= {MAX_NEXT_PRIME_START}."
    return f"Next prime after {n} is {next_p}: {axiom_colors[next_p % 11]} {axioms[next_p % 11]}"

def semantic_add_prime_highlight(a: int, b: int) -> str:
    total = a + b
    result = total % 11
    highlight = "🌟 PRIME!" if is_prime(total) else ""
    meaning = axioms.get(result, "Unknown")
    return f"{a} + {b} = {total} → Axiom {result}: {axiom_colors[result]} {meaning} {highlight}"

def semantic_power(a: int, b: int) -> str:
    power = a ** b
    result = power % 11
    meaning = axioms.get(result, "Unknown")
    prime_str = "🌟 PRIME!" if is_prime(power) else ""
    return f"{a} ^ {b} = {power} → Axiom {result}: {axiom_colors[result]} {meaning} {prime_str}"

def semantic_mod(a: int, b: int) -> str:
    if b == 0:
        return "Modulus by zero is undefined."
    mod = a % b
    result = mod % 11
    meaning = axioms.get(result, "Unknown")
    prime_str = "🌟 PRIME!" if is_prime(mod) else ""
    return f"{a} mod {b} = {mod} → Axiom {result}: {axiom_colors[result]} {meaning} {prime_str}"

def semantic_subtract(a: int, b: int) -> str:
    difference = a - b
    result = difference % 11
    meaning = axioms.get(result, "Unknown")
    prime_str = "🌟 PRIME!" if is_prime(difference) else ""
    return f"{a} - {b} = {difference} → Axiom {result}: {axiom_colors[result]} {meaning} {prime_str}"

def semantic_multiply(a: int, b: int) -> str:
    product = a * b
    result = product % 11
    meaning = axioms.get(result, "Unknown")
    prime_str = "🌟 PRIME!" if is_prime(product) else ""
    return f"{a} × {b} = {product} → Axiom {result}: {axiom_colors[result]} {meaning} {prime_str}"

def semantic_divide(a: int, b: int) -> str:
    if b == 0:
        return "Division by zero is undefined."
    quotient = a / b
    result = int(quotient) % 11
    meaning = axioms.get(result, "Unknown")
    prime_str = "🌟 PRIME!" if is_prime(int(quotient)) else ""
    return f"{a} ÷ {b} = {quotient:.2f} → Axiom {result}: {axiom_colors[result]} {meaning} {prime_str}"

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

def compose_idea(path: List[int]) -> str:
    trace = []
    for value in path:
        concept = axioms.get(value % 11, "Unknown")
        symbol = axiom_colors.get(value % 11, "")
        trace.append(f"{symbol} {value} → {concept}")
    return " →→→ ".join(trace)

def semantic_and(a: int, b: int) -> str:
    result = (a & b) % 11
    meaning = axioms.get(result, "Unknown")
    prime_str = "🌟 PRIME!" if is_prime(a & b) else ""
    return f"{a} AND {b} = {a & b} → Axiom {result}: {axiom_colors[result]} {meaning} {prime_str}"

def semantic_or(a: int, b: int) -> str:
    result = (a | b) % 11
    meaning = axioms.get(result, "Unknown")
    prime_str = "🌟 PRIME!" if is_prime(a | b) else ""
    return f"{a} OR {b} = {a | b} → Axiom {result}: {axiom_colors[result]} {meaning} {prime_str}"

def semantic_not(a: int) -> str:
    result = (~a) % 11
    meaning = axioms.get(result, "Unknown")
    prime_str = "🌟 PRIME!" if is_prime(~a) else ""
    return f"NOT {a} = {~a} → Axiom {result}: {axiom_colors[result]} {meaning} {prime_str}"

# 1. Prime Gaps
def prime_gaps(n: int) -> str:
    primes = generate_primes_up_to(n)
    if len(primes) < 2:
        return "Not enough primes in range."
    gaps = [primes[i+1] - primes[i] for i in range(len(primes)-1)]
    return "Prime gaps: " + ", ".join(str(gap) for gap in gaps)

# 2. Prime Factorization
def prime_factorization(n: int) -> str:
    if n < 2:
        return "Enter an integer ≥ 2."
    factors = []
    candidate = 2
    original = n
    while candidate * candidate <= n:
        while n % candidate == 0:
            factors.append(candidate)
            n //= candidate
        candidate += 1
    if n > 1:
        factors.append(n)
    if not factors:
        return f"{original} is prime."
    return f"Prime factors of {original}: " + ", ".join(str(f) for f in factors)

# 3. Prime Distribution Visualization
def prime_distribution(n: int):
    primes = generate_primes_up_to(n)
    return primes

# 4. Nth Prime
def nth_prime(n: int) -> str:
    if n < 1:
        return "Enter N ≥ 1."
    count = 0
    candidate = 2
    while True:
        if is_prime(candidate):
            count += 1
            if count == n:
                return f"The {n}th prime is {candidate}: {axiom_colors[candidate % 11]} {axioms[candidate % 11]}"
        candidate += 1

# 5. Goldbach Conjecture Explorer
def goldbach_pair(even_n: int) -> str:
    if even_n <= 2 or even_n % 2 != 0:
        return "Enter an even integer > 2."
    for i in range(2, even_n):
        if is_prime(i) and is_prime(even_n - i):
            return f"{even_n} = {i} + {even_n - i}"
    return "No Goldbach pair found."

# 6. Twin Primes
def twin_primes(n: int) -> str:
    primes = generate_primes_up_to(n)
    twins = [(primes[i], primes[i+1]) for i in range(len(primes)-1) if primes[i+1]-primes[i]==2]
    if not twins:
        return "No twin primes found."
    return "Twin primes: " + ", ".join(f"{a}, {b}" for a, b in twins)

# --- UI Section ---

st.set_page_config(page_title="Semantic Calculator with Primes", layout="centered")
st.title("🧠 Semantic Processor & Prime Composer")

with st.expander("📘 Axiom Legend"):
    for i in range(11):
        st.markdown(f"**{i}**: {axiom_colors[i]} {axioms[i]}")

tab1, tab2, tab3 = st.tabs(["Calculator", "Prime Tools", "Advanced Primes"])

with tab1:
    # Calculator Pad UI
    if 'calc_input' not in st.session_state:
        st.session_state['calc_input'] = ""
    st.markdown("### 🧮 Calculator Pad")
    rows = [
        ['7', '8', '9', '+'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '×'],
        ['0', '.', '=', '÷']
    ]
    for row in rows:
        cols = st.columns(4)
        for i, label in enumerate(row):
            if cols[i].button(label, key=f"btn_{label}_{row}"):
                if label == '=':
                    try:
                        st.session_state['calc_input'] = str(eval(st.session_state['calc_input'].replace('×','*').replace('÷','/')))
                    except Exception:
                        st.session_state['calc_input'] = "Error"
                else:
                    st.session_state['calc_input'] += label
    st.text_input("Result", value=st.session_state['calc_input'], key='result', disabled=True)

    st.header("Semantic Math Calculator")
    a = st.number_input("Enter first number (a):", value=2, step=1)
    b = st.number_input("Enter second number (b):", value=3, step=1)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Add (Semantic)", key="add_sem"):
            st.success(semantic_add_prime_highlight(a, b))
        if st.button("✖ Multiply (Semantic)", key="mult_sem"):
            st.success(semantic_multiply(a, b))
        if st.button("^ Power (Semantic)", key="pow_sem"):
            st.success(semantic_power(a, b))
    with col2:
        if st.button("➖ Subtract (Semantic)", key="sub_sem"):
            st.success(semantic_subtract(a, b))
        if st.button("➗ Divide (Semantic)", key="div_sem"):
            st.success(semantic_divide(a, b))
        if st.button("Mod (Semantic)", key="mod_sem"):
            st.success(semantic_mod(a, b))
    with col3:
        if st.button("🔀 AND (Logic)", key="and_sem"):
            st.success(semantic_and(a, b))
        if st.button("🔁 OR (Logic)", key="or_sem"):
            st.success(semantic_or(a, b))
        if st.button("🚫 NOT (Logic)", key="not_sem"):
            st.success(semantic_not(a))

    st.header("📈 Semantic Calculus")
    expr_input = st.text_input("Enter a mathematical expression (e.g., x**2 + 3*x):")
    var_input = st.text_input("Differentiate or integrate with respect to (e.g., x):", value="x")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🧮 Derivative", key="deriv_sem"):
            st.info(semantic_derivative(expr_input, var_input))
    with col2:
        if st.button("🔄 Integral", key="integ_sem"):
            st.info(semantic_integral(expr_input, var_input))

    st.header("🌌 Idea Composer")
    idea_input = st.text_input("Enter a sequence of numbers separated by commas (e.g. 0,1,2,3):")
    if st.button("🧬 Compose Idea", key="compose_sem"):
        try:
            path = [int(x.strip()) for x in idea_input.split(",") if x.strip().isdigit()]
            result = compose_idea(path)
            st.info(result)

            if st.button("💾 Export as JSON", key="export_json"):
                json_data = json.dumps({"idea_sequence": path, "semantic_trace": result}, indent=2)
                st.download_button("Download JSON", json_data, file_name="semantic_idea.json")

            if st.button("📄 Export as Text", key="export_txt"):
                txt_data = result
                st.download_button("Download Text", txt_data, file_name="semantic_idea.txt")
        except Exception as e:
            st.error(f"Error: {e}")

    st.subheader("🧠 Try a Semantic Template")
    selected_template = st.selectbox("Choose a Template:", [
        "(None)",
        "Big Bang → 0,1,2,3",
        "Mind Emergence → 5,6,7,9",
        "Feedback Loop → 2,4,6,10",
        "Prime Emergence → 2,3,5,7,11"
    ])
    if selected_template != "(None)":
        template_map = {
            "Big Bang → 0,1,2,3": [0,1,2,3],
            "Mind Emergence → 5,6,7,9": [5,6,7,9],
            "Feedback Loop → 2,4,6,10": [2,4,6,10],
            "Prime Emergence → 2,3,5,7,11": [2,3,5,7,11]
        }
        path = template_map[selected_template]
        st.info(compose_idea(path))

with tab2:
    st.header("🟩 Semantic Prime Tools")
    prime_input = st.number_input("Check primality for:", value=7, step=1)
    if st.button("Check Prime"):
        st.info(semantic_prime(prime_input))

    seq_limit = st.number_input("Generate primes up to:", value=20, step=1)
    if st.button("Compose Prime Sequence"):
        result = semantic_primes_trace(seq_limit)
        if "Input too large" in result:
            st.warning(result)
        else:
            st.info(result)

    st.header("🔎 Find Primes in Range")
    prime_range_min = st.number_input("Prime range minimum:", value=2, step=1)
    prime_range_max = st.number_input("Prime range maximum:", value=100, step=1)
    if st.button("Find Primes in Range"):
        if prime_range_max >= prime_range_min:
            if prime_range_max > MAX_PRIME_RANGE:
                st.warning(f"Input too large! Try <= {MAX_PRIME_RANGE}.")
            else:
                primes = generate_primes_up_to(prime_range_max)
                primes_in_range = [p for p in primes if p >= prime_range_min]
                st.markdown("**Primes found:**")
                for p in primes_in_range:
                    st.markdown(f"- {p}: {axiom_colors[p % 11]} {axioms[p % 11]}")
        else:
            st.error("Maximum must be greater than or equal to minimum.")

    st.header("🔮 Find Next Prime Number")
    next_prime_input = st.number_input("Find next prime after:", value=7, step=1)
    if st.button("Find Next Prime"):
        result = semantic_next_prime(next_prime_input)
        if "Input too large" in result:
            st.warning(result)
        else:
            st.info(result)

with tab3:
    st.header("🔸 Prime Gaps Explorer")
    gap_limit = st.number_input("Compute prime gaps up to:", value=20, step=1)
    if st.button("Show Prime Gaps"):
        st.info(prime_gaps(gap_limit))

    st.header("🔸 Prime Factorization")
    factor_input = st.number_input("Factorize:", value=28, step=1)
    if st.button("Show Prime Factors"):
        st.info(prime_factorization(factor_input))

    st.header("🔸 Prime Distribution Chart")
    dist_limit = st.number_input("Visualize primes up to:", value=100, step=1)
    if st.button("Show Prime Chart"):
        data = prime_distribution(dist_limit)
        st.bar_chart(data)

    st.header("🔸 Nth Prime Finder")
    nth_input = st.number_input("Which Nth prime?", value=10, step=1)
    if st.button("Show Nth Prime"):
        st.info(nth_prime(nth_input))

    st.header("🔸 Goldbach Explorer")
    goldbach_input = st.number_input("Even number (>2):", value=28, step=2)
    if st.button("Find Goldbach Pair"):
        st.info(goldbach_pair(goldbach_input))

    st.header("🔸 Twin Primes Finder")
    twin_limit = st.number_input("Find twin primes up to:", value=100, step=1)
    if st.button("Show Twin Primes"):
        st.info(twin_primes(twin_limit))
