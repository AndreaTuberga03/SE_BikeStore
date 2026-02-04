from database.DB_connect import DBConnect
from model.category import Category
from model.product import Product

class DAO:
    @staticmethod
    def get_date_range():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT order_date
                    FROM `order` 
                    ORDER BY order_date """
        cursor.execute(query)

        for row in cursor:
            results.append(row["order_date"])

        first = results[0]
        last = results[-1]

        cursor.close()
        conn.close()
        return first, last

    @staticmethod
    def get_categories():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT DISTINCT category_id, category_name
                    FROM category c, product p
                    WHERE p.category_id = c.id"""
        cursor.execute(query)

        for row in cursor:
            result.append(Category(row["category_id"], row["category_name"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_prod(categ):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT id, product_name
                    FROM product p
                    WHERE category_id = %s"""
        cursor.execute(query, (categ,))

        for row in cursor:
            result.append(Product(row["id"], row["product_name"]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_weighted_neigh(categ, d1, d2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """ SELECT LEAST(n.state1, n.state2) AS st1,
                           GREATEST(n.state1, n.state2) AS st2, 
                           COUNT(*) as N
                    FROM product p, order_item oi, order o
                    WHERE p.id = oi.product_id AND oi.order_id = o.id
                    AND category_id = %s
                    AND order_date BETWEEN %s AND %s
                    GROUP BY p.id """

        cursor.execute(query, (categ, d1, d2))

        for row in cursor:
            result.append((row['st1'], row['st2'], row["N"]))

        cursor.close()
        conn.close()
        return result