import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = True
    HTTPS_PROXY_USERNAME = os.environ.get("HTTPS_PROXY_USERNAME")
    HTTPS_PROXY_PASSWORD = os.environ.get("HTTPS_PROXY_PASSWORD")
    VGS_VAULT = os.environ.get("VGS_VAULT")
    CERT_PATH = os.environ.get("CERT_PATH")

