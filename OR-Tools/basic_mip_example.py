
from ortools.init.python import init
from ortools.linear_solver import pywraplp

"""
Maximize x + 10y subject to the following constraints:

x + 7y ≤ 17.5
0 ≤ x ≤ 3.5
0 ≤ y
x, y integers
"""

def main():
    # Create the mip solver with the CP-SAT backend.
    solver = pywraplp.Solver.CreateSolver("SAT")
    if not solver:
        return
    infinity = solver.infinity()
    # x and y are integer, not-negative variables
    x = solver.IntVar(0.0, infinity, "x")
    y = solver.IntVar(0.0, infinity, "y")

    #x + 7y ≤ 17.5
    solver.Add(x + 7 * y <= 17.5)
    #0 ≤ x ≤ 3.5
    solver.Add( x <= 3.5)
    
    print("Number of constraints = ", solver.NumConstraints())

    # Maximize x + 10 * y.
    solver.Maximize(x + 10 *y)
    print(f"Solving with {solver.SolverVersion()}")
    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        print("Solution:")
        print("Objective value =", solver.Objective().Value())
        print("x =", x.solution_value())
        print("y =", y.solution_value())
    else:
        print("The problem does not have an optimal solution.")  

if __name__ == "__main__":
    main()        