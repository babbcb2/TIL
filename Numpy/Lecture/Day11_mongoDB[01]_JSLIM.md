robo 3T

- show dbs
- use db_name
- show collections
- db.collection_name.find()



입력)

insert into table values ( value, value )



db.collection_name.insertone( { key : value , key : value} )

db.collection_name.insertMany( [ {key : value , key : value} ,  key : value , key : value} ])





db.user.find( {condition}, { column list} ) .limit(5)



db.user.find() - select * from user

db.user.find( { } , {user_id : 1, -id : 0} ) - select user_id from user

​					 	|                  |

​					where            set

db.user.find( {gender : 'f' } , {})  - select * from user where xxxxx

db.user.find( {gender : 'f' , user_id : 'jslim'} , {}) -  select * from user where user_id = xxx and gender

db.user.find( {$or : [ {gender : 'f'}, {user_id : 'jslim'}]} , {}) -  select * from user where user_id = xxx or gender



$or

$eq	=

$gt	>

$gte	>=

$in

$lt

$lte

$ne



수정)

update table

set		column = value

where  condition ;

db.collection_name.updateone( {where}, {set} )

db.collection_name.updateMany( {where}, {set} )



ex)

db.user.updateOne( { user_id : 'jslim' }, { $set : {gender : 'f'} } )

-> 

update user

set		gender = 'f'

where  user_id : 'jslim' ;



삭제)

delete 	from table

where 	condition ;



db.collection_name.removeeone( {where}, {set} )

db.collection_name.removeMany( {where}, {set} )