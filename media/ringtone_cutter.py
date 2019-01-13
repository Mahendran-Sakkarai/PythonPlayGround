import moviepy.editor as moviepy
from pymediainfo import MediaInfo

while True: 
    file_location = input("> Enter the location of the file: ")
    start_location = int(input("> Enter the starting location(in sec): "))
    end_location = int(input("> Enter the ending location(in sec): "))
    output_location = input("> Enter the output file location(Default - the input folder with _ringtone.mp3): ")
    if output_location == "" :
        output_location = file_location[0:file_location.rfind(".")] + "_ringtone.mp3"

    clip = moviepy.AudioFileClip(file_location).subclip(start_location,end_location)
    clip.write_audiofile(output_location)

    retry = input("> Retry (Y or N):")
    if retry.lower() == "n":
        break