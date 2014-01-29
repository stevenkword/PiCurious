# write an English text string as an audio file using Google Translate
# usage: en2audio.sh <text>
#echo $1
#echo $*
#LANGUAGE=en
LANGUAGE=en_gb #Diane: Trainspotting
#LANGUAGE=en_au
#LANGUAGE=$2
wget -q -U Mozilla -O "converted.mp3" "http://translate.google.com/translate_tts?ie=UTF-8&tl=$LANGUAGE&q=$*" 
mpg321 -q converted.mp3
#rm converted.mp3
