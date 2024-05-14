<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Search User Playlists</title>
    <link rel="stylesheet" href="../css/main.css">
</head>
<body>
    <main>
        <section class="menu">
            <h2>MENU</h2>
            <nav>
                <ul>
                    <li><a href="../index.html">HOME</a></li>
                    <li><a href="../html/users.html">USERS</a></li>
                    <li><a href="../html/playlists.html" class="current">PLAYLISTS</a></li>
                    <li><a href="../html/charts.html">CHARTS</a></li>
                    <li><a href="../html/songs.html">SONGS</a></li>
                    <li><a href="../html/artists.html">ARTISTS</a></li>
                </ul>
            </nav>
        </section>
        <h2>Search User Playlists</h2>
        <form action="" method="GET">
            <label for="username">Enter username:</label>
            <input type="text" id="username" name="username" required>
            <button type="submit">Search</button>
        </form>

        <?php
            try {
                require('pdo_connect.php');
                $username = $_GET['username'];
                $sql = "SELECT Playlist.playlistID, Playlist.playlistName 
                        FROM Playlist 
                        JOIN User ON Playlist.userID = User.userID
                        WHERE User.username LIKE :username";
                $stmt = $dbc->prepare($sql);
                $stmt->bindValue(':username', '%'. $username.'%', PDO::PARAM_STR);
                $stmt->execute();
                $playlists = $stmt->fetchAll(PDO::FETCH_ASSOC);

                if (count($playlists) > 0) {
                    echo "<h3>Playlists for User: $username</h3>";
                    echo "<ul>";
                    foreach ($playlists as $playlist) {
                        echo "<li>".$playlist['playlistName']."</li>";
                    }
                    echo "</ul>";
                } else {
                    echo "No playlists found for user with username: $username";
                }
            } catch (PDOException $e) {
                echo "Error: " . $e->getMessage();
            }
        ?>
    </main>
</body>
</html>