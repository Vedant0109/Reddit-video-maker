# merging audio and video file

import moviepy.editor as mp

input_video= "MINECRAFT — RUNAWAY [a4K_60FPS].mp4"

input_audio= "hello.mp3"

output_video= "final.mp4"

video= mp.VideoFileClip(input_video)

audio= mp.AudioFileClip(input_audio)

clip= video.set_audio(audio)

finalclip= clip.subclip(0, audio.duration)

finalclip.write_videofile(output_video , fps=60)
