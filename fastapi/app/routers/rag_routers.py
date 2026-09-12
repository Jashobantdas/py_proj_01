from fastapi import Depends, UploadFile, File, HTTPException
from fastapi.routing import APIRouter

from configs.dependency_service import get_rag_service
from services.rag_service import RagService

from pathlib import Path
import shutil

r_router = APIRouter()

@r_router.get("/question_answer/{question}")
def get_question_answer(question : str, service: RagService = Depends(get_rag_service)):
    return {"question": service.question_answer(question)}

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

MAX_FILE_SIZE = 500 * 1024 * 1024  # 500 MB
CHUNK_SIZE = 1024 * 1024           # 1 MB


@r_router.post("/documents/upload")
async def upload_pdf(file: UploadFile = File(...), service: RagService = Depends(get_rag_service)):

    # 1. Validate extension
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is required"
        )

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )

    file_path = UPLOAD_DIR / file.filename
    total_size = 0

    try:
        # 3. Stream file to disk
        with open(file_path, "wb") as buffer:

            while True:
                chunk = await file.read(CHUNK_SIZE)

                if not chunk:
                    break

                total_size += len(chunk)

                # 4. Validate size while streaming
                if total_size > MAX_FILE_SIZE:
                    file_path.unlink(missing_ok=True)

                    raise HTTPException(
                        status_code=413,
                        detail="File size cannot exceed 500 MB"
                    )

                buffer.write(chunk)

    finally:
        await file.close()

    return {
        "filename": file.filename,
        "size_mb": round(total_size / (1024 * 1024), 2),
        "path": str(file_path),
        "status": "UPLOADED"
    }