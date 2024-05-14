<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Select Chart</title>
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
                    <li><a href="../html/charts.html" class="current">CHARTS</a></li>
                    <li><a href="../html/songs.html">SONGS</a></li>
                    <li><a href="../html/artists.html">ARTISTS</a></li>
                </ul>
            </nav>
        </section>
        <h2>Select Chart</h2>
        <form method="GET" action="../php/DisplayCharts.php">
            <label for="chart_id">Select Chart:</label>
            <select name="chart_id" id="chart_id">
                <?php
                    try {
                        require('pdo_connect.php'); 
                        $sql = "SELECT chartName FROM Chart";
                        $stmt = $dbc->query($sql);

                        while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                            echo '<option value="' . $row['chartName'] . '">' . $row['chartName'] . '</option>';
                        }
                    } catch (PDOException $e) {
                        echo "Error: " . $e->getMessage();
                    }
                ?>
            </select>
            <button type="submit">Display Chart</button>
        </form>
        
    </main>
</body>
</html>