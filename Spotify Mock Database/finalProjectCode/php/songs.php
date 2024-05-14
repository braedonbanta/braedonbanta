<?php
    try {
        require('pdo_connect.php'); // Connect to the database
        $sql = 'SELECT * FROM Songs';
        $result = $dbc->query($sql);
    } catch (PDOException $e) {
        echo $e->getMessage();
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Songs</title>
    <meta charset="utf-8">
    <link rel="stylesheet" href="../css/main.css">
    <link rel="stylesheet" href="../css/songs.css">
</head>
<body>
    <header>
        <h2>ALL SONGS</h2>
    </header>
    <main>
        <section class="menu">
            <h2>MENU</h2>
            <nav>
                <ul>
                    <li><a href="../index.html">HOME</a></li>
                    <li><a href="../html/users.html">USERS</a></li>
                    <li><a href="../html/playlists.html">PLAYLISTS</a></li>
                    <li><a href="../html/charts.html">CHARTS</a></li>
                    <li><a href="../html/songs.html" class="current">SONGS</a></li>
                    <li><a href="../html/artists.html">ARTISTS</a></li>
                </ul>
            </nav>
        </section>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Length</th>
                    <th>Release Date</th>
                    <th>Artist ID</th>
                </tr>
            </thead>   
            <tbody>
                <?php foreach ($result as $song) { ?>
                    <tr>
                        <td><?php echo $song['songID']; ?></td>
                        <td><?php echo $song['songName']; ?></td>
                        <td><?php echo $song['songLength']; ?></td>
                        <td><?php echo $song['releaseDate']; ?></td>
                        <td><?php echo $song['artistID']; ?></td>
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