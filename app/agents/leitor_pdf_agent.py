from google.adk.agents import LlmAgent
from ..tools.pdf_reader import pdf_reader_tool
import os
from dotenv import load_dotenv
load_dotenv()

model_name = os.getenv("MODEL_NAME")

leitor_pdf_agent = LlmAgent(
    name="leitor_pdf_agent",
    model=model_name,
    description="Lê e extrai texto bruto de arquivos PDF armazenados como artefatos.",
    instruction="Use a função pdf_reader_tool para extrair texto de PDFs pelo nome do artefato.",
    tools=[pdf_reader_tool]
)