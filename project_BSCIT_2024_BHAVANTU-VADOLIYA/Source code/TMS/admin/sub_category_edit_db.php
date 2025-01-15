<?php
session_start();
if(isset($_SESSION['unm']))
{
    include_once('includes/config.php');
    extract($_POST);
    $sub_cat_desc = mysqli_real_escape_string($con,$sub_cat_desc);
    if($_FILES['image']['error']==0)
    {
        $filename=time()."_".$_FILES['image']['name'];
        $path="../images/subcategory/".$filename;
    
        if(move_uploaded_file($_FILES['image']['tmp_name'],$path))
        {
            $qry="update subcategories set sub_cat_name='".$sub_cat_name."' , sub_cat_desc='".$sub_cat_desc."' , cat_image='".$filename."' where id=$id";
            mysqli_query($con,$qry) or exit("sub category update fail".mysqli_error($con));
            $_SESSION['upd']="category Updated successfully"; 
            header("location:sub_category.php");
        }
        else
        {
        $_SESSION['upd']="file upload fail";
            header("location:sub_category_edit.php");
        }
    } 
    else{
        $qry="update subcategories set sub_cat_name='".$sub_cat_name."' , sub_cat_desc='".$sub_cat_desc."' where id=$id";
        mysqli_query($con,$qry) or exit("sub category insert fail".mysqli_error($con));
        $_SESSION['upd']="category Updated successfully"; 
        header("location:sub_category.php");      
    } 
}
else{
    $_SESSION['error']="your are not authorize to access this page without login";
    header("location:index.php");
}
?>
