<?php
    session_start();
    include('includes/config.php');
    extract($_POST);                         
    $qry = "select * from admin where unm='".$unm."' && pwd='".md5($pwd)."'";
    $res=mysqli_query($con,$qry) or exit("Select user fail".mysqli_error($con));
    $count = mysqli_num_rows($res);
    if($count>0){
        $_SESSION['unm']=$unm;
        header("location:dashboard.php");
    }else{
        $_SESSION['error'] = "Your <b>Username</b> or <b>Password</b> is Incorrect";
        header("location:index.php");
    }

?>