show dbs

use localmgdb

db

show dbs

db.mycollection.insertOne({name:1})

show dbs

show collections

db.createCollection('cappedCollection', {capped:true, size:10000})

db.cappedCollection.insertOne({x:1})

db.cappedCollection.find()
