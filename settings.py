

from dotenv import load_dotenv
import os
from open_router import get_model
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()
api_key = os.getenv("OPEN_ROUTER_API_KEY")

MODEL = get_model()  # "deepseek/deepseek-r1-0528:free"

def get_model_client():
    client = OpenAIChatCompletionClient(
        model=MODEL,
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1", 
        model_info={ 
            "family": "deepseek",
            "vision": True,
            "function_calling": True,
            "json_output": False,
            "structured_output": False,  
        }
    )
    return client
