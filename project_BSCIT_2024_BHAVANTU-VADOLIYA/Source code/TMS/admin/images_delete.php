<!-- images_delete.php -->
<?php
session_start();
if(isset($_SESSION['unm']))
{
    include_once('includes/config.php');
    $id=$_REQUEST['id'];
    $qry = "Delete from images where id=$id";
    mysqli_query($con,$qry) or exit("image Delete fail".mysqli_error($con));
    $_SESSION['del']="Deleted...";
    header("location:images.php");
}
else{
    $_SESSION['error']="your are not authorize to access this page without login";
    header("location:index.php");
}
?>
