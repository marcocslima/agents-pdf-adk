from google.adk.agents import LlmAgent
import os
from dotenv import load_dotenv
load_dotenv()

model_name = os.getenv("MODEL_NAME")

classificador_agent = LlmAgent(
    name="classificador_agent",
    model=model_name,
    description="Classifica o conteúdo extraído do PDF em categorias relevantes.",
    instruction="Receba texto extraído de um PDF e classifique em categorias como: financeiro, jurídico, técnico, etc.",
)