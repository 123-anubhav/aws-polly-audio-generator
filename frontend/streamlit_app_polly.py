import sys
from pathlib import Path
from datetime import datetime

import streamlit as st

# This UI file is expected to live in <project-root>/frontend/streamlit_app_polly.py.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from backend.polly_service import text_to_speech

st.set_page_config(
    page_title="Polly Studio | Text to Speech",
    page_icon="🔊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    .stApp { background: #f5f7fb; }
    .block-container { max-width: 1100px; padding-top: 2rem; padding-bottom: 3rem; }
    .hero {
        padding: 1.7rem 2rem; border-radius: 22px;
        background: linear-gradient(120deg, #172554 0%, #1d4ed8 65%, #0e7490 100%);
        color: white; margin-bottom: 1.25rem;
    }
    .hero h1 { color: white; margin: 0; font-size: 2.2rem; }
    .hero p { color: #dbeafe; margin: .5rem 0 0 0; font-size: 1rem; }
    .panel {
        background: white; border: 1px solid #e4e9f2;
        border-radius: 18px; padding: 1.25rem 1.4rem;
        margin-bottom: 1rem;
    }
    .small-label { color: #64748b; font-size: .9rem; }
    div.stButton > button[kind="primary"] {
        border-radius: 12px; min-height: 3rem; font-weight: 650;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
      <h1>🔊 Polly Studio</h1>
      <p>Turn your text into natural-sounding Hindi speech with Amazon Polly.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns([2, 1], gap="medium")
with left:
    st.markdown("### Create your audio")
    st.caption("Enter or paste the text you want Polly to speak.")
with right:
    st.markdown(
        """
        <div class="panel">
          <div class="small-label">VOICE</div><b>Aditi · Hindi (India)</b><br><br>
          <div class="small-label">OUTPUT FORMAT</div><b>MP3 audio</b><br><br>
          <div class="small-label">ENGINE</div><b>Standard</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

default_text = "नमस्ते! मेरा नाम अदिति है। मैं आपके द्वारा यहाँ टाइप किए गए वाक्य को पढ़ सकती हूँ।"
text = st.text_area(
    "Text to speak",
    value=st.session_state.get("tts_text", default_text),
    height=190,
    max_chars=3000,
    placeholder="यहाँ अपना टेक्स्ट लिखें…",
    help="Hindi text works best with the configured Aditi Hindi voice.",
    key="tts_text",
)

count_col, hint_col = st.columns([1, 3])
with count_col:
    st.caption(f"Characters: {len(text)} / 3000")
with hint_col:
    st.caption("Tip: Use punctuation and short sentences for more natural pauses.")

generate_col, clear_col, _ = st.columns([1.5, 1, 3])
with generate_col:
    generate = st.button("✨ Generate audio", type="primary", use_container_width=True)
with clear_col:
    clear = st.button("Clear text", use_container_width=True)

if clear:
    st.session_state["tts_text"] = ""
    st.session_state.pop("tts_audio_path", None)
    st.session_state.pop("tts_audio_name", None)
    st.rerun()

if generate:
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Amazon Polly is generating your speech…"):
            try:
                output_dir = PROJECT_ROOT / "generated_audio"
                filename = f"speech_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
                audio_path = text_to_speech(text, str(output_dir / filename))
                st.session_state["tts_audio_path"] = audio_path
                st.session_state["tts_audio_name"] = filename
                st.success("Audio generated successfully.")
            except Exception as exc:
                st.error(f"Could not generate audio: {exc}")
                st.info("Check your AWS credentials, Polly permissions, and the configuration in configuration/config.py.")

audio_path = st.session_state.get("tts_audio_path")
audio_name = st.session_state.get("tts_audio_name")

st.markdown("---")
st.markdown("### Your audio")
if audio_path and Path(audio_path).is_file():
    st.markdown(
        f'<div class="panel"><b>🎵 {audio_name}</b><br>'
        '<span class="small-label">Generated successfully · MP3</span></div>',
        unsafe_allow_html=True,
    )
    with open(audio_path, "rb") as audio_file:
        audio_bytes = audio_file.read()
    # Streamlit's built-in player provides play/pause, seeking, and volume controls.
    st.audio(audio_bytes, format="audio/mpeg")
    st.download_button(
        "⬇️ Download MP3",
        data=audio_bytes,
        file_name=audio_name or "speech.mp3",
        mime="audio/mpeg",
        use_container_width=False,
    )
else:
    st.info("Your generated audio will appear here. Enter text above and click Generate audio.")

st.caption("Powered by Amazon Polly · Your text is sent to AWS Polly when you generate audio.")
