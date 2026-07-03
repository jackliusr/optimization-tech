"""CP-SAT example converted to MathOpt.

Three variables, x, y, and z, each of which can take on the values: 0, 1, or 2.
One constraint: x != y

The != constraint is modeled with a binary variable and big-M constraints:
  b = 0  =>  x > y   (x - y >= 1)
  b = 1  =>  x < y   (x - y <= -1)
"""
from ortools.math_opt.python import mathopt


def main():
    model = mathopt.Model(name="cp_solver_mathopt")

    num_vals = 3
    # Integer variables in {0, 1, 2}
    x = model.add_integer_variable(lb=0, ub=num_vals - 1, name="x")
    y = model.add_integer_variable(lb=0, ub=num_vals - 1, name="y")
    z = model.add_integer_variable(lb=0, ub=num_vals - 1, name="z")

    # Model x != y using a binary variable and big-M.
    # b = 0 => x - y >= 1,   b = 1 => x - y <= -1
    b = model.add_binary_variable(name="b")
    big_m = num_vals  # sufficient since |x - y| <= num_vals - 1

    model.add_linear_constraint(x - y >= 1 - big_m * b)
    model.add_linear_constraint(x - y <= -1 + big_m * (1 - b))

    # Treat this as a feasibility problem (no objective).
    result = mathopt.solve(model, mathopt.SolverType.HIGHS)

    if result.termination.reason in (
        mathopt.TerminationReason.OPTIMAL,
        mathopt.TerminationReason.FEASIBLE,
    ):
        print("x =", result.variable_values()[x])
        print("y =", result.variable_values()[y])
        print("z =", result.variable_values()[z])
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
