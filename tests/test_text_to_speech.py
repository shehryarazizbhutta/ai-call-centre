import wave

from app.services.text_to_speech import synthesize_speech


def test_synthesize_speech(tmp_path):
    output_path = tmp_path / "test_output.wav"

    result = synthesize_speech(
        "Hello, good morning. Thank you for calling.",
        output_path,
    )

    assert result == output_path
    assert output_path.exists()

    with wave.open(str(output_path), "rb") as wav_file:
        assert wav_file.getnchannels() > 0
        assert wav_file.getsampwidth() > 0
        assert wav_file.getframerate() > 0
        assert wav_file.getnframes() > 0