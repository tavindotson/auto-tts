FROM python:alpine

WORKDIR /app

COPY . /app

RUN apk update
RUN apk upgrade
RUN apk add tmux 
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["tail"]
CMD ["-f","/dev/null"]
