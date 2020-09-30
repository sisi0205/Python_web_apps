# MongoDB

[ebook](https://mongodb.tecladocode.com/)

## [Fixing /data/db not found error in MacOS X when starting MongoDB](https://medium.com/@bryantjiminson/fixing-data-db-not-found-error-in-macos-x-when-starting-mongodb-d7b82abb2479)



1. ***cd\*** to go to your personal home directory
2. ***mkdir MongoData\*** to create a directory store your Mongo database data. You can name it to anything else.
3. You need to make this directory owned by an user id. To do that, execute ***sudo chown -R `id -un` MongoData\*** (or your directory name)
4. ***cd MongoData\*** (or your directory name) to go inside the directory
5. Lastly, type **pwd** to get the current path. Copy the path.
6. `mongod --dbpath YOUR_NEW_MONGODATA_DIRECTORY`
7. You can get the content by using **cat** (e.g. **cat /usr/local/etc/mongod.conf**) for edit the command using some text editor like **nano** or **VIM**. The content looks like

## basics



`mongod --dbpath=/Users/sisi/MongoData`

`mongo` in another terminal 



```bash
show dbs
use fullstack
show collections
db.students.insert({"name": "Jose", "mark":99})
db.students.find({})
## two elements don't need be in the same structure
db.students.insert({"item": "chair", "price":999, "age":25})
db.students.remove({"item":"chair"})
systems.indexes

```









