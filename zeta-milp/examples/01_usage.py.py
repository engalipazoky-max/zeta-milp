from spectral_pipeline import SpectralPipeline
from spectral_pipeline.data.zeta_zeros import LMFDBZetaZeros
from spectral_pipeline.representation.lie_group import LieGroupSpectralCompression

# Initialize pipeline
data_source = LMFDBZetaZeros(height=1e12, count=1000)
representation = LieGroupSpectralCompression(basis_type='dft', sparsity_param=0.1)
pipeline = SpectralPipeline(data_source, representation)

# Run analysis
metrics = pipeline.run(n_iterations=50)

# Get results
final_metrics = pipeline.get_final_metrics()
print(f"Final deviation from GUE: {final_metrics['deviation_from_GUE']:.6f}")