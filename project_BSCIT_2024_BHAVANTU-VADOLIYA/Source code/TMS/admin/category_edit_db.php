<?php
session_start();
if(isset($_SESSION['unm']))
{
    include_once('includes/config.php');
    extract($_POST);
    $catdescription = mysqli_real_escape_string($con,$catdescription);
    if($_FILES['image']['error']==0)
    {
        $filename=time()."_".$_FILES['image']['name'];
        $path="../images/category/".$filename;
    
        if(move_uploaded_file($_FILES['image']['tmp_name'],$path))
        {
            $qry="update categories set cat_name='".$cname."' , cat_desc='".$catdescription."' , cat_image='".$filename."' where id=$id";
            mysqli_query($con,$qry) or exit("category update fail".mysqli_error($con));
            $_SESSION['upd']="category Updated successfully"; 
            header("location:category.php");
        }
        else
        {
        $_SESSION['upd']="file upload fail";
            header("location:category_edit.php");
        }
    } 
    else{
        $qry="update categories set cat_name='".$cname."' , cat_desc='".$catdescription."' where id=$id";
        mysqli_query($con,$qry) or exit("category insert fail".mysqli_error($con));
        $_SESSION['upd']="category Updated successfully"; 
        header("location:category.php");      
    } 
}
else{
    $_SESSION['error']="your are not authorize to access this page without login";
    header("location:index.php");
}
?>
