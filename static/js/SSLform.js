function updateCheckoutDate() {
    var checkinDate = new Date(document.getElementById('cndcalendar').value);
    var checkoutInput = document.getElementById('codcalendar');
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