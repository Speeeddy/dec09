from flask import Flask, jsonify, request

app = Flask(__name__)

data = [
    dict(id=1, name='guido', gender='male', age=3)
]


@app.route('/users/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    for user in data:
        if user['id'] == uid:
            data.remove(user)
            return jsonify(dict(status='success'))

    return jsonify(dict(status='failed')), 403


@app.route('/users', methods=['POST'])
def add_users():
    new_user_id = data[-1]['id'] + 1
    new_user = dict(id=new_user_id)
    new_user.update(request.json)
    data.append(new_user)
    return jsonify(new_user)


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(dict(users=data))


if __name__ == '__main__':
    app.run(debug=True, port=7878)
