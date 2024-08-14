import os

class Settings:
     DATABASE_URL: str = os.getenv("postgresql://sit722_part2_pkca_user:bJrNcboTxU39r0036DKW2QDF5d4HwOoo@dpg-cqu38o3v2p9s73cvuehg-a.oregon-postgres.render.com/sit722_part2_pkca")

settings = Settings()
