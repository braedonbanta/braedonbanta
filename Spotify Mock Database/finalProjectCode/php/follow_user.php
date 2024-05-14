<?php
    try {
        require('pdo_connect.php'); // Connect to the database
        
        // from the form
        $users_username = $_POST['users_username'];
        $new_followed_username = $_POST['new_followed_username'];

        // gettin the id's
        $sql = 'SELECT userID FROM User
                WHERE username = :username';
        // 'your' username first
        $stmt = $dbc->prepare($sql);
        $stmt->bindParam(':username', $users_username);
        $stmt->execute();
        $follower = $stmt->fetch(PDO::FETCH_ASSOC); // get like the info from the stmt execution
        // username of user you're trying to follow next
        $stmt = $dbc->prepare($sql);
        $stmt->bindParam(':username', $new_followed_username);
        $stmt->execute();
        $followed = $stmt->fetch(PDO::FETCH_ASSOC);

        // actually create a new relationship in database (in ur_follows, since users both alr exist)
        $sql = "INSERT INTO ur_follows (follower, followed) VALUES (:follower, :followed)";
        $stmt = $dbc->prepare($sql);
        // bind params for injection protection stuff (interpreted from slides and research ?)
        $stmt->bindParam(':follower', $follower['userID']);
        $stmt->bindParam(':followed', $followed['userID']);
        $stmt->execute();

        // make sure the username can get displayed back to user
        $username = $new_followed_username; // $followed['username'];

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
    <link rel="stylesheet" href="../css/user_styles.css">
</head>
<body>
    <header>
        <h2>FOLLOW ANOTHER USER</h2>
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
        <div class="explanation">
            <h3>User <?php echo $username; ?> has been followed! Check 'your' <a href="../html/users_follow.html">following</a> to see that it has been updated!</h3>
        </div>
    </main>
    <footer>
        <h3>
            Email glv5151@uncw.edu (gabe), blb5012@uncw.edu (braedon), or tab7675@uncw.edu (thomas) with any questions!
        </h3>
    </footer>
</body>
</html>