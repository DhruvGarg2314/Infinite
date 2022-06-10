from hashlib import sha256
from MySQLdb.cursors import DictCursor
import MySQLdb as mysqllib
MYSQL_DATABASE_NAME = "CustomerData2"
MYSQL_TABLE_NAME = "CustomerData2.dbo"
MYSQL_HOST = "localhost"
MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "dhruv2314"
MYSQL_PORT = "3306"

MAX_NONCE=30000000
##Edit file

def SHA256(data):
    return sha256(data.encode('utf-8')).hexdigest()

#define mining function
def mine(block_number,transaction,previous_hash,prefix_zeroes):
    prefix_str='0'*prefix_zeroes #gives number of zeroes

    for nonce in range(MAX_NONCE):
        new_hash=SHA256(str(block_number)+str(transaction)+str(previous_hash)+str(nonce))

        if new_hash.startswith(prefix_str):
            print('The bock is mined with hash key {} and nonce value is {}'.format(new_hash,nonce))
            return new_hash
        #return None,None #any hash doesnot satisfy the condition

if __name__=="__main__":
    conn = mysqllib.connect(host = MYSQL_HOST, user = MYSQL_USERNAME, password = MYSQL_PASSWORD, db = MYSQL_DATABASE_NAME, cursorclass=DictCursor)
    #logger.info("Connection created")
    cursor = conn.cursor()
    #logger.info("Cursor created")
    cursor.execute("SELECT * from CustomerData2.dbo where CustID>2")
    #logger.info("Query executed")
    results = cursor.fetchall()
    print(results)
    transaction=results
    condition_zeroes=5
    import time
    start=time.time()
    print("start mining")
    new_hash=mine(2,transaction,'0000000000000000',condition_zeroes)
    print(new_hash)
    print("the time taken is {}".format(time.time()-start))

