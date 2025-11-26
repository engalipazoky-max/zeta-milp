# Fetch zeta zeros
spectral-pipeline fetch --height 1e12 --count 1000 --output zeros.csv

# Run analysis
spectral-pipeline analyze --input zeros.csv --representation lie-group

# Validate convergence
spectral-pipeline validate --input zeros.csv --output report.png

# Ablation study
spectral-pipeline ablation --input zeros.csv --output ablation.html