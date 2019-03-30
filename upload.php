<?php
	// See all errors and warnings
	error_reporting(E_ALL);
	ini_set('error_reporting', E_ALL);

	// Your database details might be different
	//$mysqli = mysqli_connect("localhost", "root", "", "dbUser");

	//$email = isset($_POST["email"]) ? $_POST["email"] : false;
	//$pass = isset($_POST["pass"]) ? $_POST["pass"] : false;


	if (isset($_FILES["picToUpload"])) {
		$questionCover = $_FILES["picToUpload"];
		
		// Establish MongoDB Connection
		$connection = new MongoDB\Client("mongodb+srv://fr_dbAdmin:ZGEkMGEeTYg6fmyH@fr-db-c5rwj.gcp.mongodb.net/test?retryWrites=true");
		$databaseMongo = $connection->selectDatabase(Config::get('FR-DB'));
		
		$testCollection = $databaseMongo->selectCollection("testing");
		$document = array(
			"type" => "MCQ",
			"cover" => new MongoDB\BSON\Binary(file_get_contents($questionCover["tmp_name"]), MongoDB\BSON\Binary::TYPE_GENERIC),
		);
		if ($testCollection>insertOne($document)) {
			return true;
		}
		return false;
	}
?>

<!DOCTYPE html>
<html>
<head>
	<title>IMY 220 - Assignment 4</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
	<meta charset="utf-8" />
</head>
<body>
	<div class="container">
	<h1>WORKS!</h1>
		<?php/*
			if($email && $pass){
				$query = "SELECT * FROM tbusers WHERE email = '$email' AND password = '$pass'";
				$res = $mysqli->query($query);
				if($row = mysqli_fetch_array($res)){
					echo 	"<table class='table table-bordered mt-3'>
								<tr>
									<td>Name</td>
									<td>" . $row['name'] . "</td>
								<tr>
								<tr>
									<td>Surname</td>
									<td>" . $row['surname'] . "</td>
								<tr>
								<tr>
									<td>Email Address</td>
									<td>" . $row['email'] . "</td>
								<tr>
								<tr>
									<td>Birthday</td>
									<td>" . $row['birthday'] . "</td>
								<tr>
							</table>";
				
					echo 	"<form enctype='multipart/form-data'>
								<div class='form-group'>
									<input type='file' class='form-control' name='picToUpload[]' id='picToUpload' multiple='multiple' /><br/>
									<input type='submit' class='btn btn-standard' value='Upload Image' name='submit' />
								</div>
						  	</form>";
				}
				else{
					echo 	'<div class="alert alert-danger mt-3" role="alert">
	  							You are not registered on this site!
	  						</div>';
				}
			} 
			else{
				echo 	'<div class="alert alert-danger mt-3" role="alert">
	  						Could not log you in
	  					</div>';
			}*/
		?>
	</div>
</body>
</html>