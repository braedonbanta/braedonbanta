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
        <form action="../php/display_user.php" method="GET">
            <label for="username">Enter username:</label>
            <input type="text" id="username" name="username" required>
            <button type="submit">Search</button>
        </form>
    </main>
</body>
</html>
