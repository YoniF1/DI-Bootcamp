import psycopg2
import config
import requests
import random

class Countries:

    @classmethod
    def fetch_country_data(cls):
        response = requests.get("https://restcountries.com/v3.1/all")

        if not response.status_code == 200:
            raise Exception("Request has failed")
        else:
            return response.json()

    @classmethod
    def save_countries(cls):
        parsed_response = cls.fetch_country_data()
        i=0
        while i < 10:
            random_country = random.choice(parsed_response)
            query = f"""INSERT INTO countries(name, capital, flag, subregion, population)
                    VALUES ('{random_country['name']['official']}', '{random_country['capital'][0]}', '{random_country['flag']}', '{random_country['subregion']}', {random_country['population']})"""

            cls.run_query(query)
            i+=1


    @staticmethod
    def run_query(query):
        conn = psycopg2.connect(host=config.HOSTNAME, user=config.USERNAME, dbname=config.DATABASE)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        cursor.close
          
          
Countries.save_countries()



