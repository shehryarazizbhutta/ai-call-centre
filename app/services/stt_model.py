from faster_whisper import WhisperModel

_model = None

def get_model():
    global _model

    if _model is None:
        _model = WhisperModel(
            "large-v3-turbo",
            device="cpu",
            compute_type="int8",
        )

    return _model