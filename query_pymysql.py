import pymysql
from app import app
import pymysql.cursors
from flask import jsonify

@app.route('/users/<uri>')
def users(uri):

        con = pymysql.connect(host='localhost',
        user='root',
        password='root',
        db='emp',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

        with con:

            cur = con.cursor()
            cur.execute("SELECT * FROM log_share_details WHERE uri='%s'"% uri)

            rows = cur.fetchall()

            for row in rows:
                print(row["id"],row["share_with_org"],row["share_with_domain"],row["share_with_app"],row["uid"],row["share_date"],row["filename"],row["doc_type"],row["source"],row["mimetype"],row["url"],row["aadhaarNumber"],row["shared_by"],row["shared_by_dob"],row["fileid"],row["org_id"],row["mobileno"],row["uri"], row["transaction_no"])
            resp = jsonify(rows)

            return resp


@app.route('/user/<transaction_no>')
def user(transaction_no):

        con = pymysql.connect(host='localhost',
        user='root',
        password='root',
        db='emp',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

        with con:

            cur = con.cursor()
            cur.execute("SELECT * FROM log_share_details WHERE transaction_no='%s'"% transaction_no)

            rows = cur.fetchall()

            for row in rows:
                print(row["id"],row["share_with_org"],row["share_with_domain"],row["share_with_app"],row["uid"],row["share_date"],row["filename"],row["doc_type"],row["source"],row["mimetype"],row["url"],row["aadhaarNumber"],row["shared_by"],row["shared_by_dob"],row["fileid"],row["org_id"],row["mobileno"],row["uri"], row["transaction_no"])
            resp = jsonify(rows)

            return resp


@app.route('/admin/<uri>/<transaction_no>')
def admin(uri,transaction_no):
    con = pymysql.connect(host='localhost',
                          user='root',
                          password='root',
                          db='emp',
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM log_share_details WHERE uri='{0}' and transaction_no='{1}'".format(uri, transaction_no))

        rows = cur.fetchall()

        for row in rows:
            print(row["id"], row["share_with_org"], row["share_with_domain"], row["share_with_app"], row["uid"],
                  row["share_date"], row["filename"], row["doc_type"], row["source"], row["mimetype"], row["url"],
                  row["aadhaarNumber"], row["shared_by"], row["shared_by_dob"], row["fileid"], row["org_id"],
                  row["mobileno"], row["uri"], row["transaction_no"])
        resp = jsonify(rows)

        return resp


if __name__ == "__main__":
    app.run(debug=True)