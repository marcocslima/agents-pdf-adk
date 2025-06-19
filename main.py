import asyncio
import base64
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts import InMemoryArtifactService
from google.genai import types

from app.workflows.team_agent import team_agent

from dotenv import load_dotenv
load_dotenv()

async def main():
    app_name = "agents_pdf_app"
    user_id = "user_1"

    session_service = InMemorySessionService()
    artifact_service = InMemoryArtifactService()
    runner = Runner(
        agent=team_agent,
        app_name=app_name,
        session_service=session_service,
        artifact_service=artifact_service
    )

    # Cria uma sessão
    session = await session_service.create_session(app_name=app_name, user_id=user_id)

    # Simula upload do PDF: leia um arquivo local e converta para base64
    with open("exemplo.pdf", "rb") as f:
        pdf_bytes = f.read()
    pdf_b64 = base64.b64encode(pdf_bytes).decode("utf-8")

    # Chama a ferramenta de upload para salvar o PDF como artefato
    upload_message = types.Content(
        role="user",
        parts=[types.Part(text=f'{{"tool":"pdf_upload_tool","parameters":{{"filename":"exemplo.pdf","file_bytes":"{pdf_b64}"}}}}')]
    )
    events = runner.run(user_id=user_id, session_id=session.id, new_message=upload_message)
    for event in events:
        if event.is_final_response():
            print("Upload response:", event.content.parts[0].text)

    # Agora envia mensagem para ler o PDF salvo
    read_message = types.Content(
        role="user",
        parts=[types.Part(text="Por favor, leia o arquivo 'exemplo.pdf' e extraia o texto.")]
    )
    events = runner.run(user_id=user_id, session_id=session.id, new_message=read_message)
    for event in events:
        if event.is_final_response():
            print("Leitura do PDF:", event.content.parts[0].text)

if __name__ == "__main__":
    asyncio.run(main())