import hashlib
from sqlalchemy.orm import Session
import aioredis
from app.models import URL 

redis = aioredis.from_url("redis://localhost")

def generate_short_url(original_url: str) -> str:
    return hashlib.md5(original_url.encode()).hexdigest()[:6]

async def get_cached_url(short_url: str) -> str:
    url= await redis.get(short_url)
    return url.decode() if url else None

async def cache_url(short_url:str, original_url: str):
        await redis.set(short_url, original_url, ex=3600) #1 hora de cache 

def store_url(db:Session, original_url: str, short_url: str) -> URL:
      db_url = URL(original_url=original_url, short_url=short_url)
      db.add(db_url)
      db.commit()
      db.refresh(db_url)
      return db_url




