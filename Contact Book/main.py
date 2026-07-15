import subprocess
import sys
from pathlib import Path


if __name__ == "__main__":
    app_path = Path(__file__).with_name("contact_book.py")
    subprocess.run([sys.executable, "-m", "streamlit", "run", str(app_path), "--server.headless", "true"])

