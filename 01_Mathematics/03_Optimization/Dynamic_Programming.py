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
    Dynamic Programming is an algorithmic technique with the following properties.

    1. It is mainly an optimization over plain `recursion`. Wherever we see a recursive solution that has repeated calls for the same inputs, we can optimize it using Dynamic Programming.
    2. The idea is to simply store the results of `subproblems` so that we do not have to re-compute them when needed later.

    Some popular problems solved using Dynamic Programming are Fibonacci Numbers, Diff Utility (Longest Common Subsequence), Bellman–Ford Shortest Path, Floyd Warshall, Edit Distance and Matrix Chain Multiplication.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Staircase Problem
    """)
    return


if __name__ == "__main__":
    app.run()
