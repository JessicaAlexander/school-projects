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
# -- Assignment:  [Use of echo() commands]
# -- Description: [Use the GET]
# ---------------

$FirstName= $_GET ['vFname'];
$LastName= $_GET ['vLname'];
$Email= $_GET ['vemail'];
$Phone= $_GET ['vphone'];
$DOB= $_GET ['vDob'];
echo("<p>Your name is $FirstName $LastName. Your email, phone number, and date of birth are $Email, $Phone, $DOB</p>");

?>

</body>
</html>