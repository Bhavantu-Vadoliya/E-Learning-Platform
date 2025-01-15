<?php
session_start();
if(isset($_SESSION['unm']))
{
    include_once('includes/config.php');
    extract($_POST);

    $filename=time()."_".$_FILES['image']['name'];
    $path="../images/subcategory/".$filename;
    $sub_cat_desc = mysqli_real_escape_string($con,$sub_cat_desc);

    if(move_uploaded_file($_FILES['image']['tmp_name'],$path))
    {
        $qry="insert into subcategories(catid,sub_cat_name,sub_cat_desc,cat_image) values('".$catid."','".$sub_cat_name."','".$sub_cat_desc."','".$filename."')";
        mysqli_query($con,$qry) or exit("Sub category insert fail".mysqli_error($con));
        $_SESSION['add']="Sub category added successfully"; 
        header("location:sub_category.php");
    }
    else
    {
    $_SESSION['add']="file upload fail";
        header("location:sub_category_add.php");
    }
}
else{
    $_SESSION['error']="your are not authorize to access this page without login";
    header("location:index.php");
}
?>
