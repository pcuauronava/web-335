/**
	Title: users-patrick.js
    Author: Professor Krasso
	Modified by: Patrick Cuauro
    Date: 13 June 2023
    Description: MongoDB Shell Scripts for the users collection.
 */
/**
 * Create personal User documents. 
 */
cuauro = {
	"firstName": "Patrick",
	"lastName": "Cuauro",
	"employeeId": "9999",
	"email": "patrickcuauro@gmail.com",
	"dateCreated": new Date()
}

/**
 * Insert the newly created user documents.
 */
db.users.insertOne(cuauro)