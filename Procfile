web: gunicorn app:app
worker: celery -A application.tasks worker --loglevel=info
beat: celery -A application.tasks beat --loglevel=info
