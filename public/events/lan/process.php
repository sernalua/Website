<?php
	// Data file
	$res_file = "../../../lanres.txt";
		
	// Input check
	if(empty($_POST['cid']) ||
	   empty($_POST['name'])) {
		header("Refresh:3; /events/lan", true, 303);
		die("Please enter your name and Coyote ID. You will be sent back to the form.");
	}

	// Add reservation to file
	file_put_contents($res_file, $_POST['cid'] . " - " . $_POST['name'] . "\n", FILE_APPEND | LOCK_EX);
		    
	echo "Your reservation has been made!";

	header("Refresh:3; url=http://cse-club.com", true, 303);
