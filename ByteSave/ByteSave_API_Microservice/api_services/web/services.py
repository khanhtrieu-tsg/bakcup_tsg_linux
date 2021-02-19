from flask import jsonify, request
from flask_restful import Resource
from pymongo import MongoClient

from app_common import Timer, client, link_api_agent, link_api_mac, GetCapacity

database = client.ByteSave_Services
db = database["MetricsServices"]


class hello(Resource):
    def get(self):
        return 'hello khánh'


class Service(Resource):
    def get(self):
        data = []
        i = 0
        finter = db.find({'IS_XOA': {'$ne': 1}})
        count = finter.count()
        try:
            for item in finter:
                i = i + 1
                data.append({'STT': i,
                             'id': item['id'],
                             'GIOI_HAN_SU_DUNG': item['GIOI_HAN_SU_DUNG'],
                             'DA_SU_DUNG': '',
                             'THONG_TIN_KET_NOI': item['THONG_TIN_KET_NOI'],
                             'KH_TEN': 'cusname',
                             'TIME_TAO_AT': item['TIME_TAO_AT'],
                             'TIME_UPDATE_AT': item['TIME_TAO_AT'],
                             'IS_DICH_VU': item['IS_DICH_VU'],
                             'ID_KH': item['ID_KH'],
                             'TAI_KHOAN': item['TAI_KHOAN'],
                             'TRANG_THAI': item['TRANG_THAI'],
                             'LOADDING': '',
                             })
        except Exception as e:
            return jsonify({'data': [], 'countdata': 0, 'string_error': str(e)})
        return jsonify({'data': data, 'countdata': count})

    def post(self):
        if request.method == 'POST':
            form = request.form
            idd = form.get('id_ser')
            if idd != '' and idd != None:
                try:
                    db.update_one(
                        {"id": int(idd)},
                        {"$set": {"GIOI_HAN_SU_DUNG": int(form.get('GIOI_HAN_SU_DUNG', '')),
                                  "THONG_TIN_KET_NOI": form.get('THONG_TIN_KET_NOI', ''),
                                  "TAI_KHOAN": form.get('TAI_KHOAN', ''),
                                  "IS_DICH_VU": int(form.get('IS_DICH_VU', '')),
                                  "ID_KH": int(form.get('ID_KH', '')),
                                  "TIME_UPDATE_AT": Timer.get_timestamp_now(),
                                  }})
                except Exception as e:
                    return jsonify(
                        {'status': 'NOK', 'msg': 'Chỉnh sửa không thành công!', 'string_error': str(e)})
                return jsonify({'status': 'OK', 'msg': 'Chỉnh sửa thành công!'})
            try:
                idmax = db.find().sort([("id", -1)])[0]['id'] if db.find().count() > 0 else 0
                db.insert({
                    'id': idmax + 1,
                    'GIOI_HAN_SU_DUNG': int(form.get('GIOI_HAN_SU_DUNG')),
                    'THONG_TIN_KET_NOI': form.get('THONG_TIN_KET_NOI'),
                    'TAI_KHOAN': form.get('TAI_KHOAN'),
                    'ID_KH': int(form.get('ID_KH')),
                    'IS_DICH_VU': int(form.get('IS_DICH_VU')),
                    'TIME_TAO_AT': Timer.get_timestamp_now(),
                    'TIME_UPDATE_AT': Timer.get_timestamp_now(),
                    'DA_SU_DUNG': 0,
                    'TRANG_THAI': 0,
                    'IS_XOA': 0,
                })
            except Exception as e:
                return jsonify(
                    {'status': 'NOK', 'msg': 'Thêm mới không thành công!', 'string_error': str(e)})
        return jsonify({'status': 'OK', 'msg': 'Thêm mới thành công!'})

