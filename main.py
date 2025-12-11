from sqlalchemy import text
from fastapi import Depends, FastAPI
from app.core.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

@app.get("/")
async def test(db: AsyncSession = Depends(get_db)):
    return await db.execute(text("SELECT 1;"))