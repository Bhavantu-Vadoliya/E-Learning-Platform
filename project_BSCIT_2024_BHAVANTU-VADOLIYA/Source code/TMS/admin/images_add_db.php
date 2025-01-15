<!-- images_add_db.php -->
<?php
session_start();
if(isset($_SESSION['unm']))
{
    include_once('includes/config.php');
    extract($_POST);

    $filename=time()."_".$_FILES['image']['name'];
    $path="images/".$filename;
    if(move_uploaded_file($_FILES['image']['tmp_name'],$path))
    {
        $qry="insert into images values('".$id."','".$filename."')";
        mysqli_query($con,$qry) or exit("Image insert fail".mysqli_error($con));
        $_SESSION['add']="Image added successfully"; 
        header("location:images.php");
    }
    else
    {
    $_SESSION['add']="image upload fail";
        header("location:images_add.php");
    }
}
else{
    $_SESSION['error']="your are not authorize to access this page without login";
    header("location:index.php");
}
?>
