<?php
    try {
        require('pdo_connect.php'); // Connect to the database
        
        // from the form
        $users_username = $_POST['users_username'];
        $mutuals_username = $_POST['mutuals_username'];

        // gettin the id's
        $sql = 'SELECT userID FROM User
                WHERE username = :username';
        // 'your' username first
        $stmt = $dbc->prepare($sql);
        $stmt->bindParam(':username', $users_username);
        $stmt->execute();
        $user1 = $stmt->fetch(PDO::FETCH_ASSOC); // get like the info from the stmt execution
        // username of user you're trying to see your mutuals with
        $stmt = $dbc->prepare($sql);
        $stmt->bindParam(':username', $mutuals_username);
        $stmt->execute();
        $user2 = $stmt->fetch(PDO::FETCH_ASSOC); // remains 'followed' because that's how it is called in the table

        // find mutual followers
        $sql = 'SELECT a.username AS mutual_follower
                FROM User AS a
                WHERE a.userID IN
                (   SELECT a1.follower
                    FROM ur_follows AS a1
                    WHERE a1.followed = :user1ID )
                AND a.userID IN
                (   SELECT a2.follower
                    FROM ur_follows AS a2
                    WHERE a2.followed = :user2ID )';
        // exec
        $stmt = $dbc->prepare($sql);
        $stmt->bindParam(':user1ID', $user1['userID']);
        $stmt->bindParam(':user2ID', $user2['userID']);
        $stmt->execute();
        $mutual_followers = $stmt->fetchAll(PDO::FETCH_ASSOC);

        // find mutual followed by
        $sql = 'SELECT a.username AS mutual_followed_by
                FROM User AS a
                WHERE a.userID IN
                (   SELECT a1.followed
                    FROM ur_follows AS a1
                    WHERE a1.follower = :user1ID )
                AND a.userID IN
                (   SELECT a2.followed
                    FROM ur_follows AS a2
                    WHERE a2.follower = :user2ID )';
        // exec
        $stmt = $dbc->prepare($sql);
        $stmt->bindParam(':user1ID', $user1['userID']);
        $stmt->bindParam(':user2ID', $user2['userID']);
        $stmt->execute();
        $mutual_followed_by = $stmt->fetchAll(PDO::FETCH_ASSOC);

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
    <link rel="stylesheet" href="../css/user_styles.css">
    <link rel="stylesheet" href="../css/user_mutuals.css">
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
        <h2 id="user_mutuals_thing">You (<?php echo $users_username?>) and user <?php echo $mutuals_username?>'s mutuals are displayed below</h2>
        <table id="following_table">
            <thead>
                <tr>
                    <th>Following</th>
                </tr>
            </thead>   
            <tbody>
                <!-- following -->
                <?php foreach ($mutual_followers as $follower) { ?>
                    <tr>
                        <td><?php echo $follower['mutual_follower'];?></td>
                    </tr>
                <?php } ?>
            </tbody>
        </table>
        <table id="followed_by_table">
            <thead>
                <tr>
                    <th>Followed By</th>
                </tr>
            </thead>   
            <tbody>
                <!-- followed by -->
                <?php foreach ($mutual_followed_by as $followed_by) { ?>
                    <tr>
                        <td><?php echo $followed_by['mutual_followed_by'];?></td>
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