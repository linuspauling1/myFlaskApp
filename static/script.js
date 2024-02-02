var label_title = document.querySelector('label[for="data_title"]')
var label_content = document.querySelector('label[for="data_content"]')

var input_title = document.getElementById('data_title')
input_title.addEventListener('focus',() => {
    label_title.style.visibility = 'visible'
    input_title.placeholder = ''
})
input_title.addEventListener('blur',() => {
    label_title.style.visibility = 'hidden'
    input_title.placeholder = 'Title'
})

var input_content = document.getElementById('data_text')
input_content.addEventListener('focus',() => {
    label_content.style.visibility = 'visible'
    input_content.placeholder = ''
})
input_content.addEventListener('blur',() => {
    label_content.style.visibility = 'hidden'
    input_content.placeholder = 'Text'
})