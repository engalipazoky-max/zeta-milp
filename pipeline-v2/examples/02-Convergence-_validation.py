from spectral_pipeline.math_core.statistics import convergence_bound, validate_convergence

# Theoretical bound for sample size N
bound = convergence_bound(1000)  # Returns 0.079

# Empirical validation
result = validate_convergence(normalized_gaps)
print(f"Bound satisfied: {result['bound_satisfied']}")