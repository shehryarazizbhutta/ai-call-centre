from pathlib import Path
import wave

from app.services.piper_model import get_voice


def synthesize_speech(text: str, output_path: str | Path) -> Path:
    if not text.strip():
        raise ValueError("Text cannot be empty.")

    output_path = Path(output_path)
    voice = get_voice()

    with wave.open(str(output_path), "wb") as wav_file:
        for index, chunk in enumerate(voice.synthesize(text)):
            if index == 0:
                wav_file.setnchannels(chunk.sample_channels)
                wav_file.setsampwidth(chunk.sample_width)
                wav_file.setframerate(chunk.sample_rate)

            wav_file.writeframes(chunk.audio_int16_bytes)

    return output_path