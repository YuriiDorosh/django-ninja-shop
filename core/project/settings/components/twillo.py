import environ


env = environ.Env()
environ.Env.read_env()

TWILIO_ACCOUNT_SID = env("MY_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = env("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = env("MY_TWILIO_NUMBER")
