import marimo

__generated_with = "0.22.0"
app = marimo.App(width="full", auto_download=["ipynb", "html"])


@app.cell(hide_code=True)
def _():
    import marimo as mo

    # Impoart theme
    import urllib.request as req

    mo.Html(
        f"<style>{req.urlopen('https://raw.githubusercontent.com/janithcyapa/Engineering-Codex/refs/heads/main/shared_files/marimo/theme.css').read().decode()}</style>"
    )
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # **Dynamic Programming (DP)**
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Introduction
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### What is DP ?
    Dynamic Programming is an algorithmic technique with the following properties.It solves complex, large-scale problems by breaking them down into smaller, simpler subproblems. Instead of recalculating the answer to these subproblems every time they appear, DP solves them once and stores the result.

    You can only use DP if a problem satisfies these two mathematical properties:
    1. `Optimal Substructure`: The optimal solution to the overall problem contains the optimal solutions to its subproblems. (e.g., If the fastest route from A to C goes through B, the A-to-B segment must be the absolute fastest route to B).

    2. `Overlapping Subproblems`: The algorithm encounters the exact same subproblems multiple times during its execution. Storing these answers saves exponential amounts of computation time.

    Some popular problems solved using Dynamic Programming are Fibonacci Numbers, Diff Utility (Longest Common Subsequence), Bellman–Ford Shortest Path, Floyd Warshall, Edit Distance and Matrix Chain Multiplication.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Dynamic Programming vs. Greedy Algorithms

    It is crucial to distinguish DP from Greedy algorithms, as both are used for optimization.

    | Feature | Greedy Algorithm | Dynamic Programming |
    | :--- | :--- | :--- |
    | **The Mindset** | "Take the best immediate option." | "Evaluate all options to find the best global plan." |
    | **Re-evaluation** | Never looks back once a choice is made. | Systematically checks combinations using stored past data. |
    | **Optimal Guarantee** | Fails if the immediate best choice leads to a bad long-term outcome. | Mathematically guarantees the absolute best overall solution. |
    | **Execution** | Fast, uses very little memory. | Slower, uses more memory (to store the DP tables). |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### The Core Elements of a DP Model

    To translate a real-world problem into a DP algorithm, you must define four components:

    1. Stages ($i$): The steps or phases where a decision must be made. (e.g., Which item to consider packing next, or which city to drive to next).

    2. States ($x_i$): The specific condition or available resources at a given stage. (e.g., "I have 4 tons of capacity left in the vessel" or "I am currently at Node C"). The state acts as the link between stages.

    3. Alternatives ($m_i$): The available choices or actions you can take from your current state. (e.g., "Pack 0, 1, or 2 units of this item").

    4. Recursive Equation: The formal mathematical function linking the stages together. It always takes the form of:

    >    Current Best Value = (Immediate Reward of Choice) + (Optimal Value of the Remaining State).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Approaches to Solving DP

    ##### Direction of Logic

    - `Top-Down (Memoization)`: Start at the final, large problem and recursively break it down. You save the answer to a cache (memo) as you find it.

    - `Bottom-Up (Tabulation)`: Start with the smallest, most trivial base cases (like x=0) and systematically build a table upward until you reach the final problem size. This eliminates the overhead of recursive function calls.

    ##### Direction of Recursion (Network/Tabular DP)

    When dealing with staged problems (like the Shortest Path or Knapsack tables), you can iterate in two directions:

    - `Forward Recursion`: Start at Stage 1 and move toward Stage n. You calculate the state based on what you already accumulated:
    $$ x_i = x_{i-1} + w_i m_i$$


    - `Backward Recursion`: Start at the final Stage n and work backward to Stage 1. You calculate the state based on what you will have left for the next stage:
    $$ x_i = x_{i+1} + w_i m_i$$

    (Note: Backward recursion is often preferred in Operations Research because it naturally answers "If I am in this state, what is the best path to the finish?")
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### General Strategy for Setting up a DP Solution

    If you are faced with a new DP problem, follow these exact steps:

    1. Define the State: What is the minimal amount of information you need to track so you don't have to look back? (e.g., "Remaining Capacity").
    2. Define the Base Case: What is the answer to the smallest possible subproblem? (e.g., "If capacity is 0, profit is 0").
    3. Formulate the Transition: How do you move from one state to the next? Write the Bellman equation.
    4. Draw the Table: Put your states (x) on the rows, your alternatives (m) on the columns, and calculate the values step-by-step.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Shortest Path Problem
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Knapsack Problem
    """)
    return


if __name__ == "__main__":
    app.run()
