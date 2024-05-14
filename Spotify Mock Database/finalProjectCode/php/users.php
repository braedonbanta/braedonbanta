<?php
    try {
        require('pdo_connect.php'); // Connect to the database
        $sql = 'SELECT * FROM User';
        $result = $dbc->query($sql);
    } catch (PDOException $e) {
        echo $e->getMessage();
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Users</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="../css/main.css">
    <link rel="stylesheet" href="../css/styles.css">
</head>
<body>
    <header>
        <h2>ALL USERS</h2>
    </header>
    <main>
        <section class="menu">
            <h2>MENU</h2>
            <nav>
                <ul>
                    <li><a href="../index.html">HOME</a></li>
                    <li><a href="../html/users.html" class="current">USERS</a></li>
                    <li><a href="../html/playlists.html">PLAYLISTS</a></li>
                    <li><a href="../html/charts.html">CHARTS</a></li>
                    <li><a href="../html/songs.html">SONGS</a></li>
                    <li><a href="../html/artists.html">ARTISTS</a></li>
                </ul>
            </nav>
        </section>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Username</th>
                    <th>Password</th>
                </tr>
            </thead>   
            <tbody>
                <?php foreach ($result as $user) { ?>
                    <tr>
                        <td><?php echo $user['userID']; ?></td>
                        <td><?php echo $user['firstName']; ?></td>
                        <td><?php echo $user['lastName']; ?></td>
                        <td><?php echo $user['username']; ?></td>
                        <td><?php echo $user['userpassword']; ?></td>
                    </tr>
                <?php } ?>
            </tbody>
        </table>
    </main>
    <footer>
        <h3>
            Email glv5151@uncw.edu (gabe), blb5012@uncw.edu (braedon), or tab7675@uncw.edu (thomas) with any questions!
        </h3>
    </footer>
</body>
</html>