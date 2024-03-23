from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    DOCUMENT_PATH: str
    PFX_FILE: str
    CERT_PEM_FILE: str
    PASSPHRASE: str

    class Config:
        env_file = ".env"  # Specify the path to your .env file

app_settings = AppSettings()

