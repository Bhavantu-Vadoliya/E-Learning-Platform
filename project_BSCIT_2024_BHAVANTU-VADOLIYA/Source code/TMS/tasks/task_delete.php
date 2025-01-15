<?php
session_start();
if(isset($_SESSION['unm']))
{
    include_once('../includes/config.php');
    $t_id=$_REQUEST['t_id'];
    $qry = "Delete from tasks where t_id=$t_id";
    mysqli_query($con,$qry) or exit("task Delete fail".mysqli_error($con));
    $_SESSION['del']="Deleted...";
    echo "<script type='text/javascript'> alert('Task Deleted successfully');
    window.location.href = '../manager_dashboard.php';
    </script>";
}
else{   
    $_SESSION['error']="your are not authorize to access this page without login";
    echo "<script type='text/javascript'> alert('Task Creation Failed!!');
    window.location.href = 'task_add .php';
    </script>";
}
?>
