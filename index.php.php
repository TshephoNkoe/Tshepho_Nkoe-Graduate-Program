<!DOCTYPE html>
<html>
<head>
	<title>My Project</title>
    <style>
		var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
var income = [2000, 2500, 1500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000];
var expenses = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500];

var ctx = document.getElementById("myChart").getContext("2d");
var myChart = new Chart(ctx, {
    type: "bar",
    data: {
        labels: months,
        datasets: [
            {
                label: "Income",
                data: income,
                backgroundColor: "rgba(75, 192, 192, 0.2)"
            },
            {
                label: "Expenses",
                data: expenses,
                backgroundColor: "rgba(255, 99, 132, 0.2)"
            }
        ]
    },
    options: {
        scales: {
            yAxes: [
                {
                    ticks: {
                        beginAtZero: true
                    }
                }
            ]
        }
    }
});

	</style>
</head>
<body>
<canvas id="myChart"></canvas>
<script src="https://cdn.jsdelivr.net/npm/chart.js@2.9.3/dist/Chart.min.js"></script>


	<form action="index.php" method="post" enctype="multipart/form-data">
		<label>First Name:</label>
		<input type="text" name="first_name">
		<br><br>
		<label>Last Name:</label>
		<input type="text" name="last_name">
		<br><br>
		<label>Date of Birth:</label>
		<input type="date" name="dob">
		<br><br>
		<label>Upload Excel Document:</label>
		<input type="file" name="file">
		<br><br>
		<input type="submit" name="submit" value="Submit">
        <script>
	    var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        datasets: [{
            label: 'Income',
            data: [your_income_data_for_12_months],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        },{
            label: 'Expense',
            data: [your_expense_data_for_12_months],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 1
        }]
    },
    options: {}
	
});

</script>
</form>
    

	<?php 
		if ($_SERVER["REQUEST_METHOD"] == "POST") {
			$first_name = $_POST["first_name"];
			$last_name = $_POST["last_name"];
			$dob = $_POST["dob"];

			echo "<h2>Your Input:</h2>";
			echo "First Name: " . $first_name . "<br>";
			echo "Last Name: " . $last_name . "<br>";
			echo "Date of Birth: " . $dob . "<br>";
			
			$file = $_FILES['file'];

			$file_name = $file['name'];
			$file_tmp = $file['tmp_name'];
			$file_size = $file['size'];
			$file_error = $file['error'];

			$file_ext = explode('.', $file_name);
			$file_ext = strtolower(end($file_ext));

			$allowed = array('xls', 'xlsx');

			if (in_array($file_ext, $allowed)) {
				if ($file_error === 0) {
					if ($file_size <= 2097152) {
						$file_name_new = uniqid('', true) . '.' . $file_ext;
						$file_destination = 'uploads/' . $file_name_new;
						if (move_uploaded_file($file_tmp, $file_destination)) {
							echo "File uploaded successfully!";
						}
					}
				}
			}
		}
	?>
</body>
</html>