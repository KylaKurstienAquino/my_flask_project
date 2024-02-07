const body = document.body;
const bookform = document.getElementById('bookform');

function openform() {
    bookform.style.display = 'flex';
    body.classList.add('modal-open');
}

function closeform() {
    bookform.style.display = 'none';
    body.classList.remove('modal-open');
}

//bookform.addEventListener('click', openform);

//bookform.addEventListener('click', closeform); // Add event listener to the close button
