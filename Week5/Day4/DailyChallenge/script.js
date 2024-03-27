const form = document.forms[0]

for(let element of form.elements) {
    element.required = true
}

let inputs = Array.from(form.elements).slice(0, 5)

const button = document.getElementsByTagName('button')[0]

button.addEventListener('click', e => {
    e.preventDefault()

    if(form.checkValidity()) {
        let story = document.getElementById('story')
        
        for(let i of inputs) {
            let content = document.createTextNode(i.value + ' ')
            story.appendChild(content)
        }

        let shuffleButton = document.createElement('button')
        let contentButton = document.createTextNode('Shuffle!')
        shuffleButton.appendChild(contentButton)
        story.appendChild(shuffleButton)

        shuffleButton.addEventListener('click', e => {
            e.preventDefault()
            inputs = inputs.sort(() => Math.random() - 0.5)
            story.innerHTML = ''

            for(let i of inputs) {
                content = document.createTextNode((i.value + ' '))
                story.appendChild(content)
                story.appendChild(shuffleButton)
            }

        } )
    } else {
        alert("Form is not valid, make sure you've filled every input field")
    }
})


