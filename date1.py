from flask import Flask, request, jsonify
import pymysql

# 调用数据库
conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='krcusz26wrh',
    db='date'
)
cursor = conn.cursor()

app = Flask(__name__)


# 提交数据函数
@app.route("/add", methods=["POST"])
def my_post():
    sql = "insert into todolist(title,body,state,intime,outtime) values(%s,%s,%s,%s,%s)"
    my_json = request.get_json()
    get_title = my_json.get("title")
    get_body = my_json.get("body")
    get_state = my_json.get("state")
    get_intime = my_json.get("intime")
    get_outtime = my_json.get("outtime")
    print(get_title, get_body, get_state, get_intime, get_outtime)
    try:
        cursor.execute(sql, (get_title, get_body, get_state, get_intime, get_outtime))
        conn.commit()
        return jsonify(date="录入成功", code="200", msg="success")
    except Exception as e:
        print(e)
        return jsonify(code="404", msg="该活动不存在")


# 获取所有数据函数
@app.route("/get", methods=["GET"])
def my_get():
    try:
        cursor.execute("select * from todolist")
        data = cursor.fetchall()
        return jsonify(code="200", msg="success", date=data)
    except Exception as e:
        print(e)
        return jsonify(code="404", msg="该活动不存在", )


# 获取单条数据函数
@app.route("/get/id", methods=["GET"])
def my_get_id():
    try:
        sql = "select * from todolist where id = %s"
        my_json = request.get_json()
        get_id = my_json.get("id")
        value = get_id
        cursor.execute(sql, value)
        data = cursor.fetchall()
        return jsonify(code="200", msg="success", date=data)
    except Exception as e:
        print(e)
        return jsonify(code="404", msg="该活动不存在", )


# 修改数据函数
@app.route("/put", methods=["PUT"])
def my_put():
    my_json = request.get_json()
    get_id = my_json.get("id")
    get_state = my_json.get("state")
    sql = "update todolist set state = %s  where id =%s "
    value = (get_state, get_id)
    try:
        cursor.execute(sql, value)
        conn.commit()
        return jsonify(code="200", msg="success")
    except Exception as e:
        print(e)
        return jsonify(code="404", msg="该活动不存在")


# 删除所有数据函数
@app.route("/delete/all", methods=["DELETE"])
def my_delete_all():
    sql = "delete from todolist "
    try:
        cursor.execute(sql)
        conn.commit()
        return jsonify(code="200", msg="success")
    except Exception as e:
        print(e)
        return jsonify(code="404", msg="该活动不存在")


# 删除单条数据函数
@app.route("/delete", methods=["DELETE"])
def my_delete():
    sql = "delete from todolist where id = %s "
    my_json = request.get_json()
    get_id = my_json.get("id")
    value = get_id
    try:
        cursor.execute(sql, value)
        conn.commit()
        return jsonify(code="200", msg="success")
    except Exception as e:
        print(e)
        return jsonify(code="404", msg="该活动不存在")


app.run()
