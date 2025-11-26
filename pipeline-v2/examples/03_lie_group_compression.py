from spectral_pipeline.representation.lie_group import LieGroupSpectralCompression

compressor = LieGroupSpectralCompression(basis_type='dft', sparsity_param=0.1)
compressed = compressor.transform(sequence)
reconstructed = compressor.inverse_transform(compressed)