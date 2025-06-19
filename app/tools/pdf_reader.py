import pdfplumber
from io import BytesIO
from google.adk.tools.tool_context import ToolContext

async def pdf_reader_tool(tool_context: ToolContext, filename: str) -> dict:
    artifact = await tool_context.load_artifact(filename=filename)
    if not artifact or not artifact.inline_data:
        return {
            "status": "error",
            "text": "",
            "message": f"Arquivo '{filename}' não encontrado como artefato."
        }

    pdf_bytes = artifact.inline_data.data
    try:
        with pdfplumber.open(BytesIO(pdf_bytes)) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return {
            "status": "success",
            "text": text,
            "message": f"Texto extraído com sucesso de {len(pdf.pages)} páginas"
        }
    except Exception as e:
        return {
            "status": "error",
            "text": "",
            "message": f"Erro ao ler PDF: {str(e)}"
        }