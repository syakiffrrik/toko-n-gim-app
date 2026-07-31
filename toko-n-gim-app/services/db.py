import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = ''
)

def insert_item(kode_menu, nama_menu, harga_menu, stok_menu):
    cursor = db.cursor()
    cursor.execute('INSERT INTO tbl_menu (kode_menu, nama_menu, harga_menu, stok_menu) VALUES (%s, %s, %s, %s)', (kode_menu, nama_menu, harga_menu, stok_menu))
    db.commit()
    
    if cursor.rowcount > 0:
        print('\nData berhasil diinsert\n')
    else:
        print('\nData gagal diinsert\n')


def fetch_item():
    cursor = db.cursor()
    cursor.execute('SELECT * FROM tbl_menu')
    return cursor.fetchall()
