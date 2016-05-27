import sqlite3

database_name ="firsty"
item_column = "Item"
count_column = "Count"
price_column = "PPI"
item_to_add = "Apple Sauce"
count_to_add = 1
price = 7.98

conn = sqlite3.connect("Z:/Projects/Python/testr")
print "Opened database successfully"
cursor = conn.cursor()
c = cursor


def add_item(item, amount, cost=0.00):
    try:
        conn.execute("""INSERT INTO {dbn} ({item_c}, {count_c}, {cost_c})
                VALUES (?, ?, ?)""".format(dbn=database_name, item_c=item_column, count_c=count_column,
                                           cost_c=price_column), (item, amount, cost))
        print str(c.rowcount) + " Row(s) added"
        conn.commit()
    except sqlite3.IntegrityError:
        print('ERROR: ID already exists in PRIMARY KEY column {}'.format(item_column))


def item_list():
    c.execute("""SELECT {itm} from {dbn} ORDER BY {price} Asc""".format(itm=item_column, dbn=database_name,
                                                                    price=price_column))
    print c.fetchall()


def update_item_price(item, value):
    c.execute("UPDATE {dbn} SET {price} = ?  WHERE {itm} = ?".format(dbn=database_name, price=price_column,
                                                                     itm=item_column), (value, item))
    conn.commit()

def update_item_count(item, count):
    c.execute("UPDATE {dbn} SET {cnt} = ? Where {itm} = ?".format(dbn=database_name, cnt=count_column,
                                                                  itm=item_column), (count, item))
    conn.commit()

def update_item(item, new_item):
    try:
        c.execute("UPDATE {dbn} SET {itm} = ? Where {itm2} = ?".format(dbn=database_name, itm=item_column,
                                                                       itm2=item_column), (new_item, item))
        conn.commit()
    except sqlite3.IntegrityError:
        print "Error: Item name already exists"

def delete_item(item):
    c.execute("DELETE FROM {dbn} where {itm} = ?".format(dbn=database_name, itm=item_column), (item, ))
    print str(c.rowcount) + " Row affected"
    conn.commit()


f = item_list()
j = add_item(item_to_add, count_to_add, price)
f = item_list()
#u = update_item_price("Milk", 5.56)
#uc = update_item_count("Spaghetti", 3)
#ui = update_item("Bread", "Bread")
# = delete_item("Spaghetti")
conn.close()
