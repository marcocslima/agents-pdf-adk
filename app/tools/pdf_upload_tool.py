import google.genai.types as types
from google.adk.tools.tool_context import ToolContext
import base64

async def pdf_upload_tool(tool_context: ToolContext, filename: str, file_bytes: str):
    try:
        decoded_bytes = base64.b64decode(file_bytes)
    except Exception as e:
        return {"status": "error", "message": f"Falha ao decodificar arquivo: {e}"}

    artifact = types.Part.from_bytes(data=decoded_bytes, mime_type="application/pdf")

    try:
        version = await tool_context.save_artifact(filename=filename, artifact=artifact)
        return {"status": "success", "message": f"Arquivo salvo como artefato versão {version}"}
    except Exception as e:
        return {"status": "error", "message": f"Erro ao salvar artefato: {e}"}