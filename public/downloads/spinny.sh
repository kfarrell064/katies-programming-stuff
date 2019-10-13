# -n makes sure the echo doesn't start a new line
# -e makes sure the echo interprets the escape character, \r
# \r makes a carriage return after each character (basically erasing it,
# because new text is not started on the next line

chars="/-\|"

while :; do
  for (( i=0; i<${#chars}; i++ )); do
    sleep 0.5
    echo -en "${chars:$i:1}" "\r" 
  done
done
