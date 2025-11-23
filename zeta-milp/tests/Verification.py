import gurobipy as gp
try:
    model = gp.Model()
    print("Gurobi installed successfully")
except Exception as e:
    print(f"Gurobi error: {e}")