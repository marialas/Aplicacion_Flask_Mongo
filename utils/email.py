import yagmail
import os
from dotenv import load_dotenv

load_dotenv()

def enviarCorreo(destinatario, asunto, mensaje, archivos=None):
    yag = yagmail.SMTP(user=os.getenv("CORREO_APP"), password=os.getenv("CLAVE_APP"))
    yag.send(to=destinatario, subject=asunto, contents=mensaje, attachments=archivos)
