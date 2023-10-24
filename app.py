from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# สร้างการเชื่อมต่อกับ MySQL
# db_connection = mysql.connector.connect(
#     host="your_host",
#     user="your_user",
#     password="your_password",
#     database="your_database"
# )

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="fbx-api",  # เปลี่ยนชื่อฐานข้อมูลเป็น "fbx-api"
    port=4306
)

# class PostForm:
#     def ConfirmPost(self, user_id, tag_friend_id, location_id, post_content):
#         cursor = db_connection.cursor()
#         insert_query = "INSERT INTO posts (User_ID, TagFriend_ID, Location_ID, Post_Content) VALUES (%s, %s, %s, %s)"
#         data = (user_id, tag_friend_id, location_id, post_content)
#         cursor.execute(insert_query, data)
#         db_connection.commit()
#         cursor.close()
#         return {"message": "Post created successfully"}

class PostForm:
    def ConfirmPost(self, user_id, tag_friend_ids, location_id, post_content):
        cursor = db_connection.cursor()
        insert_query = "INSERT INTO posts (User_ID, TagFriend_ID, Location_ID, Post_Content) VALUES (%s, %s, %s, %s)"
        
        # สร้างสร้างคู่ (User_ID, TagFriend_ID) สำหรับแต่ละเพื่อน
        data = [(user_id, tag_friend_id, location_id, post_content) for tag_friend_id in tag_friend_ids]
        
        cursor.executemany(insert_query, data)
        db_connection.commit()
        cursor.close()
        return {"message": "Post created successfully"}
    
class User:
    def GetUser(self, user_id):
        cursor = db_connection.cursor()
        select_query = "SELECT * FROM users WHERE User_ID = %s"
        cursor.execute(select_query, (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        if user_data:
            return user_data
        else:
            return {"message": "User not found"}, 404

class Location:
    def GetLocationInfo(self, location_id):
        cursor = db_connection.cursor()
        select_query = "SELECT * FROM locations WHERE Location_ID = %s"
        cursor.execute(select_query, (location_id,))
        location_data = cursor.fetchone()
        cursor.close()
        if location_data:
            return location_data
        else:
            return {"message": "Location not found"}, 404

class TagFriend:
    def getTagFriend(self, user_id):
        cursor = db_connection.cursor()
        select_query = "SELECT * FROM tag_friends WHERE User_ID = %s"
        cursor.execute(select_query, (user_id,))
        tag_friend_data = cursor.fetchall()
        cursor.close()
        if tag_friend_data:
            return tag_friend_data
        else:
            return {"message": "Tag friends not found"}, 404

# @app.route('/api/post', methods=['POST'])
# def create_post():
#     data = request.get_json()
#     user_id = data['user_id']
#     tag_friend_id = data['tag_friend_id']
#     location_id = data['location_id']
#     post_content = data['post_content']

#     post_form = PostForm()
#     response = post_form.ConfirmPost(user_id, tag_friend_id, location_id, post_content)
#     return jsonify(response), 201

@app.route('/api/post', methods=['POST'])
def create_post():
    data = request.get_json()
    user_id = data['user_id']
    tag_friend_ids = data.get('tag_friend_ids', [])  # รับรายการของ tag_friend_ids
    location_id = data['location_id']
    post_content = data['post_content']

    post_form = PostForm()
    response = post_form.ConfirmPost(user_id, tag_friend_ids, location_id, post_content)
    return jsonify(response), 201

@app.route('/', methods=['GET'])
def get_all_post():
    pass


@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User()
    response, status_code = user.GetUser(user_id)
    return jsonify(response), status_code

@app.route('/api/location/<int:location_id>', methods=['GET'])
def get_location(location_id):
    location = Location()
    response, status_code = location.GetLocationInfo(location_id)
    return jsonify(response), status_code

@app.route('/api/tagfriend/<int:user_id>', methods=['GET'])
def get_tagfriend(user_id):
    tagfriend = TagFriend()
    response, status_code = tagfriend.getTagFriend(user_id)
    return jsonify(response), status_code

if __name__ == "__main__":
    app.run()
