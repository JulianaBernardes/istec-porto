// alert('Olá mundo')
// console.log("Olá mundo");

// window.addEventListener('load', function(){
//     let products = document.getElementById('products');
//     console.log(products);
// })
 
// 4. SELECIONAR ELEMENTOS
//console.log(document.getElementsByTagName('form')[0])
//console.log(document.querySelector('form label:nth-child(2) input'));
// console.log(document.querySelectorAll('form input'));
// let inputs = document.querySelectorAll('form input')
// for (let i = 0; i< inputs.length; i++ ){
//     console.log(inputs[i]);
// }

// 5. EVENTOS

let form = document.getElementsByTagName('form')[0];

form.addEventListener('submit', function(event){
    let description = document.querySelector('form input[name=description]')
    let quantity = document.querySelector('form input[name=quantity]')
    //alert(description.value)
    let element = document.createElement('tr')
    element.innerHTML = 
        '<tr><td>' + description.value + '</td>' +
        '<td>' + quantity.value + '</td><td><input type="button" value="remove"></td></tr>'

    let elementUp = document.getElementById('products')
    elementUp.appendChild(element)

    let removeBtn = element.querySelector('input[type=button]')
    removeBtn.addEventListener('click', function(){
        removeBtn.parentNode.parentNode.remove()
        console.log(removeBtn);
    })
    event.preventDefault();
})

