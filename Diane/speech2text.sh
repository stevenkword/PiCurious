#!/bin/bash

echo "Recording..."
arecord -D "plughw:0,0" --duration=4 -q -f cd -t wav | ffmpeg -loglevel panic -y -i - -ar 16000 -acodec flac file.flac > /dev/null 2>&1

echo "Processing..."
wget -q -U "Mozilla/5.0" --post-file file.flac --header "Content-Type: audio/x-flac; rate=16000" -O - "https://www.google.com/speech-api/v1/recognize?xjerr=1&client=chromium&lang=en-US" | cut -d\" -f12  >stt.txt

#echo -n "Result: "
cat stt.txt

rm file.flac  > /dev/null 2>&1
