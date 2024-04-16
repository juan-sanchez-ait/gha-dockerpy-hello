FROM python:3
COPY greeting.py /greeting.py
CMD ["python", "/greeting.py"]