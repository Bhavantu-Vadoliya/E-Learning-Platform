<!-- emp_register_db.php -->
<?php
 session_start();
 include('includes/config.php');
 if($con)
 {
    extract($_POST);
    $qry = mysqli_query($con,"INSERT INTO emp VALUES (NULL,'".$name."' , '".$email."' , '".md5($password)."');");
    if($qry)
    {  
        echo "<script type='text/javascript'> alert('Employee Added successfully');
        window.location.href = 'employees.php';
        </script>";
    }else{
        echo "Errorrrrr";
    }
 }else{
    echo"Error";
 }
?>