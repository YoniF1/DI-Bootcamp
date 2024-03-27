function insertRow () {
    let table = document.getElementById('sampleTable')
    let row = document.createElement('tr')
    let i = 0
    let row_counter = 3
    let cell_counter = 1
    for (i=0; i<3; i++) {
        let row_data = document.createElement('td')
        let row_text = document.createTextNode(`Row${row_counter} cell${cell_counter}`)

        row_data.appendChild(row_text)

        row.appendChild(row_data)
        i+=1
        cell_counter += 1
    }
    row_counter += 1

    table.appendChild(row)
}