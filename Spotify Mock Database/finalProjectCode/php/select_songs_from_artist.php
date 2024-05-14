<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Select Artist</title>
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
                    <li><a href="../html/playlists.html">PLAYLISTS</a></li>
                    <li><a href="../html/charts.html">CHARTS</a></li>
                    <li><a href="../html/songs.html">SONGS</a></li>
                    <li><a href="../html/artists.html" class="current">ARTISTS</a></li>
                </ul>
            </nav>
        </section>
        <h2>Select Artist</h2>
        <form action="../php/display_songs_from_artist.php" method="POST">
            <label for="artistName">Enter artist name:</label>
            <input type="text" id="artistName" name="artistName" required>
            <button type="submit">Search</button>
        </form>
    </main>
</body>
</html>
