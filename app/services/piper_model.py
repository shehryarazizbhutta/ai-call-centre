from piper import PiperVoice
from app.core.config import settings

_voice = None


def get_voice():
    global _voice

    if _voice is None:
        _voice = PiperVoice.load(settings.PIPER_MODEL_PATH)

    return _voice