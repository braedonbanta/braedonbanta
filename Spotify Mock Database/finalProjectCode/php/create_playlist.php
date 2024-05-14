<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Create Playlist for User</title>
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
        <h2>Create Playlist for User</h2>
        <form action="" method="POST">
            <label for="username">Enter username:</label>
            <input type="text" id="username" name="username" required>
            <br>
            <label for="playlist_name">Enter playlist name:</label>
            <input type="text" id="playlist_name" name="playlist_name" required>
            <br>
            <button type="submit">Create Playlist</button>
        </form>

        <?php
            try {
                require('pdo_connect.php');

                if ($_SERVER["REQUEST_METHOD"] == "POST") {
                    $username = $_POST['username'];
                    $playlistName = $_POST['playlist_name'];

                    // Check if the user exists
                    $sql = "SELECT userID FROM User WHERE username = :username";
                    $stmt = $dbc->prepare($sql);
                    $stmt->bindParam(':username', $username, PDO::PARAM_STR);
                    $stmt->execute();
                    $user = $stmt->fetch(PDO::FETCH_ASSOC);

                    if ($user) {
                        $userID = $user['userID'];

                        // ADDED BY GABE -> need to make an id for this because it's not default
                        // $playlistID = uniqid();
                        $length = 5;
                        $playlistID = '';
                        // looked up how to basically make a 'random' string of 5 chars in php
                        for ($i = 0; $i < $length; $i++) {
                            $playlistID .= mt_rand(0, 9); // Append a random digit (0-9) to the string
                        }

                        // Insert the playlist
                        $sql = "INSERT INTO Playlist (playlistID, playlistName, userID) VALUES (:playlistID, :playlistName, :userID)";
                        $stmt = $dbc->prepare($sql);
                        $stmt->bindParam(':playlistID', $playlistID, PDO::PARAM_STR);
                        $stmt->bindParam(':playlistName', $playlistName, PDO::PARAM_STR);
                        $stmt->bindParam(':userID', $userID, PDO::PARAM_STR);
                        $stmt->execute();

                        echo "<p>Playlist '$playlistName' created successfully for user '$username'!</p>";
                    } else {
                        echo "<p>User '$username' not found. Please enter a valid username.</p>";
                    }
                }
            } catch (PDOException $e) {
                echo "Error: " . $e->getMessage();
            }
        ?>
    </main>
</body>
</html>
