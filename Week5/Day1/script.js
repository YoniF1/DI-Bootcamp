let name2;
name2 = 5

let str2= ''
let freeting = 'hello'
let name3 = 'Nadav'
let greeting ='Yoni'
let fullGreeting = greeting + name3

console.log(greeting, name3)

let longStr="lirjgpoirjgoierjgoerilong \
jsrgkrejgerkjgerkgjerk \
ioffoijriofjeo";

console.log(longStr.length)
    console.log(longStr.indexOf('long'))
console.log(longStr.substring(longStr.indexOf('long'), 25))
let small = longStr.toLowerCase()
let big = longStr.toUpperCase()

//================================================

let num2=15
console.log(typeof(num2));
console.log(num2.toString())
let frac = 3.145
console.log(frac.toFixed(2))

//================================================

let bool2 = true
let checkBool = Boolean(bool2)
console.log(checkBool)


// alert("hello")

// let conf = confirm('are you feeling ok')
// let prop = prompt('and what is your name')
// console.log(prop);

let colors = ['blue', 'pink', 'red']
some = colors.pop()
console.log(some)

let car = {
    owner: 'yoni',
    year: 2016,
    model: 'ford focus'
}

console.log(car['year'])
car['color'] = 'red'
car.furniture = 'table'
console.log(car)

if (car.year > 2015) {
    console.log('that\'s a new car')
} else {
    console.log('not a new car')
}


switch(car.owner) {
    case 'fred':
        console.log(`fred's car`)
    case 'nadav':
        console.log(`nadav's car`)
    case 'yoni':
        console.log(`yoni's car`)
        break
    default :
        console.log('this is the default')
}