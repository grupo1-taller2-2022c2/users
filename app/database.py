import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# database prod: "postgresql://xossdlbipiwucq:5644bec1e5a0f1ca947c878cb07fcfe8723c18d05cb7011d8c914100a0ab9095@ec2-18-214-35-70.compute-1.amazonaws.com:5432/d2groiiegd881h"
SQLALCHEMY_DATABASE_URL = os.getenv('DATABASE_URL')
# SQLALCHEMY_DATABASE_URL = "postgresql://xossdlbipiwucq:5644bec1e5a0f1ca947c878cb07fcfe8723c18d05cb7011d8c914100a0ab9095@ec2-18-214-35-70.compute-1.amazonaws.com:5432/d2groiiegd881h"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
