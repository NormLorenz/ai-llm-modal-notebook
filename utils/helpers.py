# utils/helpers.py

def greet(name: str) -> str:
    return f"Hello, {name.title()}!"

def log(msg: str) -> None:
    from datetime import datetime
    print(f"[{datetime.now().isoformat()}] {msg}")