from pymongo import MongoClient

# 连接到MongoDB，假设MongoDB在本地运行，端口是默认的27017
client = MongoClient('localhost', 27017)

# 选择或创建一个数据库，这里的数据库名为"mydatabase"
db = client['mydatabase']

# 选择或创建一个集合（类似于SQL中的表），这里的集合名为"mycollection"
collection = db['mycollection']

# 插入一个文档（记录）
insert_result = collection.insert_one({'name': 'Alice', 'age': 30})
print(f'Inserted document id: {insert_result.inserted_id}')

# 查询集合中的所有文档
print('All documents:')
for doc in collection.find():
    print(doc)

# 更新文档，将名为Alice的文档的年龄改为31
update_result = collection.update_one({'name': 'Alice'}, {'$set': {'age': 31}})
print(f'Modified document count: {update_result.modified_count}')

# 删除一个文档，删除名为Alice的文档
# delete_result = collection.delete_one({'name': 'Alice'})
# print(f'Deleted document count: {delete_result.deleted_count}')

# 关闭与数据库的连接
client.close()
