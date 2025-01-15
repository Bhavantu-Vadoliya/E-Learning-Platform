<!-- update_status.php --><?php
include_once('includes/config.php');

if (isset($_POST['task_id']) && isset($_POST['status'])) {
    $task_id = $_POST['task_id'];
    $status = $_POST['status'];

    $query = "UPDATE TASKS SET status = '$status' WHERE t_id = '$task_id'";
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