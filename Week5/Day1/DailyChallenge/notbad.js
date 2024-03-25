let sentence = 'This dinner is not that bad ! You cook well'
let sentence_array = sentence.split(" ")
let wordNot = sentence_array.indexOf('not')
let wordBad = sentence_array.indexOf('bad')
let new_sentence;

if (wordNot < wordBad) {
    sentence_array.splice(wordNot, (wordBad - wordNot) + 1, 'good')
    new_sentence = sentence_array.join(' ')
    console.log(new_sentence)
} else {
    console.log(sentence)
}
