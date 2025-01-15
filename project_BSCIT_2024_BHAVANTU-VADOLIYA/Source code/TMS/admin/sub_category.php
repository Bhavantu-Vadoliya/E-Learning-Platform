<?php
session_start();
if(isset($_SESSION['unm']))
{

?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>AdminLTE 3 | Dashboard</title>

  <!-- Google Font: Source Sans Pro -->
  <?php include_once('includes/style.php');
  ?>

<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
  <!-- Font Awesome -->
  <link rel="stylesheet" href="plugins/fontawesome-free/css/all.min.css">
  <!-- DataTables -->
  <link rel="stylesheet" href="plugins/datatables-bs4/css/dataTables.bootstrap4.min.css">
  <link rel="stylesheet" href="plugins/datatables-responsive/css/responsive.bootstrap4.min.css">
  <link rel="stylesheet" href="plugins/datatables-buttons/css/buttons.bootstrap4.min.css">
  <!-- Theme style -->
  <link rel="stylesheet" href="dist/css/adminlte.min.css">
</head>
<body class="hold-transition sidebar-mini layout-fixed">
<div class="wrapper">

  <!-- Preloader -->
  <div class="preloader flex-column justify-content-center align-items-center">
    <img class="animation__shake" src="dist/img/AdminLTELogo.png" alt="AdminLTELogo" height="60" width="60">
  </div>

  <!-- Navbar -->
  <?php include_once('includes/header.php');
  ?>
  <!-- /.navbar -->

  <!-- Main Sidebar Container -->
  <?php include_once('includes/sidebar.php');
  ?>
  <!-- Content Wrapper. Contains page content -->
  <div class="content-wrapper">
    <!-- Content Header (Page header) -->
    <div class="content-header">
      <div class="container-fluid">
        <div class="row mb-2">
          <div class="col-sm-6">
            <h1 class="m-0">Sub Categories</h1>
          </div><!-- /.col -->
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="dashboard.php">Home</a></li>
              <li class="breadcrumb-item"><a href="category.php">catagories</a></li>
              <li class="breadcrumb-item active">Sub catagories</li>
            </ol>
          </div><!-- /.col -->
        </div><!-- /.row -->
      </div><!-- /.container-fluid -->
    </div>
    <!-- /.content-header -->

    <!-- Main content -->
    <section class="content">
      <div class="container-fluid">
        <!-- Small boxes (Stat box) -->
      <div class="row">
        <div class="col-12">
        <div class="card">
              <div class="card-header">
                <h3 class="card-title">DataTable with default features</h3>
                <a href="sub_category_add.php"><button class="btn btn-primary float-right">Add New</button></a>
              </div>
              <!-- /.card-header -->

              <div class="card-body">
                <table id="example1" class="table table-bordered table-striped">
                  <thead>
                  <tr>
                    <th>ID</th>
                    <th>Images</th>
                    <th>category Name</th>
                    <th>Sub category Name</th>
                    <th>Sub Category Description</th>
                    <th>Action</th>
                  </tr>
                  </thead>
                  <tbody>
                    <?php
                      include_once('includes/config.php');
                      $qry="SELECT * FROM subcategories order by id desc";
                      $result = mysqli_query($con,$qry) or exit("Sub category Select fail".mysqli_error($con));
                      while($row= mysqli_fetch_array($result)) 
                      {
                            $subqry="SELECT cat_name FROM categories where id='".$row['catid']."'";
                            $subresult = mysqli_query($con,$subqry) or exit("category Select fail".mysqli_error($con));
                            $subrow= mysqli_fetch_array($subresult)
                        ?>
                        <tr>
                    <td><?php echo $row['id']; ?></td>
                    <td><img src="../images/subcategory/<?php echo $row['cat_image']?>" alt="not Found" width="200px" ></td>
                    <td><?php echo $subrow['cat_name'] ?></td>
                    <td><?php echo $row['sub_cat_name'] ?></td>
                    <td><?php echo $row['sub_cat_desc'] ?></td>
                    <td>
                        <a href="sub_category_delete.php?id=<?php echo $row['id']?>"><i class="fas fa-trash"></i></a>
                        <a href="sub_category_edit.php?id=<?php echo $row['id']?>"><i class="fas fa-edit"></i></a>
                    </td>
                  </tr>
                    <?php

                    }
?>
                  
                  </tbody>
                  <tfoot>
                  <tr>
                    <th>ID</th>
                    <th>Images</th>
                    <th>category Name</th>
                    <th>Sub category Name</th>
                    <th>Sub Category Description</th>
                    <th>Action</th>
                  </tr>
                  </tfoot>
                </table>
              </div>
              <!-- /.card-body -->
            </div>

        </div>

      </div>
        <!-- /.row -->
        <!-- Main row -->
       
        <!-- /.row (main row) -->
      </div><!-- /.container-fluid -->
    </section>
    <!-- /.content -->
  </div>
  <!-- /.content-wrapper -->
  <?php include_once('includes/footer.php');
?>   
</div>
<!-- ./wrapper -->

<!-- jQuery -->
<?php include_once('includes/script.php');
?>

<script src="plugins/jquery/jquery.min.js"></script>
<!-- Bootstrap 4 -->
<script src="plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
<!-- DataTables  & Plugins -->
<script src="plugins/datatables/jquery.dataTables.min.js"></script>
<script src="plugins/datatables-bs4/js/dataTables.bootstrap4.min.js"></script>
<script src="plugins/datatables-responsive/js/dataTables.responsive.min.js"></script>
<script src="plugins/datatables-responsive/js/responsive.bootstrap4.min.js"></script>
<script src="plugins/datatables-buttons/js/dataTables.buttons.min.js"></script>
<script src="plugins/datatables-buttons/js/buttons.bootstrap4.min.js"></script>
<script src="plugins/jszip/jszip.min.js"></script>
<script src="plugins/pdfmake/pdfmake.min.js"></script>
<script src="plugins/pdfmake/vfs_fonts.js"></script>
<script src="plugins/datatables-buttons/js/buttons.html5.min.js"></script>
<script src="plugins/datatables-buttons/js/buttons.print.min.js"></script>
<script src="plugins/datatables-buttons/js/buttons.colVis.min.js"></script>
<!-- AdminLTE App -->
<script src="dist/js/adminlte.min.js"></script>
<!-- AdminLTE for demo purposes -->
<script src="dist/js/demo.js"></script>
<!-- Page specific script -->
<script>
  $(function () {
    $("#example1").DataTable({
      "responsive": true, "lengthChange": false, "autoWidth": false,
      "buttons": ["copy", "csv", "excel", "pdf", "print", "colvis"]
    }).buttons().container().appendTo('#example1_wrapper .col-md-6:eq(0)');
    $('#example2').DataTable({
      "paging": true,
      "lengthChange": false,
      "searching": false,
      "ordering": true,
      "info": true,
      "autoWidth": false,
      "responsive": true,
    });
  });
</script>

</body>
</html>

<?php
if(isset($_SESSION['add']))
{?>
    <script>alert("Sub Category Added successfully")</script>          
    <?php
    unset($_SESSION['add']);
}

if(isset($_SESSION['del']))
{?>
    <script>alert("Sub Category Deleted successfully")</script>          
    <?php
    unset($_SESSION['del']);
}

if(isset($_SESSION['upd']))
{?>
    <script>alert("Sub Category Updated successfully")</script>          
    <?php
    unset($_SESSION['upd']);
}
?>

<?php
}
else{
  $_SESSION['error'] = "You are not authorised to access this";
  header("location:index.php");
}
?>
