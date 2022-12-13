from flask import Flask, jsonify, request, Response 
from database.db import initialize_db
from database.models import Photo, Album
import json
from bson.objectid import ObjectId
import os
import urllib
import base64
import codecs

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://mongo:27017/flask-database'   
}
db = initialize_db(app)


def str_list_to_objectid(str_list):
    return list(
        map(
            lambda str_item: ObjectId(str_item),
            str_list
        )
    )

def object_list_as_id_list(obj_list):
    return list(
        map(
            lambda obj: str(obj.id),
            obj_list
        )
    )


@app.route('/listPhoto', methods=['POST'])
def add_photo():
    posted_image = request.files['file']
    posted_data = request.form.to_dict()
    def_albums = Album.objects(name='Default')
    if def_albums: 
        pass
    else:
        def_albums.save()
    photo = Photo(name=posted_data['name'], location=posted_data['location'])
    photo.image_file.replace(posted_image)
    photo.save()
    output = {'message': "Photo successfully created", 'id': str(photo.id)}
    status_code = 201
    return output, status_code

@app.route('/listPhoto/<photo_id>', methods=['GET'])
def get_photo_by_id(photo_id):
    photo = Photo.objects.get(id=photo_id)
    if photo:
        
        base64_data = codecs.encode(photo.image_file.read(), 'base64')
        image = base64_data.decode('utf-8')
        return {'name': photo['name'], 'tags': photo['tags'], 'location': photo['location'], 'albums': object_list_as_id_list(photo['albums']), 'file': image }, 200

@app.route('/listPhoto/<photo_id>', methods=['PUT'])
def update_photo(photo_id):
    body = request.get_json()
    keys = body.keys()
    if body and keys:
        if "albums" in keys:
            body["albums"] = str_list_to_objectid(body["albums"])
        Photo.objects.get(id=photo_id).update(**body)
    return {'id': str(photo_id), 'message': "Photo successfully updated" }, 200

@app.route('/listPhoto/<photo_id>', methods=['DELETE'])
def delete_photo(photo_id):
    photo = Photo.objects.get_or_404(id=photo_id)
    photo.delete()
    return {'id' : str(photo_id), 'message': "Photo successfully deleted" }, 200

@app.route('/listPhotos', methods=['GET'])
def get_photos():
    tags = str(request.args.get('tags'))
    albumName = request.args.get('albumName')
    if albumName is not None:
        photo_objects = Photo.objects(albumName=album_id)
    elif tags is not None:
        photo_objects = Photo.objects(tags=tags)
    else:
        photo_objects = Photo.objects()
    photos = []
    for photo in photo_objects:
        base64_data = codecs.encode(photo.image_file.read(), 'base64')
        image = base64_data.decode('utf-8')
        photos.append({'name': photo['name'], 'location': photo['location'], 'file': image})
    return jsonify(photos), 200


@app.route('/listAlbum', methods=['POST']) 
def add_album():
    body = request.get_json()
    album = Album(**body).save()
    return {'id': str(album.id), 'message': "Album successfully created" }, 201

@app.route('/listAlbum/<album_id>', methods=['GET']) 
def get_album(album_id):
    album = Album.objects.get_or_404(id=album_id)
    return {'id': str(album.id), 'name': album['name']}, 200

@app.route('/listAlbum/<album_id>', methods=['PUT'])
def update_album(album_id):
    body = request.get_json()
    album = Album.objects.get_or_404(id=album_id)
    album.update(**body)
    return {'id': str(album.id), 'message': "Album successfully updated" }, 200


@app.route('/listAlbum/<album_id>', methods=['DELETE'])
def delete_album(album_id):
    album = Album.objects.get_or_404(id=album_id)
    album.delete()
    return {'id' : str(album.id), 'message': "Album successfully deleted" }, 200


if __name__ == '__main__':
    app.run()


