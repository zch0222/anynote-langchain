from pydantic import BaseModel


class PdfVO(BaseModel):
    message: str

    def to_dic(self):
        return {
            "message": self.message
        }
