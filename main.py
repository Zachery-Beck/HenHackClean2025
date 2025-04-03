"""
This module serves as the entry point for the Flask application.

Functions:
    main(): Starts the Flask application.
"""

from flask_backend import app

def main():
    """
    Starts the Flask application.

    Returns:
        None
    """
    try:
        app.run()
    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
