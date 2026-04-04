from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.reference import Reference

router = APIRouter(prefix="/api/references", tags=["references"])


class RefCreate(BaseModel):
    page_id: int
    title: str = ""
    arxiv_id: str | None = None
    doi: str | None = None
    url: str | None = None


class RefOut(BaseModel):
    id: int
    page_id: int
    title: str
    arxiv_id: str | None
    doi: str | None
    url: str | None

    model_config = {"from_attributes": True}


@router.get("", response_model=list[RefOut])
def list_references(page_id: int, db: Session = Depends(get_db)):
    return db.query(Reference).filter(Reference.page_id == page_id).all()


@router.post("", response_model=RefOut, status_code=201)
def create_reference(body: RefCreate, db: Session = Depends(get_db)):
    ref = Reference(page_id=body.page_id, title=body.title, arxiv_id=body.arxiv_id, doi=body.doi, url=body.url)
    db.add(ref)
    db.commit()
    db.refresh(ref)
    return ref
