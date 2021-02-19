from app import app
from flask_pymongo import PyMongo

@app.route('/')
def home():
   return "hello world! dsssssorld! dsssssss"
# db = mongo.db.Licenses
# @app.route('/danh-sach', methods=['GET'])
# def get_all():
#     data = []
#     i = 0
#     try:
#         for item in db.find({'IS_XOA': {'$ne': 1}}):
#             i = i + 1
#             data.append({'STT': i,
#                 'id': item['id'],
#                 'MA_LICENSE': item['MA_LICENSE'],
#                 'TIME_TAO_AT': item['TIME_TAO_AT'],
#                 'TIME_UPDATE_AT': item['TIME_UPDATE_AT'],
#                 'TIME_HET_HAN': '',
#                 'ID_KH': item['ID_KH'],
#                 'THANG_NAM': item['THANG_NAM'],
#                 'SO_THANG_NAM': item['SO_THANG_NAM'],
#                 'TRANG_THAI': item['TRANG_THAI'],
#                 'SO_LUONG_MAY_SU_DUNG': item['SO_LUONG_MAY_SU_DUNG'],
#             })
#     except Exception as e:
#         return jsonify({'data': [],'string_error':str(e)})
#     return jsonify({'data': data})


