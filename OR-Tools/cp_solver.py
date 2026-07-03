from ortools.sat.python import cp_model


def main():
    model = cp_model.CpModel()

    """
    Three variables, x, y, and z, each of which can take on the values: 0, 1, or 2.
    One constraint: x != y
    """
    num_vals =3
    x = model.new_int_var(0, num_vals -1, "x")
    y = model.new_int_var(0, num_vals -1, "y")
    z = model.new_int_var(0, num_vals -1, "z")
    model.add(x !=y)

    solver = cp_model.CpSolver()
    status = solver.solve(model)

    if status == cp_model.OPTIMAL or status ==cp_model.FEASIBLE:
        print("x =", solver.value(x))
        print("y =", solver.value(y))
        print("z =", solver.value(z))
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()