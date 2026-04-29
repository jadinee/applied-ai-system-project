def get_range_for_difficulty(difficulty: str):
    if difficulty == "Easy":
        return 1, 50
    elif difficulty == "Medium":
        return 1, 100
    elif difficulty == "Hard":
        return 1, 200
    else:
        return 1, 100


def parse_guess(raw: str):
    try:
        guess = int(raw)
        return True, guess, None
    except:
        return False, None, "Please enter a valid number."


def check_guess(guess, secret):
    if guess == secret:
        return "Win", "Correct. You found the number."

    diff = abs(guess - secret)

    if diff <= 5:
        closeness = "very close"
    elif diff <= 15:
        closeness = "close"
    else:
        closeness = "far"

    if guess > secret:
        return "Too High", f"Too high. You are {closeness}."
    else:
        return "Too Low", f"Too low. You are {closeness}."


def update_score(current_score: int, outcome: str, attempt_number: int):
    if outcome == "Win":
        return current_score + max(0, 100 - attempt_number * 10)
    return current_score