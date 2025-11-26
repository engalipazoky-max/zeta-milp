# examples/ablation_study.py
def run_ablation_study():
    """Analyze component importance in the pipeline"""
    components = {
        'full_pipeline': FullPipeline(),
        'no_milp': PipelineWithoutMILP(), 
        'no_compression': PipelineWithoutCompression(),
        'basic_controller': PipelineWithBasicController()
    }
    
    results = {}
    for name, pipeline in components.items():
        metrics = pipeline.run()
        results[name] = {
            'deviation': metrics['deviation_from_GUE'],
            'runtime': metrics['total_runtime'],
            'stability': metrics['parameter_stability']
        }
    return results