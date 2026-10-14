import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from configuration.config import build_llm

# Reuse your existing AWS Polly configuration.
polly, _ = build_llm("polly")


def text_to_speech(text: str, output_file: str = "output.mp3") -> str:
    """Convert text to Hindi speech and save it as an MP3 file."""
    if not text or not text.strip():
        raise ValueError("Please enter some text before generating audio.")

    response = polly.synthesize_speech(
        Text=text.strip(),
        OutputFormat="mp3",
        VoiceId="Aditi",
        Engine="standard",
        LanguageCode="hi-IN",
    )

    audio_stream = response.get("AudioStream")
    if audio_stream is None:
        raise RuntimeError("AWS Polly did not return an audio stream.")

    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with audio_stream:
        output_path.write_bytes(audio_stream.read())

    return str(output_path)
