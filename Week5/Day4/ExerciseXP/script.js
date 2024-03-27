// Exercise1

// // Q1
// title = document.querySelector('h1')
// console.log(title)

// // Q2
// paragraphs = document.querySelectorAll('article > p')
// last_p = paragraphs[paragraphs.length - 1]
// last_p.remove()

// // Q3
// subtitle = document.querySelector('h2')
// subtitle.onclick = function () {
//     subtitle.style.backgroundColor = 'red'
// }

// // Q4
// subtitle1 = document.querySelector('h3')
// subtitle1.onclick = function () {
//     subtitle.style.display = 'none'
// }

// // Q5

// article = document.querySelector('article')
// button = document.createElement('button')
// content = document.createTextNode('A button')
// button.appendChild(content)
// article.appendChild(button)
// button.onclick = function () {
//     paragraphs = document.querySelectorAll('p')
//     for(let p of paragraphs) {
//         p.style.fontWeight = 'bold'
//     }
// }

// // Q6 - bonus
// title = document.querySelector('h1')
// title.addEventListener('mouseover', e => {
//     title.style.fontSize =`${(Math.random() * 100)}px`
// })

// // Q7 - bonus
// subtitle = document.querySelector('h2')
// subtitle.addEventListener('mouseover', e => {
//     subtitle.style.opacity = 0
//     subtitle.style.transition = '1s'
// })

// Exercise2

// const form = document.forms[0]
// console.log(form)

// let input = document.getElementById('fname')
// let input1 = document.getElementById('lname')
// console.log(input, input1)

// input = form.elements.firstname
// input1 = form.elements.lastname
// console.log(input, input1)

// form.addEventListener('submit', e => {
//     e.preventDefault()
//     firstName = input.value
//     lastName = input1.value
//     fnewLi = document.createElement('li')
//     lnewLi = document.createElement('li')

//     content = document.createTextNode(firstName)
//     content1 = document.createTextNode(lastName)

//     fnewLi.appendChild(content)
//     lnewLi.appendChild(content1)

//     list = document.getElementsByClassName('usersAnswer')[0]
//     list.appendChild(fnewLi)
//     list.appendChild(lnewLi)
// })

// Exercise3

// let allBoldItems;

// function getBoldItems(){
//     allBoldItems = document.getElementsByTagName('strong')
//     return allBoldItems
// }

// function highlight(e) {
//     e.target.style.color = 'blue'
// }

// function returnItemsToDefault(e) {
//     e.target.style.color = 'black'
// }

// allBoldItems = getBoldItems()
// for(let bold of allBoldItems) {
//     bold.addEventListener('mouseover', highlight)
//     bold.addEventListener('mouseout', returnItemsToDefault)
// }

// Exercise4
// see ex4.js

