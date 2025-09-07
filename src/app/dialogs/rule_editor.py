# ------------------ HEURISTIC FUNCTION ------------------
def evaluate_url(url: str, blacklist=None, whitelist=None) -> dict:
    """
    Heuristic URL evaluator.
    Returns a dict with:
        - url: str
        - score: int
        - verdict: "Safe"|"Suspicious"|"Malicious"
        - matched_rules: list of { "rule": str, "explanation": str, "weight": int }
    """
    if blacklist is None:
        blacklist = ["badsite.com", "malware.com"]
    if whitelist is None:
        whitelist = ["example.com", "trustedsite.org"]

    matched_rules = []
    score = 0
    url_lower = url.lower()

    # ----- HEURISTIC RULES -----

    # Rule 1: Blacklist match
    for b in blacklist:
        if b in url_lower:
            matched_rules.append({
                "rule": "Blacklist match",
                "explanation": f"URL matches blacklisted domain '{b}'",
                "weight": 10
            })
            score += 10

    # Rule 2: Whitelist match (reduces suspicion)
    for w in whitelist:
        if w in url_lower:
            matched_rules.append({
                "rule": "Whitelist match",
                "explanation": f"URL matches trusted domain '{w}'",
                "weight": -5
            })
            score -= 5

    # Rule 3: Unsecure login page
    if "login" in url_lower and not url_lower.startswith("https://"):
        matched_rules.append({
            "rule": "Unsecure login page",
            "explanation": "Login page is not HTTPS",
            "weight": 5
        })
        score += 5

    # Rule 4: Suspicious keywords
    suspicious_keywords = ["free", "bonus", "click", "verify", "update"]
    for keyword in suspicious_keywords:
        if keyword in url_lower:
            matched_rules.append({
                "rule": "Suspicious keyword",
                "explanation": f"URL contains suspicious keyword '{keyword}'",
                "weight": 3
            })
            score += 3

    # Rule 5: Long URL
    if len(url) > 75:
        matched_rules.append({
            "rule": "Long URL",
            "explanation": "URL length is unusually long",
            "weight": 2
        })
        score += 2

    # ----- DECIDE VERDICT -----
    if score <= 0:
        verdict = "Safe"
    elif score <= 7:
        verdict = "Suspicious"
    else:
        verdict = "Malicious"

    # Return results in required format
    return {
        "url": url,
        "score": score,
        "verdict": verdict,
        "matched_rules": matched_rules
    }
