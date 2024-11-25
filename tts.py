from gtts import gTTS

word= "Hello, this is some text for merging it in a video file"

tts= gTTS(word, lang= 'en')

tts.save('hello.mp3')