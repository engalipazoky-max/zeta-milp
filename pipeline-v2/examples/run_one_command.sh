# Installation
pip install spectral-pipeline-v2.0.zip

# Full pipeline execution
spectral-pipeline run-full --height 1e12 --count 1000 --representation lie-group

# Ablation study
spectral-pipeline ablation --input zeros.csv --output ablation_report.html

# Convergence certification  
spectral-pipeline certify --input zeros.csv --bound-type explicit