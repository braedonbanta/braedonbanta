<!DOCTYPE html>
<html lang="en">
<head>
    <title>Songs</title>
    <meta charset="utf-8">
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
        <h2>Songs</h2>
        <?php
        try {
            require('pdo_connect.php');
            $artistName = $_POST['artistName'];
            $sql = "SELECT * FROM Songs WHERE artistID IN (SELECT artistID FROM Artist WHERE artistName LIKE :artistName)";
            $stmt = $dbc->prepare($sql);
            $stmt->bindValue(':artistName','%'.$artistName.'%', PDO::PARAM_STR);
            $stmt->execute();
            $result = $stmt->fetchAll(PDO::FETCH_ASSOC);

            if (count($result) > 0) {
                echo "<table>";
                echo "<tr>";
                echo "<th>ID</th>";
                echo "<th>Name</th>";
                echo "<th>Length</th>";
                echo "<th>Release Date</th>";
                echo "<th>Artist ID</th>";
                echo "</tr>";
                foreach ($result as $song) {
                    echo "<tr>";
                    echo "<td>".$song['songID']."</td>";
                    echo "<td>".$song['songName']."</td>";
                    echo "<td>".$song['songLength']."</td>";
                    echo "<td>".$song['releaseDate']."</td>";
                    echo "<td>".$song['artistID']."</td>";
                    echo "</tr>";
                }
                echo "</table>";
            } else {
                echo "No songs found for the artist: $artistName";
            }
        } catch (PDOException $e) {
            echo $e->getMessage();
        }
        ?>
    </main>
</body>
</html>