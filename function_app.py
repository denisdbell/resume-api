import azure.functions as func
import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2
from psycopg2.extras import RealDictCursor
import uuid
from datetime import date
import os
import json
#import azure.keyvault 
#from azure.keyvault.secrets import SecretClient
#from azure.identity import DefaultAzureCredential


# Define connection parameters from environment variables
#keyVaultName = os.environ["KEY_VAULT_NAME"]
#KVUri = f"https://{keyVaultName}.vault.azure.net"

##credential = DefaultAzureCredential()
##client = SecretClient(vault_url=KVUri, credential=credential)

DB_HOST = os.environ["PGHOST"]
DB_USER = os.environ["PGUSER"]
DB_PASSWORD = os.environ["PGPASSWORD"]
DB_NAME = os.environ["PGDATABASE"]
DB_PORT = os.environ["PGPORT"]

# Connect to the PostgreSQL database
'''
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        dbname=DB_NAME,
        port=DB_PORT
    )
    return conn
'''

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)
@app.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    #logging.info('Python HTTP trigger function processed a request.')
    #conn = get_db_connection()
    #cursor = conn.cursor(cursor_factory=RealDictCursor)
    success = True
    '''
    try:
       
        success = True
    
        count = ""
        ##Insert visitor
        visit_id = str(uuid.uuid4())
        visitor_ip = req.headers.get("X-FORWARDED-FOR")
        #visitor_ip = "TESTIP"
        sql = "INSERT INTO public.resume_visitor_counter (visitor_ip, visit_time, visit_id) VALUES ('"+ visitor_ip +"',now(),'"+ visit_id +"')"
        print(sql)
        #logging.info('Adding visitor ' + visit_id)
        cursor.execute(sql)
        conn.commit()

        ##Get visitor count
        cursor.execute("SELECT COUNT(*) FROM public.resume_visitor_counter")
        visitors = cursor.fetchall()
        count = {"visitors": visitors}
    except Exception as e:
        success = False
        conn.rollback()
    # raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    '''
    count = {"visitors": "test"}

    if success:
        return func.HttpResponse(
             #json.dumps(count),
             json.dumps(count),
             mimetype="application/json",
        )
    else:
        return func.HttpResponse("Response failed ")