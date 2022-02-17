import sys
import pytube
import os

temppercent = 0.0


def progress_function(stream, chunk, bytes_remaining):
    global temppercent
    percent = round((1 - bytes_remaining / downloaded.filesize) * 100)
    if percent != temppercent:
        print(str(percent) + '% done...')
        temppercent = percent


if __name__ == '__main__':
    youtubeLink = str(sys.argv[1:])
    fileLocation = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    video = pytube.YouTube(youtubeLink, on_progress_callback=progress_function)
    print("\nselected video: " + str(video.title))

    if input("everything right? [y/n] ") == "y":
        print("\navaible streams: ")
        avaiblestreams = video.streams.filter(progressive=True).order_by("resolution").desc()

        for i in range(len(avaiblestreams)):
            print("        " + str(i) + " >>> resolution: " + str(avaiblestreams[i].resolution) + ", datatype: " +
                  avaiblestreams[
                      i].mime_type + ", fps: " + str(avaiblestreams[i].fps) + "fps, type: " + str(
                avaiblestreams[i].type) +
                  ", vcodec: " + str(avaiblestreams[i].codecs[0]) +
                  ", acodec: " + str(avaiblestreams[i].codecs[1]))

        try:
            selectedstream = avaiblestreams[
                int(input("type number of avaible stream: "))]
            downloaded = video.streams.get_by_itag(selectedstream.itag)
            print("\nDownload started ...\n")
            downloaded.download(fileLocation)
            print("\nDownload completed. :-)")
        except:
            print("\nSomething went wrong. Try again! \n")
