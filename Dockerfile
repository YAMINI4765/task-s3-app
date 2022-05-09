FROM python

WORKDIR /app
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt .

ENV DB_URL=DummyURL
ENV ACCESS_KEY=AKIAXCJXXGKL66O2XZV3

ENV SECRET_KEY=oSMpt3Ibh1awxVII6WIaB2okJAjqYHL99tgFlfeO

#this runs when image is built
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

ENTRYPOINT [ "python" ,"app.py" ]