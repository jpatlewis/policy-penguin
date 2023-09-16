from app.app import app
import sys

if __name__ == '__main__':
    try:
        app.run(host="0.0.0.0", debug=True)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {str(e)}", file=sys.stderr)
