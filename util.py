from datetime import datetime
from rich import print

def time() -> str: return datetime.now().strftime('%H:%M:%S')
def log(s: str) -> None: print(f'[{time()}] {s}')