#!python
import sys
import json

from os import getenv, remove
from pathlib import Path
from datetime import datetime

verbs = [
  "add", "delete", "edit", "clearall", "get"
]

home_dir = getenv("USERPROFILE")

note_file = f"{home_dir}\\.note"

now = datetime.now()

def verify_file_integrity():
  try:
    with open(note_file) as f:
      json.load(f)
    return True
  except:
    return False

def verify_verbs(s):
  if s in verbs:
    return True
  return False

def add(text):
  # attempt to load the file
  temp = {
    "date_time": now.strftime("%H:%M %d/%m/%y"),
    "note": text
  }
  if verify_file_integrity():
    with open(note_file) as f:
      data = json.load(f)
    last_entry = int(list(data.keys())[-1])
    new_entry = last_entry + 1
    out = {
      new_entry: temp
    }
    
    data.update(out)

    with open(note_file, 'w') as f:
      json.dump(data, f)

    print(json.dumps(out))
  else:
    print("failed integrity check")
    new_entry = 1
    out = {
      new_entry: temp
    }
    with open(note_file, 'w') as f:
      json.dump(out, f)

    print(json.dumps(out))

def get():
  if verify_file_integrity():
    with open(note_file) as f:
      data = json.load(f)
    keys = list(data.keys())
    
    for key in keys:
      temp = data[key]
      print("Date/Time : " + temp['date_time'])
      print("Note:\n\t" + temp['note'] + "\n")
      print("-----------------------")
  else:
    print("no notes saved")

def clearall():
  if verify_file_integrity():
    remove(note_file)
  else:
    print("failed integrity check...")

if __name__ == "__main__":
  if len(sys.argv) <= 1:
    print("not enough information provided")
    exit(1)

  verb = sys.argv[1].lower()

  if not verify_verbs(verb) or not verb.isalpha():
    print(f"invalid verb '{verb}' provided.")
    print(f"following are the verbs approved: {verbs}")
    exit(1)

  if not Path(note_file).exists():
    Path(note_file).touch()
  
  if verb == "add":
    if len(sys.argv) <= 2:
      print("please provide information you wish to add")
      exit(2)
    add(sys.argv[2])
  elif verb == "get":
    get()
  elif verb == "clearall":
    clearall()