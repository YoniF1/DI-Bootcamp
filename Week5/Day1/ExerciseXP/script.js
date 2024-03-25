//Exercise1

// const people = ["Greg", "Mary", "Devon", "James"];

// index = people.indexOf("Greg")
// people.splice(index, 1)

// index = people.indexOf('James')
// new_value = 'Jason'
// people[index] = new_value

// people.push('Yoni')
// console.log(people)

// index = people.indexOf('Mary')
// console.log(index)

// new_people = people.slice(1,3)
// console.log(new_people)

// people.indexOf('Foo')
// // it gives -1 because it's not in the array

// last = people[people.length - 1]
// console.log(last)


// for (i=0; i < people.length; i++) {
//     console.log(people[i])
// }

// // OR

// for (let person of people) {
//     console.log(person)
// }

// for (i=0; i < people.length; i++) {
//     if(people[i] == 'Devon') {
//         break;
//     }
//     console.log(people[i]);
// };

// Exercise2

// colors = ['blue', 'red', 'purple', 'black', 'white']

// for (let color of colors) {
//     console.log(color)
// }

// let j = 1
// for (let color of colors) {
//     console.log("My #" + j + " choice is " + color)
//     j++
// }

// suffix = ['', 'st', 'nd', 'rd', 'th', 'th']

// let k = 1
// for (let color of colors) {
//     console.log("My " + k + suffix[k] + " choice is " + color)
//     k++
// }

// input = prompt('Give me a number')
// console.log(typeof(input))

// number = 0
// while(number < 10) {
//     number = prompt('Give me a number again')
//     console.log(number)
// }


// Exercise4

// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }

// console.log(building.numberOfFloors)
// console.log(building.numberOfAptByFloor.firstFloor)
// console.log(building.numberOfAptByFloor.thirdFloor)
// console.log("The name of the tenant is " + building.nameOfTenants[1] + " and he has " + building.numberOfRoomsAndRent.dan[0] + " rooms")

// sum_of_rent = (building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1])
// sum_of_dan = building.numberOfRoomsAndRent.dan[1]

// if (sum_of_dan < sum_of_rent) {
//     building.numberOfRoomsAndRent.dan[1] = 1200
// }
// console.log(building.numberOfRoomsAndRent.dan[1])

// Exercise 5

// family = {
//     someone: 'Joe',
//     someone1: 'Jake',
//     someone2: 'Josh'
// }

// for (let k in family) {
//     console.log(k)
// }

// for (let k in family) {
//     console.log(family[k])
// }


// Exercise 6

// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
//   }

// sentence = ''
// for (let key in details) {
//     sentence += key + ' ' + details[key] + ' '
// }
// console.log(sentence)


// Exercise 7

// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// let new_word = ''
// for (let word of names) {
//     new_word += word[0]
// }
// console.log(new_word.split("").sort().join(""))


