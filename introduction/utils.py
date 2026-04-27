def sanitize_username(username: str) -> str:
    """
    Sanitize a username by stripping whitespace and converting to lowercase.

    Args:
        username: Raw username string from user input

    Returns:
        Sanitized username string
    """
    if not isinstance(username, str):
        raise TypeError(f"Expected str, got {type(username).__name__}")
    return username.strip().lower()


def is_valid_email(email: str) -> bool:
    """
    Check if an email address contains an @ symbol and a domain.

    Args:
        email: Email address string to validate

    Returns:
        True if email looks valid, False otherwise
    """
    if not isinstance(email, str):
        raise TypeError(f"Expected str, got {type(email).__name__}")
    parts = email.strip().split("@")
    return len(parts) == 2 and len(parts[0]) > 0 and "." in parts[1]
