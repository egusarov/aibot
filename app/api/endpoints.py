from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Source, Keyword
from app.models.news import NewsItem

from app.api.schemas import (
    SourceCreate, SourceOut,
    KeywordCreate, KeywordOut,
    NewsOut,
)

from app.utils import get_db

router = APIRouter()


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/sources/", response_model=SourceOut)
def create_source(source: SourceCreate, db: Session = Depends(get_db)):
    db_source = Source(**source.dict())
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source


@router.get("/sources/", response_model=list[SourceOut])
def list_sources(db: Session = Depends(get_db)):
    return db.query(Source).all()


@router.delete("/sources/{source_id}")
def delete_source(source_id: str, db: Session = Depends(get_db)):
    source = db.query(Source).filter(Source.id == source_id).first()
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")

    db.delete(source)
    db.commit()
    return {"detail": "Source deleted"}


@router.post("/keywords/", response_model=KeywordOut)
def create_keyword(keyword: KeywordCreate, db: Session = Depends(get_db)):
    exists = db.query(Keyword).filter(Keyword.word == keyword.word).first()
    if exists:
        raise HTTPException(status_code=400, detail="Keyword already exists")

    db_keyword = Keyword(word=keyword.word)
    db.add(db_keyword)
    db.commit()
    db.refresh(db_keyword)
    return db_keyword


@router.get("/keywords/", response_model=list[KeywordOut])
def list_keywords(db: Session = Depends(get_db)):
    return db.query(Keyword).all()


@router.delete("/keywords/{keyword_id}")
def delete_keyword(keyword_id: str, db: Session = Depends(get_db)):
    keyword = db.query(Keyword).filter(Keyword.id == keyword_id).first()
    if not keyword:
        raise HTTPException(status_code=404, detail="Keyword not found")

    db.delete(keyword)
    db.commit()
    return {"detail": "Keyword deleted"}


@router.get("/news/", response_model=list[NewsOut])
def list_news(
        source: str | None = None,
        from_date: datetime | None = None,
        limit: int = 20,
        db: Session = Depends(get_db)
):
    query = db.query(NewsItem)

    if source:
        query = query.filter(NewsItem.source == source)

    if from_date:
        query = query.filter(NewsItem.created_at >= from_date)

    query = query.order_by(NewsItem.created_at.desc()).limit(limit)

    return query.all()
