FROM python:3.8.5

WORKDIR /usr/src/app

COPY main.py .
COPY load_and_test.py .
COPY output.py .
COPY prep_cifar10.py .
COPY set_initials.py .
COPY shape_model.py .
COPY test.py .
COPY training.py .
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "./main.py"]

