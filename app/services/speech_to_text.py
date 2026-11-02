from pathlib import Path
import time
from app.services.stt_model import get_model


def transcribe_audio(audio_path: str | Path) -> str:
    start_time = time.perf_counter()
    segments, _ = get_model().transcribe(
        str(audio_path),
        language="en",
        beam_size=5,
    )

    result = " ".join(segment.text.strip() for segment in segments)

    elapsed_time = time.perf_counter() - start_time
    print(f"Transcription time: {elapsed_time:.2f} seconds")

    return result