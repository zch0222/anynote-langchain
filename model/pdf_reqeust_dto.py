from pydantic import BaseModel


class PDFRequestDTO(BaseModel):
    url: str
    question: str
    user_id: int
    file_key: str
