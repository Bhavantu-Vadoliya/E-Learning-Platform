<?php
// Configuration
// $db_host = 'localhost';
// $db_username = 'root';
// $db_password = '';
// $db_name = 'login';

// // Create connection
// $con = new mysqli($db_host, $db_username, $db_password, $db_name);
session_start();

include_once('includes/config.php');

// extract($_POST);


// Check connection
if ($con->connect_error) {
    die("Connection failed: " . $con->connect_error);
}

// Login function
function login($username, $password) {
    global $con;

    // Check admin credentials
    $admin_query = "SELECT * FROM admin WHERE unm = '$username' AND pwd = md5('$password')";
    $admin_result = $con->query($admin_query);
    if ($admin_result->num_rows > 0) {
        // Redirect to emp.php
        $_SESSION['unm']=$username;
        header('Location: manager_dashboard.php');
        exit;
    }

    // Check employee credentials
    $emp_query = "SELECT * FROM emp WHERE mail = '$username' AND pwd = md5('$password')";
    $emp_result = $con->query($emp_query);
    if ($emp_result->num_rows > 0) {
        // Redirect to admin.php
        $_SESSION['mail']=$username;
        header('location:emp_dashboard.php');
        exit;
    }

    // If no match, display error message
    $_SESSION['error'] = "Your <b>Username</b> or <b>Password</b> is Incorrect";
    echo "Invalid username or password";
    header('location:sign_in.php');
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Call login function
    login($username, $password);
}

// Close connection
$con->close();
?>

<!-- Login form -->
<!-- <form action="" method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Login">
</form> -->