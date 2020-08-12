from tools.shujuku_conn.oracle_conn import OracleOperation

db = OracleOperation()
DATA = db.execute_sql('SELECT comp_id,address FROM wuhan_rest')
data = db.get_data()
num = 0
for concent in data:
    comp_id = concent[0]