<!-- manager_delete.php -->
<?php
session_start();
if(isset($_SESSION['unm']))
{
    include_once('includes/config.php');
    $id=$_REQUEST['id'];
    $qry = "Delete from admin where id=$id";
    mysqli_query($con,$qry) or exit("manager Delete fail".mysqli_error($con));
    $_SESSION['del']="Deleted...";
    echo "<script type='text/javascript'> alert('Manager Removed successfully');
    window.location.href = 'managers.php';
    </script>";
}
else{   
    $_SESSION['error']="your are not authorize to access this page without login";
    echo "<script type='text/javascript'> alert(' Failed!!');
    window.location.href = 'managers.php';
    </script>";
}
?>
