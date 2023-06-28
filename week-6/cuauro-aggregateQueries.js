/**
	Title: cuauro-aggregateQueries.js
    Author: Patrick Cuauro
    Date: June 27th 2023
    Description: MongoDB Shell Scripts for the houses and students collections and aggregation queries.
 */
// Operations
// query to show a list of houses
db.houses.find()

// query to show a list of students
db.students.find()

// query to insert a new document using the example schema
db.students.insertOne({firstName:"Patrick",lastName:"Cuauro",studentId:"v9999",houseId:"m9999"})

// query to delete the previously created document
db.students.deleteOne({lastName:"Cuauro"})

// query to show a list of students for house Gryffindor using $lookup and $match
db.houses.aggregate(
    [
        { $lookup:
            { from: "students", localField: "houseId", foreignField: "houseId", as:"gryffindorMembers" }
        },
        { $match:
            {"gryffindorMembers.houseId":"h1007" }
            // used the Gryffindor housed id as filter
        }
    ])

// query to show a list of students for the Eagle mascot using $lookup and $match
db.houses.aggregate(
    [
        { $lookup:
            { from: "students", localField: "houseId", foreignField: "houseId", as:"eagleMembers" }
        },
        { $match:
            {"mascot":"Eagle" }
        }
    ])