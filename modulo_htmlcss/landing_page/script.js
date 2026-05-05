const button = document.querySelector('.btn-menu');
const menu = document.querySelector('.ul-nav');

button.addEventListener('click', ()=>{
    menu.classList.toggle('show');
});

const buttons = document.querySelectorAll('.btn')
buttons.forEach((button) => {
    button.addEventListener('click', ()=>{
        alert('Your ticket has been reserved')
    })
})
// button.addEventListener('click',)
    // alert('Your ticket has been reserved'
