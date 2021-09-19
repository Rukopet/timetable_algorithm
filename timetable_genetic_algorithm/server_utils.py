from pathlib import Path

import psycopg2
from . import config


def send_email(to_email: str, file, filename: str = 'Timetable.xls'):
    import smtplib
    import ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    message = MIMEMultipart()
    message["From"] = 'example.timetable.ru@gmail.com'
    message["To"] = to_email
    message["Subject"] = "Генерация расписания"
    message["Bcc"] = to_email  # Recommended for mass emails

    message.attach(MIMEText("Выбранный формат отправки", "plain"))

    with file.open('rb') as attachment:
        timetable = MIMEBase("application", "octet-stream")
        timetable.set_payload(attachment.read())

    encoders.encode_base64(timetable)
    timetable.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(timetable)
    text = message.as_string()

    port = 465  # For SSL
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("example.timetable.ru@gmail.com", 'qscwdv4321')
        server.sendmail('example.timetable.ru@gmail.com', to_email, text)


class PostgresClass:
    @classmethod
    def _connection_with_db(cls):  # returning psycopg2 connect
        return psycopg2.connect(dbname=config.POSTGRES_DB,
                                user=config.POSTGRES_USER,
                                password=config.POSTGRES_PASSWORD,
                                host=config.DB_HOST)

