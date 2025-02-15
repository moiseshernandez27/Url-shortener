from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import SessionLocal 
from app.services import generate_short_url, store_url, get_cached_url, cache_url
from app.models import URL



router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/shorten")
async def shorten_url(original_url: str, db: Session = Depends(get_db)):
    short_url = generate_short_url(original_url)
    url_in_cache = await get_cached_url(short_url)
    if url_in_cache:
        return{"short_url": short_url, "original_url": url_in_cache}
    
    db_url = store_url(db, original_url, short_url)
    await cache_url(short_url, db_url.original_url)
    if url_in_cache:
        return {"short_url": short_url, "original_url": db_url.original_url}
    
@router.get("/{short_url}")
async def redirect_to_url(short_url: str, db: Session = Depends(get_db)):
    original_url = await get_cached_url(short_url)
    if not original_url:
        url = db.query(URL).filter(URL.short_url == short_url).first()
        if not url:
            raise HTTPException(status_code=404, detail="URL not found")
        original_url = url.original_url
        await cache_url(short_url, original_url)
    return {"original_url": original_url}
