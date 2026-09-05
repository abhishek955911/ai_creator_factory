from utils.database import engine
from utils.models import Base


Base.metadata.create_all(engine)

print("Database tables created successfully.")