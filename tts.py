from gtts import gTTS
from deep_translator import GoogleTranslator

def text_to_speech(text, lang='hi'):
    """Translate text to Hindi and convert to speech."""
    translated_text = GoogleTranslator(source='auto', target='hi').translate(text)  # Translate to Hindi
    tts = gTTS(text=translated_text, lang='hi', slow=False)  # Convert to Hindi speech
    audio_path = "output.mp3"
    tts.save(audio_path)
    return audio_path
