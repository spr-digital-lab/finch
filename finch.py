#!/usr/bin/env python
import sys
import requests
import os
import readline

if len(sys.argv)<2:
  print("[-] No finch link provided.")
  exit()

link = sys.argv[1];
print("[+] Connecting to ",link);

def remote(query):
  payload = {'query': query}
  r = requests.post(link, data=payload)
  return r.json();

hello = remote('hello')
if hello['result']!="finch":
  print("[-] Unable to resolve connection to finch server.")
  exit()

print("[+] Connected to",link);

try:
  while True:
    query = input("FINCH >> ")
    if query == 'exit':
      exit()
    if query == 'clear':
      os.system("clear")
      continue
    response = remote(query)
    print(response['result'])
except KeyboardInterrupt:
  exit();
