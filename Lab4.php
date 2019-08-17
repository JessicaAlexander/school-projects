<!doctype html public>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Personal information Formm</title>
</head>
<body>
<?php
      # --------------
# -- Programmer:  [Jessica Alexander]
# -- Course:      ITSE-1306 (Intro to PHP)
# -- Instructor:  Cesar "Coach" Marrero
# -- Assignment:  [Week 4 Lab]
# -- Description: [Asks for a series of personal information from the user, and once the user presses the [SUBMIT] button, sends the data to a PHP script that generates HTML code displaying the data entered]
# ---------------

$FirstName= $_POST ['vFname'];
$LastName= $_POST ['vLname'];
$Email= $_POST ['vemail'];
$Phone= $_POST ['vphone'];
$DOB= $_POST ['vDob'];
echo("<p>Your name is $FirstName $LastName. Your email, phone number, and date of birth are $Email, $Phone, $DOB</p>");

?>

</body>
</html>