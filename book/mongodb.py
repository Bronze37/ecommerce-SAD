from pymongo import MongoClient

client = MongoClient('mongodb+srv://ndinhdong1808:0pArqLiOkaRjOMWW@bronze.yy04j.mongodb.net/?retryWrites=true&w=majority&appName=Bronze')
db = client['product']
book_collection = db['book']