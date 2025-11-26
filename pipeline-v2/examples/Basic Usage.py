from spectral_pipeline import SpectralPipeline, LMFDBZetaZeros, LieGroupSpectralCompression

# Initialize pipeline
data_source = LMFDBZetaZeros(height=1e12, count=1000)
representation = LieGroupSpectralCompression()
pipeline = SpectralPipeline(data_source, representation)

# Run analysis
metrics = pipeline.run(n_iterations=50)
results = pipeline.get_final_metrics()
print(f"Deviation from GUE: {results['deviation_from_GUE']:.6f}")