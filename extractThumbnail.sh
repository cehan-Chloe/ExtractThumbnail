#!/bin/bash
URL="$1"
# get the file name of video
file_name=$(basename "$URL")

wget "$URL"
# get the length of video, and choose the middle image as the thumbnail
# length=$(ffmpeg -i "$file_name" 2>&1 | grep 1/2 Duration | cut -d ' ' -f 4 | sed s/,//)
# ffmpeg -i "$file_name" -ss "$length" -vframes 1 "$file_name".png 

# save the frame at 00:00:00 as the thumbnail
ffmpeg -i "$file_name" -ss 00:00:00 -vframes 1 "$file_name".png 

mv "$file_name".png static/img/

printf "$file_name".png