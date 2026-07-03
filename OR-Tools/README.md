# OR-Tools Examples

A collection of Google OR-Tools example scripts demonstrating different solver APIs and optimization techniques.

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) (package manager)

## Setup

```bash
# Create a virtual environment and install dependencies
uv sync
```

## Examples

### Linear Programming

| File | Solver | Description |
|------|--------|-------------|
| [`basic_example.py`](basic_example.py) | **GLOP** (LP) | Maximize $3x + y$ subject to $x + y \leq 2$, $x \in [0, 1]$, $y \in [0, 2]$ |
| [`mathopt_basic_example.py`](mathopt_basic_example.py) | **GLOP** (via MathOpt) | Same type of LP but using the newer MathOpt API: maximize $x + 2y$ subject to $x + y \leq 1.5$ |

### Mixed-Integer Programming (MIP)

| File | Solver | Description |
|------|--------|-------------|
| [`basic_mip_example.py`](basic_mip_example.py) | **CP-SAT** | Maximize $x + 10y$ subject to $x + 7y \leq 17.5$, $x \leq 3.5$, with $x, y \in \mathbb{Z}_{\geq 0}$ |
| [`mip_var_array.py`](mip_var_array.py) | **SCIP** | MIP with 5 variables and 4 constraints using array-based variable and constraint construction |

### Constraint Programming (CP)

| File | Solver | Description |
|------|--------|-------------|
| [`cp_solver.py`](cp_solver.py) | **CP-SAT** | 3 variables $\{0, 1, 2\}$ with constraint $x \neq y$ — finds one feasible solution |
| [`cp_solver_all.py`](cp_solver_all.py) | **CP-SAT** | Same problem, but enumerates **all** solutions using a solution callback |
| [`cp_solver_mathopt.py`](cp_solver_mathopt.py) | **HIGHS** (via MathOpt) | Same CP problem reformulated with a binary variable and big-M constraints |

## APIs Covered

- **`pywraplp`** — Traditional OR-Tools linear solver wrapper (GLOP, SCIP, CP-SAT)
- **`cp_model`** — CP-SAT constraint programming model
- **`mathopt`** — Modern MathOpt API (GLOP, HIGHS, and other solvers)

## Running an Example

```bash
uv run python basic_example.py
```

## References

- [Google OR-Tools Documentation](https://developers.google.com/optimization)
- [OR-Tools GitHub](https://github.com/google/or-tools)
