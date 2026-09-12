import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from configs.exception_handler import register_exception_handlers
from routers.department_routers import d_router
from routers.employee_routers import e_router
from routers.model_routers import m_routers
from routers.product_routers import p_router
from routers.rag_routers import r_router
from routers.user_routers import u_router

import os

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    e_router,
    prefix="/employee",
    tags=["employee"],
)

app.include_router(
    r_router,
    prefix="/rag",
    tags=["rag"],
)

app.include_router(
    d_router,
    prefix="/department",
    tags=["department"]
)

app.include_router(
    p_router,
    prefix="/products",
    tags=["products"]
)

app.include_router(
    m_routers,
    prefix="/models",
    tags=["models"]
)

app.include_router(
    u_router,
    prefix="/user",
    tags=["user"],
)

app.include_router(m_routers, prefix="/model", tags=["model"])

@app.get("/")
def health():
    return {"message" : "ok", "OPENAI_API_KEY" : os.getenv("OPENAI_API_KEY")}


register_exception_handlers(app)

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )