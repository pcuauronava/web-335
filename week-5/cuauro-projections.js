/**
	Title: cuauro-projections-create.js
    Author: Professor Krasso
    Date: 22 June 2023
    Description: MongoDB Shell Scripts.
 */
// declare the new composer to create
handel = {
    "firstName": "George",
    "lastName": "Handel",
    "employeeId": "1013",
    "email": "handel@me.com",
    "dateCreated": new Date()
}
// script for insert the newly created composer
db.users.insertOne(handel)

// script to show the information of Mozart composer before it gets modified
db.users.find({ lastName :"Mozart"});

// script for update the Mozart composer information
db.users.update({ lastName: "Mozart" }, { $set: { email: "mozart@me.com" } });

// script for showing the results after the modification
db.users.find({ lastName: "Mozart" });

// script for aggregate using $project and show all the documents in the collection showing only the desired fields
db.users.aggregate( { $project: { firstName:1, lastName:1, email:1, _id:0 } } );