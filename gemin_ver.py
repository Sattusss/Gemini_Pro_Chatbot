import google.generativeai as gen_ai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
gen_ai.configure(api_key=api_key)

models = gen_ai.list_models()
for m in models:
    print(m.name)