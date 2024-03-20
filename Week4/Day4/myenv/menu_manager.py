import psycopg2
import configxp

from menu_item import MenuItem

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = f"SELECT * FROM menu_items WHERE item_name = '{name}'"
        result = cls.run_query(query)
        if result is []:
            return None
        else:
            return MenuItem(name, result[0][2])

    @classmethod
    def all(cls):
        query = f"SELECT * FROM menu_items"
        return cls.run_query(query)
    
    @staticmethod
    def run_query(query):
        conn = psycopg2.connect(host=configxp.HOSTNAME, user=configxp.USERNAME, password=configxp.PASSWORD, dbname=configxp.DATABASE )
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results

item5 = MenuManager.get_by_name('Beef Stew')
print(item5.name)
print(item5.price)