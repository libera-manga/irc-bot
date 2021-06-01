
import psycopg2 # for Postgres database connection
from datetime import date, datetime, time, timedelta,timezone

import asyncio


# Postgres Database credentials
t_host = "172.18.0.4"
t_port = "5432" # Default postgres port
t_dbname = "postgres"
t_user = "postgres"
t_pw = "example"

db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_cursor = db_conn.cursor()


#Time
currTime = datetime.now(timezone.utc)


async def ingest():
        
        


    # Data validation would go here.

    #Add Statement to Create a DB if it already does not existotherwise continue
    #-- Basic table creation
#Important for uniqueness do not delete

#   a="""CREATE TABLE IF NOT EXISTS public.accounts (
# 	user_id serial PRIMARY KEY,
# 	username VARCHAR ( 50 ) UNIQUE NOT NULL,
# 	password VARCHAR ( 50 ) NOT NULL,
# 	email VARCHAR ( 255 ) UNIQUE NOT NULL,
# 	created_on TIMESTAMP NOT NULL,
#     last_login TIMESTAMP 
# );


    
    accounts="""CREATE TABLE IF NOT EXISTS public.accounts (
	user_id uuid NOT NULL PRIMARY KEY,
	username VARCHAR ( 255 )  NOT NULL,
	password VARCHAR ( 255 ) NOT NULL,
	email VARCHAR ( 255 )  NOT NULL,
	created_on TIMESTAMP NOT NULL,
    last_login TIMESTAMP);
    """

    manga_list = """
    CREATE TABLE IF NOT EXISTS public.list (
    user_id uuid NOT NULL ,
	manga_name VARCHAR( 255 ) NOT NULL,
	last_updated TIMESTAMP ( 255 )  NOT NULL ,
	latest_chapter TIMESTAMP ( 255 )  ,
	count BIGINT   NOT NULL );
    """
    # Helps deduplicate data
    list_constraint = """
    ALTER TABLE  public.list
    ADD CONSTRAINT list_constraint
    UNIQUE (user_id, manga_name, last_updated, latest_chapter) ;
    """

    
    
    
    


    db_cursor.execute(manga_list)
    db_cursor.execute(list_constraint)

    db_cursor.execute(accounts)


    db_conn.commit()


    try:
        db_conn.commit()
    except psycopg2.Error as e:
        # Create a message to send to the user with valuable information, including
        #    the error message and the SQL that caused the error.
        t_message = "Database error: " + e + "/n SQL: " + s
        print(t_message)
        # Notice: you may want to create a template page called "error.html" for handling errors.
        #   We are also sending a parameter along with our call to the page.

    # They got this far, meaning success
    # Clean up our Postgres database connection and cursor object
    db_cursor.close()
    db_conn.close()


if __name__ == "__main__":
    asyncio.run(ingest())