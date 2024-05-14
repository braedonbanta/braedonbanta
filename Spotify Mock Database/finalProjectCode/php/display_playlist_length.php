<?php
try {
    require('pdo_connect.php');
    $playlist_id = $_POST['playlist_id'];
    $sql = "SELECT SEC_TO_TIME(SUM(TIME_TO_SEC(songLength))) AS total_length 
            FROM Songs 
            WHERE songID IN (SELECT songID FROM re_has WHERE playlistID = :playlist_id)";
    $stmt = $dbc->prepare($sql);
    $stmt->bindParam(':playlist_id', $playlist_id, PDO::PARAM_INT);
    $stmt->execute();
    $result = $stmt->fetch(PDO::FETCH_ASSOC);

    $total_length = $result['total_length'];
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Calculate Playlist Length Result</title>
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
        <?php if (isset($total_length)) { ?>
            <div>
                <h3>Total Length of Selected Playlist:</h3>
                <p><?php echo $total_length; ?></p>
            </div>
        <?php } ?>
    </main>
</body>
</html>
