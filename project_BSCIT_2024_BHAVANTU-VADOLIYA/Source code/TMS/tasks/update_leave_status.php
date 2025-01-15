<!-- update_leave_status.php -->
 <!-- update_status.php --><?php
include_once('../includes/config.php');

if (isset($_POST['leave_id']) && isset($_POST['status'])) {
    $leave_id = $_POST['leave_id'];
    $status = $_POST['status'];

    $query = "UPDATE leaves SET status = '$status' WHERE l_id = '$leave_id'";
    $query_run = mysqli_query($con, $query);

    if ($query_run) {
        echo 'Status updated successfully';
    } else {
        echo 'Error updating status';
    }
} else {
    echo 'Invalid request';
}
?>