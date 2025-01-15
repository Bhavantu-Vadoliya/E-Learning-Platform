<!-- image_edit_db.php -->
<?php
session_start();
if (isset($_SESSION['unm'])) {
    include_once('includes/config.php');
    extract($_POST);
    if ($_FILES['image']['error'] == 0) {
        $filename = time() . "_" . $_FILES['image']['name'];
        $path = "images/" . $filename;

        if (move_uploaded_file($_FILES['image']['tmp_name'], $path)) {
            $qry = "update images set id='".$id."' , image='" . $filename . "' where id=$o_id";
            mysqli_query($con, $qry) or exit("image update fail" . mysqli_error($con));
            $_SESSION['upd'] = "Image Updated successfully";

            echo "<script type='text/javascript'> alert('Image Updated successfully');
            window.location.href = 'images.php';
            </script>";
        } 
        else {
            $_SESSION['upd'] = "file upload fail";

            echo "<script type='text/javascript'> alert('Image Updatation Failed');
            window.location.href = 'images.php';
            </script>";
        }
    }

} else {
    $_SESSION['error'] = "your are not authorize to access this page without login";
    header("location:index.php");
}
?>