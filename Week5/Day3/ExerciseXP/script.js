// Exercise1

// function displayNumbersDivisible(divisor) {
//     let sum = 0
//     for(i=0; i < 500; i++) {
//         if(i % divisor == 0) {
//             console.log(i)
//             sum += i
//         }
//     }

//     console.log(`Sum is: ${sum}`)
// }

// displayNumbersDivisible(3)
// displayNumbersDivisible(45)


// Exercise2

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// shoppingList = ["banana", "orange", 'apple']

// function myBill () {
//     for(i=0; i < shoppingList.length; i++) {
//         fruit = shoppingList[i]
//         if(stock[fruit] > 0) {
//             console.log(`The price of a ${fruit} is $${prices[fruit]}`)
//             stock[fruit] -= 1
//         }
//     }
// }

// myBill()

// Exercise3

// const mapPrice = {
//     0: 0.25,
//     1: 0.1,
//     2: 0.05,
//     3: 0.01
// }

// function changeEnough(itemPrice, amountOfChange) {
//     let totalValue = 0
//     const mapPrice = {
//         0: 0.25,
//         1: 0.1,
//         2: 0.05,
//         3: 0.01
//     }

//     for(i=0; i < amountOfChange.length; i++) {
//         totalValue += amountOfChange[i] * mapPrice[i]
//     }

//     if(totalValue > itemPrice) {
//         return true
//     }

//     return false
    

// }

// console.log(changeEnough(4.25, [25, 20, 5, 0]))
// console.log(changeEnough(14.11, [2, 100, 0, 0]))
// console.log(changeEnough(0.75, [0,0,20,5]))


// Exercise4

// function hotelCost () {
//     let answer;
//     while(isNaN(answer)) {
//         answer = prompt("How many nights would you like to stay?")
//     }

//     let price = 140 * answer
//     return price
// }

// function planeRideCost() {
//     let answer;

//     const mapDestination = {
//         "London": 183,
//         "Paris": 220
//     }

//     while(typeof(answer) != String) {
//         answer = prompt("What is your destination?")

//         if (mapDestination[answer]) {
//             return mapDestination[answer]
//         }
//         return 300
//     }

// }

// function rentalCarCost() {
//     let answer;
//     let cost = 0;

//     while(isNaN(answer)) {
//         answer = prompt("How many days would you like to rent the car?")
        
//         if (answer > 10) {
//             cost += 38 * answer
//         } else {
//             cost += 40 * answer
//         }
//     }

//     return cost
// }

// function totalVacationCost() {
//     hCost = hotelCost()
//     pCost = planeRideCost()
//     rCost = rentalCarCost()

//     return (hCost + pCost + rCost)
// }

// console.log(totalVacationCost)

// Exercise 5
// see ex5.js

// Exercise6
// see ex6.js


// Exercise7
// let book1 = {
//     title: 'Harry Potter',
//     author: 'J.K Rowling',
//     image: 'url1',
//     alreadyRead: true
// }

// let book2 = {
//     title: 'Lord of the Rings',
//     author: 'J.R.R Tolkien',
//     image: 'url2',
//     alreadyRead: false
// }

// let allBooks = [book1, book2]

// let section = document.getElementsByTagName('section')[0]
// for(let i of allBooks) {
//     let div = document.createElement('div')
//     let p = document.createElement('p')
//     let content = document.createTextNode(i['title'])
//     p.appendChild(content)
//     div.appendChild(p)

//     let p2 = document.createElement('p')
//     content = document.createTextNode(i['author'])
//     p2.appendChild(content)
//     div.appendChild(p2)

//     let image = document.createElement('img')
//     image.setAttribute('src', i['image'])
//     image.style.width = '100px'

//     section.appendChild(div)
//     section.appendChild(image)

//     if(i['alreadyRead'] == true) {
//         div.style.color = 'red'
//     }
// }

