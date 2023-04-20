FROM python:3.8.10-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install Flask==1.1.4
RUN pip install Werkzeug==0.16.1
RUN pip install python-dotenv==0.17.1
RUN pip install click==7.1.2
RUN pip install Flask-SQLAlchemy==2.5.1
RUN pip install Flask-Login==0.5.0
RUN pip install psycopg2-binary==2.8.6
RUN pip install MarkupSafe==2.0.1
RUN pip install Flask-Migrate==3.0.0
RUN pip install SQLAlchemy==1.3.24
RUN pip install Flask-COMBO-JSONAPI==1.0.7
RUN pip install alembic==1.10.2
RUN pip install apispec==4.7.1
RUN pip install certifi==2022.12.7
RUN pip install WTForms==2.3.3
RUN pip install Flask-WTF==0.15.1
RUN pip install email-validator==1.1.2
RUN pip install Flask-Admin==1.5.8
RUN pip install PyYAML==5.4.1
RUN pip install ComboJSONAPI==1.1.1
#--no-cache -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
# "python3", "-m" ,
