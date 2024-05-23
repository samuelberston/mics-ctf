for i in {1000..9999};
do
  seq -f "%0${width}g" "$start" "$stop"
  echo $i
  openssl enc -aes-256-ecb -d -base64 -A -nosalt -k $i < flag.txt
  
done
