from flask import jsonify, request
from flask_restful import Resource
from pymongo import MongoClient

from app_common import Timer, client, link_api_agent, link_api_mac, GetCapacity

database = client.ByteSave_Services
db = database["Services"]


class Service_Storage(Resource):
    def get(self,id):
        data = []
        i = 0
        try:
            if int(id) != 0:
                finter = db.find({'$and': [{'IS_XOA': {'$ne': 1}}, {'id': int(id)}]})
                count = finter.count()
                for item in finter:
                    i = i + 1
                    data.append({'STT': i,
                                 'id': item['id'],
                                 'TEN_DICH_VU': item['TEN_DICH_VU'],
                                 'MO_TA': item['MO_TA'],
                                 'TIME_TAO_AT': item['TIME_TAO_AT'],
                                 'TIME_UPDATE_AT': item['TIME_UPDATE_AT'],
                                 })
            else:
                finter = db.find({'IS_XOA': {'$ne': 1}})
                count = finter.count()
                for item in finter:
                    i = i + 1
                    data.append({'STT': i,
                                 'id': item['id'],
                                 'TEN_DICH_VU': item['TEN_DICH_VU'],
                                 'MO_TA': item['MO_TA'],
                                 'TIME_TAO_AT': item['TIME_TAO_AT'],
                                 'TIME_UPDATE_AT': item['TIME_UPDATE_AT'],
                                 })
        except Exception as e:
            return jsonify({'data': [], 'countdata': 0, 'string_error': str(e)})
        return jsonify({'data': data, 'countdata': count})

    def post(self):
        if request.method == 'POST':
            form = request.form
            idd = form.get('id_ser_sto', '')
            if idd != '' and idd != None:
                try:
                    db.update_one(
                        {"id": int(idd)},
                        {"$set": {
                            'TEN_DICH_VU': form.get('TEN_DICH_VU'),
                            'MO_TA': form.get('MO_TA'),
                            'TIME_UPDATE_AT': Timer.get_timestamp_now(),
                        }})
                except Exception as e:
                    return jsonify(
                        {'status': 'NOK', 'msg': 'Chỉnh sửa không thành công!', 'string_error': str(e)})
                return jsonify({'status': 'OK', 'msg': 'Chỉnh sửa thành công!'})
            try:
                idmax = db.find().sort([("id", -1)])[0]['id'] if db.find().count() > 0 else 0
                db.insert({
                    'id': idmax + 1,
                    'TEN_DICH_VU': form.get('TEN_DICH_VU'),
                    'MO_TA': form.get('MO_TA'),
                    'IS_XOA': 0,
                    'TIME_TAO_AT': Timer.get_timestamp_now(),
                    'TIME_UPDATE_AT': Timer.get_timestamp_now(),
                })
            except Exception as e:
                return jsonify(
                    {'status': 'NOK', 'msg': 'Thêm mới không thành công!', 'string_error': str(e)})
        return jsonify({'status': 'OK', 'msg': 'Thêm mới thành công!'})

class Del_Service_Storage(Resource):
    def post(self, id):
        try:
            if id != '':
                db.update_one(
                    {"id": int(id)},
                    {"$set": {"IS_XOA": 1,
                              'TIME_UPDATE_AT': Timer.get_timestamp_now(),
                              }})
        except Exception as e:
            return jsonify({'status': 'NOK', 'msg': 'Xóa không thành công!', 'string_error': str(e)})
        return jsonify({'status': 'OK', 'msg': 'Xóa thành công!'})

