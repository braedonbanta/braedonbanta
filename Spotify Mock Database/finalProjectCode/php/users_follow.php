<?php
    try {
        require('pdo_connect.php'); // Connect to the database
        
        $username = $_POST['username']; // use POST to get the username entered; can put in sql statement so not hardcoded

        $sql = 'SELECT Followed.username FROM ur_follows
                JOIN User AS Follower ON ur_follows.follower = Follower.userID
                JOIN User AS Followed ON ur_follows.followed = Followed.userID
                WHERE Follower.username = :username';

        $stmt = $dbc->prepare($sql); // preparing the statement
        $stmt->bindParam(':username', $username); // bind the parameterto the thingy
        $stmt->execute(); // exec obv

        $result = $stmt->fetchAll(PDO::FETCH_ASSOC); // looked up how to use -> fetch the rows from the 'result set' ig
        // $result = $dbc->query($sql);
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
    <link rel="stylesheet" href="../css/songs.css">
</head>
<body>
    <header>
        <h2>SEE THE USERS A USER FOLLOWS</h2>
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
                    <th>Username</th>
                </tr>
            </thead>   
            <tbody>
                <?php foreach ($result as $username) { ?>
                    <tr>
                        <td><?php echo $username['username']; ?></td>
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