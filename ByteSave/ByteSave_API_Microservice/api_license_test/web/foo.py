from flask import jsonify, request
from flask_restful import Resource
from pymongo import MongoClient

from app_common import Timer

client = MongoClient("mongodb://localhost:27017")
db = client.ByteSave_Licenses
users = db["Users"]
license = db["Licenses"]

class License3s3(Resource):
    def get(self):
        data = []
        i = 0
        try:
            for item in license.find({'IS_XOA': {'$ne': 1}}):
                i = i + 1
                data.append({'STT': i,
                             'id': item['id'],
                             'MA_LICENSE': item['MA_LICENSE'],
                             'TIME_TAO_AT': item['TIME_TAO_AT'],
                             'TIME_UPDATE_AT': item['TIME_UPDATE_AT'],
                             'TIME_HET_HAN': '',
                             'ID_KH': item['ID_KH'],
                             'THANG_NAM': item['THANG_NAM'],
                             'SO_THANG_NAM': item['SO_THANG_NAM'],
                             'TRANG_THAI': item['TRANG_THAI'],
                             'SO_LUONG_MAY_SU_DUNG': item['SO_LUONG_MAY_SU_DUNG'],
                             })
        except Exception as e:
            return jsonify({'data': [], 'string_error': str(e)})
        return jsonify({'data': data})
    def post(self):
        if request.method == 'POST':
            form = request.form
            idd = form.get('idlicense', '')
            if idd != '' and idd != None:
                try:
                    license.update_one(
                        {"id": idd},
                        {"$set": {"ID_KH": form.get('ID_KH', ''),
                                  "MA_LICENSE": form.get('MA_LICENSE', ''),
                                  "TIME_HET_HAN": form.get('TIME_HET_HAN', ''),
                                  "SO_THANG_NAM": form.get('SO_THANG_NAM', ''),
                                  "THANG_NAM": form.get('THANG_NAM', ''),
                                  "SO_LUONG_MAY_SU_DUNG": form.get('SO_LUONG_MAY_SU_DUNG', ''),
                                  }})
                except Exception as e:
                    return jsonify(
                        {'status': 'NOK', 'msg': 'Chỉnh sửa không thành công mã bản quyền', 'string_error': str(e)})
                return jsonify({'status': 'OK', 'msg': 'Chỉnh sửa thành công mã bản quyền'})
            try:
                idmax = license.find().sort([("id", -1)])[0]['id'] if license.find().count() > 0 else 0
                license.insert({
                    'id': idmax + 1,
                    'ID_KH': int(form.get('ID_KH')),
                    'MA_LICENSE': form.get('MA_LICENSE'),
                    # 'TIME_HET_HAN': form.get('TIME_HET_HAN'),
                    'SO_THANG_NAM': int(form.get('TIME_HET_HAN')),
                    'THANG_NAM': int(form.get('Choisenamthang')),
                    'SO_LUONG_MAY_SU_DUNG': int(form.get('SO_LUONG_MAY_SU_DUNG')),
                    'TIME_TAO_AT': Timer.get_timestamp_now(),
                    'TIME_UPDATE_AT': Timer.get_timestamp_now(),
                    'TRANG_THAI': 0,
                })
            except Exception as e:
                return jsonify(
                    {'status': 'NOK', 'msg': 'Thêm mới không thành công mã bản quyền', 'string_error': str(e)})
        return jsonify({'status': 'OK', 'msg': 'Thêm mới thành công mã bản quyền'})

class Foo(Resource):
    def get(self):
        pass
    def post(self):
        pass