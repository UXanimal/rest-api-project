import rq
import os
import requests
import jinja2
from dotenv import load_dotenv

load_dotenv()

DOMAIN = os.getenv("MAILGUN_DOMAIN")
templateLoader = jinja2.FileSystemLoader(searchpath="templates")
template_env = jinja2.Environment(loader=templateLoader)

def render_template(template_filename, **context):
	return template_env.get_template(template_filename).render(**context)

def send_simple_message(to, subject, body, html):
    return requests.post(
		f"https://api.mailgun.net/v3/{DOMAIN}/messages",
		auth=("api", os.getenv("MAILGUN_API_KEY")),
		data={"from": "Matt C <mailgun@{DOMAIN}>",
			"to": [to],
			"subject": subject,
			"text": body,
			"html": html
		}
	)	

def send_user_registration_email(email, username):
	return send_simple_message(
            email, 
            "Welcome to Stores REST API", 
            f"Welcome, {username}! Thanks for registering for the Stores REST API. You can now log in and start creating stores and items!",
			render_template("email/action.html", username=username)				
	)	
	
	