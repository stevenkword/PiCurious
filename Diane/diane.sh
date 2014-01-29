#!/bin/bash

echo "Recording... Press Ctrl+C to Stop."

/home/pi/PiAUISuite/Personas/Diane/speech2text.sh

QUESTION=$(cat stt.txt)

#QUESTION=$1
echo "Me: ", $QUESTION

ANSWER=$(python /home/pi/PiAUISuite/Personas/Diane/querywolfram.py $QUESTION)
echo "Robot: ", $ANSWER

/home/pi/PiAUISuite/Personas/Diane/text2speech.sh $ANSWER
