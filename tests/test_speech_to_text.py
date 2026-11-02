from app.services.speech_to_text import transcribe_audio


def test_transcribe_audio():
    result = transcribe_audio("audio.m4a")

    assert result.strip()
    print(result)