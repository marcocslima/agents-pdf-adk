from google.adk.agents import SequentialAgent
from ..agents.leitor_pdf_agent import leitor_pdf_agent
from ..agents.classificador_agent import classificador_agent
from ..agents.extrator_agent import extrator_agent
from ..tools.pdf_upload_tool import pdf_upload_tool

leitor_pdf_agent.tools.append(pdf_upload_tool)

team_agent = SequentialAgent(
    name="team_agent",
    description="Time de agentes para processar PDFs: leitura, classificação e extração.",
    sub_agents=[leitor_pdf_agent, classificador_agent, extrator_agent]
)