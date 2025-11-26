# Certifiable Computational Framework for Zeta Zero Spectral Analysis

This repository provides the **full reproducible pipeline** for the paper:

&gt; **"Certifiable Computational Framework for Riemann Zeta Zero Spectral Analysis with Explicit Performance Guarantees"**  
&gt; *ali pazoky*  
&gt; Submitted to *Experimental Mathematics* (2025)

---

## 🔍 What You Can Reproduce Here

- ✅ Validate the convergence bound:  
  ‖S_N − C_GUE‖ ≤ 2.5/√N + 3 log N / N
- ✅ Re-run MILP subset selection with certified optimality gaps &lt; 1e-6
- ✅ Reproduce all figures (1a–1d) from the paper
- ✅ Re-run GUE simulations and LMFDB data extraction

---
## 📄 Latest Preprint
- **PDF**: [zeta_milp_2025_preprint.pdf](paper/zeta_milp_2025_preprint.pdf)
- **Zenodo DOI**: [10.5281/zenodo.17688932](https://doi.org/10.5281/zenodo.17688932)
- **arXiv**: *Pending endorsement* (submitted [Date])
---
graph TD

    A[LMFDB Data] --> B[Preprocessing]
    B --> C [S_N Computation]
    C --> D [Bootstrap CI]
    D --> E {Representation}
    E --> F [Raw Domain]
    E --> G [MILP Subset]
    E --> H [Lie-Group Compression]
    F --> I [CAL Controller]
    G --> I
    H --> I
    I --> J [Evaluation]
    J --> K [Certification]
---

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/engalipazoky-max/zeta-milp-certified.git
cd zeta-milp-certified

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run full pipeline
python scripts/run_all.py

![Paper Figures](https://raw.githubusercontent.com/engalipazoky-max/zeta-milp/main/figures/Theoretical C_GUE.png)


## 📄 Citation

If you use this code or data in your research, please cite:

```bibtex
@misc{pazoky2025zeta,
  author       = {Ali Pazoky},
  title        = {Certifiable Computational Framework for Riemann Zeta Zero Spectral Analysis},
  year         = {2025},
  howpublished = {\url{https://github.com/engalipazoky-max/zeta-milp}},
  note         = {GitHub repository, DOI: (10.5281/zenodo.17688932)} }
