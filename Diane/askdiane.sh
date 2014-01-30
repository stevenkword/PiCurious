#!/bin/bash

#echo "Recording... Press Ctrl+C to Stop."

#./speech2text.sh

#QUESTION=$(cat stt.txt)

QUESTION=$1
echo "Me: ", $QUESTION

ANSWER=$(python ./querywolfram.py $QUESTION)
echo "Robot: ", $ANSWER

./text2speech.sh $ANSWER