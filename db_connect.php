<?php

$servername = "MySQL";
$username = "root";
$password = "";
$dbname = "MySQL";

// Create connection
$conn = mysqli_connect($MySQL, $root, $MySQL);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

echo "Connected successfully";

?>
<?php

require_once 'db_connect.php';

// Perform database operations here

?>
<?php

require_once 'db_connect.php';

// Perform database operations here

$sql = "INSERT INTO financials (month, income, expenses)
VALUES ('January', 19770, 3438),
       ('February', 29926, 25382),
       ('March', 21500, 26737),
       ('April', 29023, 18685),
       ('May', , 26737, 22691),
       ('june', 29245, 13706),
       ('July', 28474, 10402),
       ('August', 25398, 12039),
       ('September', 33953, 3411),
       ('October', 30650, 26110),
       ('November', 20149, 9971),
       ('December', 30613, 20821)";

if (mysqli_query($conn, $sql)) {
    echo "Records inserted successfully.";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

?>


