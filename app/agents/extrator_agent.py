from google.adk.agents import LlmAgent
import os
from dotenv import load_dotenv
load_dotenv()

model_name = os.getenv("MODEL_NAME")

extrator_agent = LlmAgent(
    name="extrator_agent",
    model=model_name,
    description="Extrai dados relevantes do texto classificado.",
    instruction="Receba texto classificado e extraia dados relevantes, como nomes, datas, valores, e outros campos importantes.",
)