<?php
	// See all errors and warnings
	error_reporting(E_ALL);
	ini_set('error_reporting', E_ALL);

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
	<title>Facial Recognition</title>
	<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
	<meta charset="utf-8" />
</head>
<body>
	<h1>If this loads then check to see if the database is updated!</h1>
</body>
</html>