def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret): #FIX: Refactored logic into logic_utils.py using agent mode and swapped the hint logic to match the correct outcome Higher or Lower
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    try:
        guess_int = int(guess)
        secret_int = int(secret)
    except (ValueError, TypeError):
        return "Too Low", "📈 Go HIGHER!"

    if guess_int == secret_int:
        return "Win", "🎉 Correct!"
    if guess_int > secret_int:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
