<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Search User</title>
    <link rel="stylesheet" href="../css/main.css">
</head>
<body>
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
        <h2>Search User</h2>
        <form action="" method="GET">
            <label for="username">Enter username:</label>
            <input type="text" id="username" name="username" required>
            <button type="submit">Search</button>
        </form>

        <?php
            try {
                require('pdo_connect.php');
                $username = $_GET['username'];
                $sql = "SELECT User1.* 
                        FROM User User1 
                        JOIN User User2 ON User1.userID = User2.userID
                        WHERE User1.username LIKE :username";
                $stmt = $dbc->prepare($sql);
                $stmt->bindValue(':username', '%'. $username.'%', PDO::PARAM_STR);
                $stmt->execute();
                $users = $stmt->fetchAll(PDO::FETCH_ASSOC);

                if (count($users) > 0) {
                    echo "<h3>Search Results:</h3>";
                    echo "<ul>";
                    foreach ($users as $user) {
                        echo"<li>".$user['firstName'].' '.$user['lastName']."</li>";
                    }
                    echo "</ul>";
                } else {
                    echo "No users found with the username: $username";
                }
            } catch (PDOException $e) {
                echo "Error: " . $e->getMessage();
            }
        ?>
    </main>
</body>
</html>
