BLACKLIST_FILE = '../resources/icons/blacklist_urls.txt'  # your actual file

def load_blacklist():
    """Load blacklist dynamically from file"""
    try:
        with open(BLACKLIST_FILE, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Blacklist file not found.")
        return []

def is_blacklisted(url):
    """Check if a URL is in the blacklist"""
    blacklist = load_blacklist()
    for entry in blacklist:
        if entry in url:
            return True, entry  # matched entry
    return False, None

def add_to_blacklist(url):
    """Add a URL to the blacklist dynamically"""
    with open(BLACKLIST_FILE, 'a') as f:
        f.write(url + "\n")

