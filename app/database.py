def save_ioc(mongo, data):
    collection = mongo.db.iocs
    collection.insert_one(data)

def get_recent_iocs(mongo, limit=20):
    return list(mongo.db.iocs.find().sort("date", -1).limit(limit))
