<?php
session_start();
if(isset($_SESSION['unm']))
{
    include_once('includes/config.php');
    extract($_POST);

    $filename=time()."_".$_FILES['image']['name'];
    $path="../images/category/".$filename;
    $catdescription = mysqli_real_escape_string($con,$catdescription);

    if(move_uploaded_file($_FILES['image']['tmp_name'],$path))
    {
        $qry="insert into categories(cat_name,cat_desc,cat_image) values('".$cname."','".$catdescription."','".$filename."')";
        mysqli_query($con,$qry) or exit("category insert fail".mysqli_error($con));
        $_SESSION['add']="category added successfully"; 
        header("location:category.php");
    }
    else
    {
    $_SESSION['add']="file upload fail";
        header("location:category_add.php");
    }
}
else{
    $_SESSION['error']="your are not authorize to access this page without login";
    header("location:index.php");
}
?>
