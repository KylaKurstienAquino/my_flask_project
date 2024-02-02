const fullform = document.body;
    const main = document.getElementById('main');

    function openBook() {
        main.style.display = 'flex';
        fullform.classList.add('main-open');
    }

    function closeBook() {
        main.style.display = 'none';
        fullform.classList.remove('main-open');
    }

    document.querySelector('.book').addEventListener('click', openBook);


function updateCheckoutDate() {
    var checkinDate = new Date(document.getElementById('cndcalendar').value);
    var checkoutInput = document.getElementById('codcalendar');
    checkoutInput.min = formatDate(checkinDate);
    checkoutInput.value = formatDate(checkinDate); 

    if (checkoutDate < checkinDate) {
        alert('Error: Invalid Check-Out Date');
        checkoutInput.value = formatDate(checkinDate);
        return;
    }

    checkoutInput.min = formatDate(checkinDate);
    checkoutInput.value = formatDate(checkinDate);

}

function updateRoomAvailability() {
    var checkinDate = new Date(document.getElementById('cndcalendar').value);
    var checkoutDate = new Date(document.getElementById('codcalendar').value);
    var roomSelect = document.getElementById('roomt');

    for (var i = 1; i < roomSelect.options.length; i++) {
        var roomType = roomSelect.options[i].value;

        if (roomType === 'room1' && (checkoutDate - checkinDate) < 86400000) {
            roomSelect.options[i].disabled = true;
        } else if (roomType === 'room2' && (checkoutDate - checkinDate) < 172800000) {
            roomSelect.options[i].disabled = true;
        } else if (roomType === 'room3' && (checkoutDate - checkinDate) < 259200000) {
            roomSelect.options[i].disabled = true;
        } else {
            roomSelect.options[i].disabled = false;
        }
    }
}

function formatDate(date) {
    var year = date.getFullYear();
    var month = ('0' + (date.getMonth() + 1)).slice(-2);
    var day = ('0' + date.getDate()).slice(-2);
    return year + '-' + month + '-' + day;
}


function calculateTotalPrice() {
    var roomPrice = 0;
    var totalPrice = 0;

    switch(roomSelect.value) {
        case 'room1':
            roomPrice = 350; 
            break;
        case 'room2':
            roomPrice = 300;
            break;
        case 'room3':
            roomPrice = 400;
            break;
        default:
            roomPrice = 0;
            break;
    }

    var checkinDate = new Date(document.getElementById('cndcalendar').value);
    var checkoutDate = new Date(document.getElementById('codcalendar').value);

    var oneDay = 24 * 60 * 60 * 1000;
    var nights = Math.round(Math.abs((checkinDate - checkoutDate) / oneDay));

    totalPrice = roomPrice * nights;

    document.getElementById('totalPrice').innerHTML = 'Total Price: $' + totalPrice;
}

document.getElementById('roomt').addEventListener('change', calculateTotalPrice);
document.getElementById('cndcalendar').addEventListener('change', calculateTotalPrice);
document.getElementById('codcalendar').addEventListener('change', calculateTotalPrice);

