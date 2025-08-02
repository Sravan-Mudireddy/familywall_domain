def is_safe_input(description):
    banned_keywords = [
        "adult", "nude", "sex", "drugs", "weapons", "weapon", "hate", "suicide",
        "bully", "hacker", "kill", "violent", "explicit", "porn", "fraud", "bomb"
    ]
    return not any(word in description.lower() for word in banned_keywords)
