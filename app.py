from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fbx-api",  # เปลี่ยนชื่อฐานข้อมูลเป็น "fbx-api"
    port = 3307
)

class PostForm:
    def ConfirmPost(self, user_id, tag_friend_ids, location_id, post_content):
        cursor = db_connection.cursor()
        insert_post_query = "INSERT INTO post (User_ID, Location_ID, Post_Content) VALUES (%s, %s, %s)"
        cursor.execute(insert_post_query, (user_id, location_id, post_content))
        db_connection.commit()
        
        post_id = cursor.lastrowid  # Get the last inserted Post_ID
        
        cursor.close()

        # Insert the Post_ID into the tag_friends table
        cursor = db_connection.cursor()
        insert_post_tagged_query = "INSERT INTO tag_freinds (Post_ID, Friend_ID) VALUES (%s, %s)"
        for tag_friend_id in tag_friend_ids:
            cursor.execute(insert_post_tagged_query, (post_id, tag_friend_id))

        db_connection.commit()
        cursor.close()
        return post_id


class User:
    def Get_posts_by_user_id(self, user_id):
        cursor = db_connection.cursor()

        # Retrieve the user's own posts and tagged posts
        select_user_posts_query = """
            SELECT Post_ID, User_ID, Location_ID, Post_Content
            FROM post
            WHERE User_ID = %s
            UNION ALL
            SELECT p.Post_ID, p.User_ID, p.Location_ID, p.Post_Content
            FROM post p
            JOIN tag_freinds t ON p.Post_ID = t.Post_ID
            WHERE t.Friend_ID = %s
        """
        cursor.execute(select_user_posts_query, (user_id, user_id))
        all_posts = cursor.fetchall()

        cursor.close()

        # Sort the posts by Post_ID
        all_posts.sort(key=lambda post: post[0])

        keys = ["Post_ID", "User_ID", "Location_ID", "Post_Content"]
        posts_dict = [dict(zip(keys, post)) for post in all_posts]

        return posts_dict, 200  # Return response data and a status code

        


class Location:
    def Get_post_By_location_ID(self, location_id):
        cursor = db_connection.cursor()
        select_query = "SELECT Post_ID, User_ID, Location_ID, Post_Content FROM post WHERE Location_ID = %s"
        cursor.execute(select_query, (location_id,))
        location_data = cursor.fetchall()
        cursor.close()

        # Transform the list of tuples into a list of dictionaries
        keys = ["Post_ID", "User_ID", "Location_ID", "Post_Content"]
        location_data_dict = [dict(zip(keys, post)) for post in location_data]

        if location_data:
            return location_data_dict, 200  # Return response data and a status code
        else:
            return {"message": "No posts found for this location"}, 404




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
def home():
    return "Hello, world"



@app.route('/api/posts', methods=['GET'])
def get_all_posts():
    cursor = db_connection.cursor()
    select_query = "SELECT * FROM post"
    cursor.execute(select_query)
    posts = cursor.fetchall()
    cursor.close()
    
    if posts:
        # Transform the list of tuples into a list of dictionaries
        keys = ["Post_ID", "User_ID", "Location_ID", "Post_Content"]
        posts_dict = [dict(zip(keys, post)) for post in posts]
        
        return jsonify(posts_dict), 200
    else:
        return {"message": "No posts found"}, 404


@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User()
    response, status_code = user.Get_posts_by_user_id(user_id)
    return jsonify(response), status_code

@app.route('/api/location/<int:location_id>', methods=['GET'])
def get_posts_by_location_id(location_id):
    location = Location()
    response, status_code = location.Get_post_By_location_ID(location_id)
    return jsonify(response), status_code



if __name__ == "__main__":
    app.debug = True
    app.run()
