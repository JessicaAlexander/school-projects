
<!doctype html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>Greetings!</title>
	<style type="text/css">
	.bold {
		font-weight: bolder;
	}
	</style>
</head>
<body>
<?php // Script 3.7 - hello.php 
      # --------------
# -- Programmer:  [Jessica Alexander]
# -- Course:      ITSE-1306 (Intro to PHP)
# -- Instructor:  Cesar "Coach" Marrero
# -- Assignment:  [Chapter 3 Pursue]
# -- Description: [Use the GET]
# ---------------

ini_set('display_errors', 1);
$name = $_GET['name'];
print "<p>Hello, <span class=\"bold\">$name</span>!</p>";
?>
</body>
</html>