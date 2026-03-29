# 📄 Document Processing System

## 🚀 Overview
This project is a full-stack asynchronous document processing system built using:

- FastAPI (Backend)
- React (Frontend)
- PostgreSQL (Database)
- Celery (Background Workers)
- Redis (Queue + Pub/Sub)

---

## ⚙️ Features

- Upload documents
- Async background processing
- Real-time progress tracking
- Edit processed data
- Retry failed jobs
- Export results

---

## 🏗 Architecture

Frontend → FastAPI → Celery Worker → Redis → PostgreSQL

---

## ▶️ How to Run

### Backend
cd backend  
pip install -r requirements.txt  
uvicorn app.main:app --reload  

### Celery
celery -A app.workers.celery_app.celery worker --loglevel=info  

### Redis
redis-server  

### Frontend
cd frontend  
npm install  
npm start  

---

## 📊 Workflow

1. Upload document  
2. Background processing starts  
3. Progress updates via Redis  
4. Final result stored  
5. User can edit/export  

---

## 🎥 Demo Video
(Add your video link here)

---

## 📌 Assumptions
- Processing logic is mocked
- Focus is on async system design

---

## ⚠️ Limitations
- No authentication
- No file storage system

---

## ⭐ Future Improvements
- WebSockets for real-time updates
- Authentication
- File storage (S3)

