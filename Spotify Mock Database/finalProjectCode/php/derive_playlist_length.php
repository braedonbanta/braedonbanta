<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Calculate Playlist Length</title>
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
        <h2>Calculate Playlist Length</h2>
        <form method="POST" action="../php/display_playlist_length.php">
            <label for="playlist_id">Select Playlist:</label>
            <select name="playlist_id" id="playlist_id">
                <?php
                try {
                    require('pdo_connect.php'); 
                    $sql = "SELECT playlistID, playlistName FROM Playlist";
                    $stmt = $dbc->query($sql);

                    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                        echo "<option value='".$row['playlistID']."'>".$row['playlistName']."</option>";
                    }
                } catch (PDOException $e) {
                    echo "Error: " . $e->getMessage();
                }
                ?>
            </select>
            <button type="submit">Calculate</button>
        </form>
    </main>
</body>
</html>
