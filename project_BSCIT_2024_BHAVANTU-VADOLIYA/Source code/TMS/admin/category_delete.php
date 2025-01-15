<?php
session_start();
if(isset($_SESSION['unm']))
{
    include_once('includes/config.php');
    $id=$_REQUEST['id'];
    $qry = "Delete from categories where id=$id";
    mysqli_query($con,$qry) or exit("category Delete fail".mysqli_error($con));
    $_SESSION['del']="Deleted...";
    header("location:category.php");
}
else{
    $_SESSION['error']="your are not authorize to access this page without login";
    header("location:index.php");
}
?>
