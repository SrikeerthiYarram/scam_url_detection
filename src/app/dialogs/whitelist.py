def load_whitelist():
    try:
        with open('../resources/icons/whitelist_urls.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print("Whitelist file not found.")
        return []

def is_whitelisted(item):
    whitelist = load_whitelist()
    return item in whitelist

# Example usage
if _name_ == "_main_":
    whitelist_data = load_whitelist()
    print("Whitelist:", whitelist_data)
    
    item_to_check = "example_url"
    if is_whitelisted(item_to_check):
        print(f"{item_to_check} is whitelisted.")
    else:
        print(f"{item_to_check} is not whitelisted.")
