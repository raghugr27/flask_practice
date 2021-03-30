from flask import Flask, request, jsonify
from utils import db_connection

app = Flask(__name__)
conn, cursor = db_connection()
dic = {}


# @app.route("/hello")
# def hello_world():
#     return "hello world!!"


# @app.route("/")
# def home():
#     conn, cursor = db_connection()
#     if conn:
#         return "success"
#     return "not success"


@app.route("/login", methods=['POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        cursor.execute("SELECT email from details")
        user_email = cursor.fetchall()
        for email in user_email:
            if data["email"] in email:
                return "email already exists"
        cursor.execute("INSERT INTO Details (first_name,last_name,email,password)VALUES (%s, %s,%s,%s)",
                       (data['first_name'], data['last_name'], data['email'], data['password']))
        conn.commit()
        if conn:
            return jsonify(data)
    return "connection not established"


@app.route("/user_details/<int:uid>", methods=["GET", "DELETE"])
def user_details(uid):
    global dic
    if request.method == "GET":
        cursor.execute(f"select * from details where uid={uid}")
        user_info = cursor.fetchall()
        for row in user_info:
            tuple_to_dict = dict(row)
            dic = {str(i): str(j) for i, j in tuple_to_dict.items()}
        return dic

    if request.method == "DELETE":
        cursor.execute(f"DELETE FROM details where uid={uid}")
        conn.commit()
        return "deleted"


@app.route("/update_details/<uid>/<last_name>", methods=["PATCH"])
def update_user(uid, last_name):
    if request.method == "PATCH":
        inst = "UPDATE details SET  last_name = %s where uid = %s"
        data = (last_name, uid)
        cursor.execute(inst, data)
        conn.commit()
        # updated_user = cursor.fetchall()
        # print(updated_user)
        return "updated"


if __name__ == "__main__":
    app.run(debug=True)
