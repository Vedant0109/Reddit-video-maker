import time 
import math 
import ffmpeg
from faster_whisper import WhisperModel
input_viedo = r"" # ADD YOUR VIEDO PATH 
input_viedo_name = input_viedo.replace(".mp4","")
def extracted_audio ():
    excrated_audio = f"audio-{input_viedo_name}.wav"
    stream = ffmpeg.input(input_viedo)
    stream = ffmpeg.output(stream,excrated_audio)
    ffmpeg.run(stream,overwrite_output=True)
    return excrated_audio 
def trancrible (audio):
    model = WhisperModel("small")
    segments , info = model.transcribe(audio)
    language = info[0]
    print(f"language: {language}")
    segments = list(segments)
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" %(segment.start,segment.end,segment.text)) # segment specifyer 
    return language , segment
def format_time(seconds): # done by gpt lol
# this function convert the time script into hours ig 
    hours = math.floor(seconds / 3600)
    seconds %= 3600
    minutes = math.floor(seconds / 60)
    seconds %= 60
    milliseconds = round((seconds - math.floor(seconds)) * 1000)
    seconds = math.floor(seconds)
    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:01d},{milliseconds:03d}"

    return formatted_time
def genrate_subtitle_file (lanuage, segments):
    subtitle_file = f"sub-{input_viedo_name}.{lanuage}.srt"
    text = ""
    for index , segment in enumerate(segments): # enumerate keep track of the index with the value
        segments_start = format_time(segment.start) # format time convert the number  into hh:mm:ss  
        segments_end = format_time(segment.end)
        text += f"{str(index+1)} \n"
        text += f"{segments_start} --> {segments_end} \n "
        text += f"{segment.text} " # need to input \n 
    with open(subtitle_file ,"w") as f:
        f.write(text)
        f.close()
        return subtitle_file
def add_subtitle_to_viedo (soft_subtitle , subtitle_file, subtitle_language):
    viedo_input_stream = ffmpeg.input(input_viedo)
    subtitle_input_stream = ffmpeg.input(subtitle_file)
    output_viedo = f"output-{input_viedo_name}.mp4" # need to do something for the overwrite 
    subtitle_track_title = subtitle_file.replace(".srt","")
    if soft_subtitle:
        stream = ffmpeg.output(
            viedo_input_stream,subtitle_input_stream,output_viedo **{"c": "copy","cs":"mov_text"},
            **{"metadata:s:s:0":f"lanuage={subtitle_language}",
            "metadata:s:s:0":  f"title={subtitle_track_title}"}
      )
    else:
        stream= ffmpeg.output(viedo_input_stream , output_viedo,
        vf =f"subtitles={subtitle_file}")
    ffmpeg.run(stream,overwrite_output=True)
# not writen the function starter yet 
