def fetch_meeple():
    try:
        open("meeple.json")
    except FileNotFoundError:
        return None
