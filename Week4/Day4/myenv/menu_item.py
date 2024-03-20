import psycopg2
import configxp

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        query = f"""INSERT INTO menu_items(item_name, item_price)
                    VALUES ('{self.name}', {self.price})"""
        
        self.run_query(query)
        return self

    def delete(self):
        query = f"DELETE FROM menu_items WHERE item_name = '{self.name}' AND item_price = {self.price}"

        self.run_query(query)
        return self

    def update(self, name, price):
        query = f"UPDATE menu_items SET item_name ='{name}', item_price ={price} WHERE item_name='{self.name}' AND item_price={self.price} "

        self.run_query(query)
        return self

    def run_query(self, query):
        conn = psycopg2.connect(host=configxp.HOSTNAME, user=configxp.USERNAME, dbname=configxp.DATABASE )
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()
        cursor.close

item = MenuItem('Burger', 35)
item2 = MenuItem('Beef Stew', 21)

item.save()
item.delete()

item2.save()
item2.delete()

item = MenuItem('Burger', 35)
item.save()
item.update('Veggie Burger1', 37)

item3 = MenuItem('Beef Stew', 21)
item3.save()




