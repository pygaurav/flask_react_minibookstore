from app import app
from flask import jsonify,request
from app.db.book_model import BookModel

@app.route('/',methods=['GET'])
def index():
    return '<h1>Loaded</h1>'

@app.route('/api/fetch_book_slot/<int:value>',methods=['GET'])
def get_n_records(value):
    finalarr = BookModel.get_slot_books(value)
    if not finalarr is None:
        return jsonify({"results":finalarr})
    return jsonify({"Error":"Some Error occured at backend"}),400

@app.route('/api/fetch_books', methods=['GET'])
def get_books():
    finalarr = BookModel.get_all_books()
    if not finalarr is None:
        return jsonify({"results":finalarr})
    return jsonify({"Error":"Some Error occured at backend"}),400


@app.route('/api/fetch_book/<int:id>', methods=['GET'])
def get_book_by_id(id):
    finalarr = BookModel.get_book_by_id(id)
    if finalarr:
        return jsonify({"results":finalarr})
    return jsonify({"Error":"Some Error occured at backend"}),400


@app.route('/api/add_book', methods=['POST'])
def add_book():
    dict_book = request.get_json()
    deftupleval = (dict_book.get('book_name'),
    dict_book.get('book_author'),
    dict_book.get('book_price'),
    dict_book.get('book_url'),
    dict_book.get('book_image')
    )
    val = BookModel.insert_book(deftupleval)
    if val:
        return jsonify({"success":"Record successfully inserted"})
    return jsonify({"Error":"Some Error occured at backend"}),400



@app.route('/api/remove_books', methods=['DELETE'])
def delete_book_all():
    val = BookModel.delete_books()
    if val:
        return jsonify({"success":"All Records successfully deleted"})
    return jsonify({"Error":"Some Error occured at backend"}),400


@app.route('/api/remove_book/<int:id>', methods=['DELETE'])
def delete_book(id):
    val = BookModel.delete_book_by_id(id)
    if val:
        return jsonify({"success":"Record successfully deleted"})
    return jsonify({"Error":"Some Error occured at backend"}),400


@app.route('/api/update_book/<int:id>', methods=['PUT'])
def update_books(id):
    dict_book = request.get_json()
    deftupleval = (dict_book.get('book_name'),
    dict_book.get('book_author'),
    dict_book.get('book_price'),
    dict_book.get('book_url'),
    dict_book.get('book_image'),
    id
    )
    val = BookModel.update_book(deftupleval)
    if val:
        return jsonify({"success":"Record successfully updated"})
    return jsonify({"Error":"Some Error occured at backend"}),400
