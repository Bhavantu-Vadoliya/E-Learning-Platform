<!-- task_edit_db.php -->
<!-- INSERT INTO TASKS VALUES(NULL, '$_POST[e_id]','$_POST[description]','$_POST[s_date]','$_POST[e_date]','Not Started') -->
<?php
session_start();
if(isset($_SESSION['unm']))
{
    include_once('../includes/config.php');
    extract($_POST);    
            $qry="UPDATE tasks SET  e_id='$e_id',description='$description',s_date='$s_date',e_date='$e_date',status='$status' WHERE t_id=$t_id";
            mysqli_query($con,$qry) or exit("task update fail".mysqli_error($con));
            $_SESSION['upd']="task Updated successfully"; 
            echo "<script type='text/javascript'> alert('Task Updated successfully');
            window.location.href = '../manager_dashboard.php';
            </script>";
}
else
{
    $_SESSION['error']="your are not authorize to access this page without login";
    echo "<script type='text/javascript'> alert('Something went wrong');
    window.location.href = 'task_edit.php';
    </script>";
}
?>

