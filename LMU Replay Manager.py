import requests
import json
import sys
import time

while True:
    try:
        saved_replay = requests.get("http://localhost:6397/rest/watch/replays").json()
    except requests.ConnectionError:
        print("== Le Mans Ultimate is not running! Run the script after launching LMU.", file=sys.stderr)
        print("== Exiting in 10 seconds...")
        time.sleep(10)
        break
        
    readable = [f" * id: {item["id"]} | Replay Name: {item["replayName"]}" for item in saved_replay]
    print("\n".join(readable))
    id_replay = input("\n== Enter id of the replay file to load (e.g. 0), or -1 to exit: ")
    try:
        id_replay = int(id_replay.strip())
        if id_replay == -1:
            break
        requests.get(f"http://localhost:6397/rest/watch/play/{id_replay}")
        print("== Loading Replay... Check the game screen.")
        time.sleep(30)
        break
    except:
        print("!! Invalid id. Try again.", file=sys.stderr)