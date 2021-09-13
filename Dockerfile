FROM debian
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TOKEN 1981206468:AAFyK6Umdh3aG9-XNAmx4IOgxEytEaiZ5ZI
ENV TEXT_FILE t.txt
ENV IMAGE_DIR images
ENV FONT_FILE Lobster.ttf
ENV REPOST_CHANNEL -1001277471725
WORKDIR /app/
COPY . .
RUN apt update && apt install -y --no-install-recommends python3-minimal python3-setuptools python3-pip
RUN python3 -m pip install --no-cache-dir -r requirements.txt
CMD [ "python3", "main.py" ]
