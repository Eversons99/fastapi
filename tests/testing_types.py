def do_full_name(first_name: str, last_name: str) -> str:
    """
    Type hinting in arguments
    """
    return f"{first_name.capitalize()} {last_name.capitalize()}"


if __name__ == "__main__":
    # Test the function with a sample input
    first_name = "john"
    last_name = "doe"       
    full_name = do_full_name(first_name, last_name)
    print(full_name)  # Output: John Doe