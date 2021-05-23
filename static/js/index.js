
function activate(id) {
    console.log(id)
    var name1 = document.getElementById('name1')
    var name2 = document.getElementById('name2')
    var name3 = document.getElementById('name3')

    if (id === 'name1') {
        if (name1.classList.contains('activated')) {
            name1.classList.remove('activated')
        }
        else {
            name1.classList.add('activated')
        }
        name2.classList.remove('activated')
        name3.classList.remove('activated')
    }
    if (id === 'name2') {
        name1.classList.remove('activated')
        if (name2.classList.contains('activated')) {
            name2.classList.remove('activated')
        }
        else {
            name2.classList.add('activated')
        }
        name3.classList.remove('activated')
    }
    if (id === 'name3') {
        name1.classList.remove('activated')
        name2.classList.remove('activated')
        if (name3.classList.contains('activated')) {
            name3.classList.remove('activated')
        }
        else {
            name3.classList.add('activated')
        }
    }
}