<?php

$fname = $_POST['fnames'];
$lname = $_POST['lnames'];
$email = $_POST['mailes'];
$phone = $_POST['numbers'];
$address = $_POST['addre'];
$city = $_POST['cits'];
$state = $_POST['stats'];
$postal = $_POST['postals'];
$checkin = $_POST['cndcalendar'];
$checkout = $_POST['codcalendar'];
$room = $_POST['room'];
$guests = $_POST['numguest'];
$notes = $_POST['notes'];

$DBHost = "localhost"; 
$DBUser = "root"; 
$DBPass = ""; 
$DBName = "database_employee"; 

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO your_table (fname, lname, email, phone, address, city, state, postal, checkin, checkout, room, guests, notes)
        VALUES ('$fname', '$lname', '$email', '$phone', '$address', '$city', '$state', '$postal', '$checkin', '$checkout', '$room', '$guests', '$notes')";

if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
