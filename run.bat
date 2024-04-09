@echo off 

start cmd /k python -m uvicorn backend.api.searchAPI.main:app --port 8000
start cmd /k python -m uvicorn backend.api.personAPI.main:app --port 8001
start cmd /k python -m uvicorn backend.api.newsAPI.main:app --port 8002
start cmd /k python -m uvicorn backend.api.identityAPI.main:app --port 8003
start cmd /k python -m uvicorn backend.api.analyticsAPI.main:app --port 8004