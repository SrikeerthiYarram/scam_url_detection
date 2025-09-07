def load_blacklist():
    try:
        with open('../resources/icons/blacklist_urls.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Blacklist file not found.")
        return []

def is_blacklisted(item):
    blacklist = load_blacklist()
    return item in blacklist

# Example usage
if _name_ == "_main_":
    blacklist_data = load_blacklist()
    print("Blacklist:", blacklist_data)
    
    item_to_check = "example_url"
    if is_blacklisted(item_to_check):
        print(f"{item_to_check} is blacklisted.")
    else:
        print(f"{item_to_check} is not blacklisted.")
