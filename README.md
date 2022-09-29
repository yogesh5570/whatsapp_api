# WhatsApp API to reply received messages and store them in MongoDB as well 

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Requirements.

```bash
pip install -r requirement.txt
```

### Add .env File
Add Twilio account Creds in your .env file which will be in project folder.
```bash
MONGODB_CONNECTION=<Mongo DB Connection String>

TWILIO_ACCOUNT_SID=<Twilio Account SID>
TWILIO_AUTH_TOKEN=<Twilio Auth Token>


```

## Command to Run
```bash
python app.py
```

This command will run a local server but it will not work yet because to configure it on twilio we need to deploy it first and add that link to whatsApp Sandbox.