class Service_KH(Resource):
    def get(self,idkh):
        data = []
        i = 0
        finter = db.find({'$and': [{'IS_XOA': {'$ne': 1}}, {'ID_KH': int(idkh)}]})
        count = finter.count()
        try:
            for item in finter:
                i = i + 1
                data.append({'STT': i,
                             'id': item['id'],
                             'GIOI_HAN_SU_DUNG': item['GIOI_HAN_SU_DUNG'],
                             'DA_SU_DUNG': '',
                             'THONG_TIN_KET_NOI': item['THONG_TIN_KET_NOI'],
                             'KH_TEN': 'cusname',
                             'TIME_TAO_AT': item['TIME_TAO_AT'],
                             'TIME_UPDATE_AT': item['TIME_TAO_AT'],
                             'IS_DICH_VU': item['IS_DICH_VU'],
                             'ID_KH': item['ID_KH'],
                             'TAI_KHOAN': item['TAI_KHOAN'],
                             'TRANG_THAI': item['TRANG_THAI'],
                             'LOADDING': '',
                             })
        except Exception as e:
            return jsonify({'data': [], 'countdata': 0, 'string_error': str(e)})
        return jsonify({'data': data, 'countdata': count})
    def post(self,idkh):
        try:
            form = request.form
            for i in range(1, int(form.get('CountRowService')) + 1):
                try:
                    if form.get('IS_DICH_VU' + str(i)) != '' and form.get(
                            'THONG_TIN_KET_NOI' + str(i)) != None and db.find({'$and': [{'IS_XOA': {'$ne': 1}},{'ID_KH': int(idkh)}, {'TAI_KHOAN': form.get('TAI_KHOA' + str(i))}]}).count() == 0:
                        idmax = db.find().sort([("id", -1)])[0]['id'] if db.find().count() > 0 else 0
                        db.insert({
                            'id': idmax + 1,
                            'ID_KH': int(idkh),
                            'GIOI_HAN_SU_DUNG': int(form.get('GIOI_HAN_SU_DUNG' + str(i))),
                            'THONG_TIN_KET_NOI': form.get('THONG_TIN_KET_NOI' + str(i)),
                            'TAI_KHOAN': form.get('TAI_KHOAN' + str(i)),
                            'IS_DICH_VU': int(form.get('IS_DICH_VU' + str(i))),
                            'TIME_TAO_AT': Timer.get_timestamp_now(),
                            'TIME_UPDATE_AT': Timer.get_timestamp_now(),
                            'TRANG_THAI': 0,
                            'IS_XOA':0,
                            'DA_SU_DUNG':0,
                        })
                except Exception as e:
                    continue
        except Exception as e:
            return jsonify(
                {'status': 'NOK', 'msg': 'Thêm mới không thành công!', 'string_error': str(e)})
        return jsonify({'status': 'OK', 'msg': 'Thêm mới thành công!'})

class Load_DSD(Resource):
    def get(self, id):
        data = []
        i = 0
        acountServiceQuaHan = 0
        try:
            if int(id) != 0:
                finter = db.find({'$and': [{'IS_XOA': {'$ne': 1}}, {'ID_KH': int(id)}]})
                count = finter.count()
                for item in finter:
                    i = i + 1
                    size = GetCapacity(item['THONG_TIN_KET_NOI'])
                    formatted_float = "{:.2f}".format(size * 0.000000000931)

                    percen = "{:.2f}".format((int(size * 0.000000000931)/int(item['GIOI_HAN_SU_DUNG'])) * 100)
                    if item['DA_SU_DUNG']:
                        if int(item['DA_SU_DUNG']) > int(item['GIOI_HAN_SU_DUNG']):
                            acountServiceQuaHan += 1
                    data.append({'STT': i,
                                 'id': item['id'],
                                 'LOADDING': percen,
                                 'DA_SU_DUNG': formatted_float,
                                 'GIOI_HAN_SU_DUNG': item['GIOI_HAN_SU_DUNG'],
                                 })
            else:
                finter = db.find({'$and': [{'IS_XOA': {'$ne': 1}}]})
                count = finter.count()
                for item in finter:
                    i = i + 1
                    size = GetCapacity(item['THONG_TIN_KET_NOI'])
                    formatted_float = "{:.2f}".format(size * 0.000000000931)
                    percen = "{:.2f}".format((int(size * 0.000000000931) / int(item['GIOI_HAN_SU_DUNG'])) * 100)
                    if item['DA_SU_DUNG']:
                        if int(item['DA_SU_DUNG']) > int(item['GIOI_HAN_SU_DUNG']):
                            acountServiceQuaHan += 1
                    data.append({'STT': i,
                                 'id': item['id'],
                                 'LOADDING': percen,
                                 'DA_SU_DUNG': formatted_float,
                                 'GIOI_HAN_SU_DUNG': item['GIOI_HAN_SU_DUNG'],
                                 })
        except Exception as e:
            return jsonify({'status': 'NOK','data': [], 'countdata': 0, 'acountServiceQuaHan': 0, 'string_error': str(e)})
        return jsonify({'status': 'OK','data': data, 'countdata': count, 'acountServiceQuaHan': acountServiceQuaHan})



class Del_Service(Resource):
    def post(self,id):
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



