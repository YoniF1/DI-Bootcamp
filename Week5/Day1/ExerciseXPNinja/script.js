// #Exercise1

// let person1 = {
//     FullName: 'David Ben Gurion',
//     Mass: 80,
//     Height: 1.75,
//     BMI: function () {
//         return this.Mass / (this.Height * this.Height)
//     }
// }

// let person2 = {
//     FullName: 'Golda Meir',
//     Mass: 70,
//     Height: 1.55,
//     BMI: function () {
//         return this.Mass / (this.Height * this.Height)
//     }
// }

// let person3 = {
//     FullName: 'Menachem Begin',
//     Mass: 180,
//     Height: 1.65,
//     BMI: function () {
//         return this.Mass / (this.Height * this.Height)
//     }
// }

// function CompareBMI () {
//     let person_array = [person1, person2, person3]
//     let highest_BMI = person1

//     for (let p of person_array) {
//         if (highest_BMI.BMI() < p.BMI() ) {
//             highest_BMI = p
//         }
//     }
//     return highest_BMI.FullName;
// }

// console.log(CompareBMI())


// let user1 = {
//     name: 'Fred',
//     grades: [20, 45, 97, 58, 75]
// } 
// let user2 = {
//     name: 'Steve',
//     grades: [99, 95, 90, 75, 87]
// }

// function findAvg(gradesList) {
//     let total = 0
//     for (let grade of gradesList) {
//         total += grade
//     }
//     return total/gradesList.length
// }

// function tellUser() {
//     user_array = [user1, user2]
//     for (let user of user_array ) {
//         if (findAvg(user.grades) > 65 ) {
//             console.log(user.name + " you have passed" )
//         } else {
//             console.log(user.name + " you have failed")
//         }

//     }
// }

// tellUser()