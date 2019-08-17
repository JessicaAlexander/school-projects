<!doctype html>
<html lang = "en">
<head>
    <meta charset="utf-8">
    <title>Blood Alcohol Content Calculator</title>
        <style type="text/css">
            .number {font - weight: bold; }
        </style>
</head>
<body>
    <?php // Script4. - BAC.php
    /* This script takes values from BAC.html and calculates an individuals Blood Alcohol Content. */

          # --------------
# -- Programmer:  [Jessica Alexander]
# -- Course:      ITSE-1306 (Intro to PHP)
# -- Instructor:  Cesar "Coach" Marrero
# -- Assignment:  [Week 5 Lab]
# -- Description: [Calculate Blood Alcohol Content.]
# ---------------

    $Weight = $_POST['weight'];
    $Number_of_drinks = $_POST['Number_of_drinks'];
    $Amount_of_alcohol = $_POST['Amount_of_alcohol'];
    $Hours = $_POST['hours'];
    $Gender = $_POST['gender'];

    if($Gender=="Male")
{
$ratio=0.73;   
}
else
{
$ratio= 0.66;
}
    
    $BAC = ($Amount_of_alcohol * 5.14 )/ $Weight * $ratio - 0.015 * $Hours;

    print "<p>If your current weight is 
    <span class=\"number\">$Weight</span> pound(s) and you've had a total of <span class=\"number\">$Number_of_drinks </span> alcoholic drinks with an alcohol content of <span class=\"number\">$Amount_of_alcohol</span> percent over a span of <span class=\"number\">$Hours</span> hours and you are $Gender your total blood alcohol content will be <span class=\"number\">$BAC</span>.<br>
    If your BAC is greater than a 0.08 you are not able to drive. Please call an Uber!</p>"

    ?>
    </body>
    </html>
