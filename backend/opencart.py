import pymysql

# Fonction pour se connecter à la base de données OpenCart
def connect_to_opencart_db():
    connection = pymysql.connect(host='localhost',
                                 user='utilisateur_opencart',
                                 password='mot_de_passe',
                                 database='nom_de_la_base_de_donnees_opencart',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

# Fonction pour récupérer le nombre d'utilisateurs actuellement connectés
def get_active_users_count(connection):
    query = "SELECT COUNT(*) AS active_users FROM oc_customer_online"
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        return result['active_users']

# Fonction pour récupérer le nombre d'achats par produit pour chaque mois
def get_product_sales_per_month(connection):
    query = """
        SELECT DATE_FORMAT(date_added, '%Y-%m') AS month,
               product_id,
               COUNT(*) AS sales
        FROM oc_order_product
        GROUP BY month, product_id
        ORDER BY month
    """
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return result

# Fonction pour récupérer le nombre total de ventes
def get_total_sales(connection):
    query = "SELECT COUNT(*) AS total_sales FROM oc_order"
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        return result['total_sales']

# Fonction pour récupérer le nombre total d'utilisateurs ayant un compte
def get_total_users(connection):
    query = "SELECT COUNT(*) AS total_users FROM oc_customer"
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        return result['total_users']

# Fonction pour récupérer le nombre total de commandes faites actuellement
def get_current_orders_count(connection):
    query = "SELECT COUNT(*) AS current_orders FROM oc_order WHERE order_status_id != 0"
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
        return result['current_orders']

# Fonction principale pour récupérer toutes les données demandées
def get_opencart_statistics():
    connection = connect_to_opencart_db()
    active_users = get_active_users_count(connection)
    product_sales = get_product_sales_per_month(connection)
    total_sales = get_total_sales(connection)
    total_users = get_total_users(connection)
    current_orders = get_current_orders_count(connection)
    connection.close()

    return {
        'active_users': active_users,
        'product_sales_per_month': product_sales,
        'total_sales': total_sales,
        'total_users': total_users,
        'current_orders': current_orders
    }
