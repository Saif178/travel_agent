import os
from dotenv import load_dotenv
load_dotenv()
MODEL = os.getenv("OPENAI_MODEL", "gpt-5.4-mini")
