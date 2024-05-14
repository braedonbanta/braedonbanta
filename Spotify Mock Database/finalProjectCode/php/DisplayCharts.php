<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Display User Ranking Charts</title>
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
        <!-- <h2>Display Artist Ranking Charts</h2>
        <form action="" method="GET">
            <label for="artistName">Enter Artist Name:</label>
            <input type="text" id="artistName" name="artistName" required>
            <button type="submit">Search</button>
        </form> -->
        <h2>Select Chart</h2>
        <form method="GET" action="">
            <label for="chartName">Select Chart:</label>
            <select name="chartName" id="chartName">
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

        <?php
        try {
            require('pdo_connect.php');

            if ($_SERVER["REQUEST_METHOD"] == "GET") {
                $chartName = $_GET['chartName'];

                // Check if the selected chart is a song chart or an artist chart
                $isSongChart = false; // Assume it's not a song chart by default

                // Check if the chart name exists in the re_chartsongs table
                $sqlCheckSongChart = "SELECT COUNT(*) AS count FROM re_chartsongs WHERE chartName = :chartName";
                $stmtCheckSongChart = $dbc->prepare($sqlCheckSongChart);
                $stmtCheckSongChart->bindValue(':chartName', $chartName, PDO::PARAM_STR);
                $stmtCheckSongChart->execute();
                $songChartCount = $stmtCheckSongChart->fetchColumn();

                // If there are records in the re_chartsongs table, it's a song chart
                if ($songChartCount > 0) {
                    $isSongChart = true;
                }

                // Prepare the appropriate SQL query based on the chart type
                if ($isSongChart) {
                    // For song charts
                    $sql = "SELECT c.chartName, rs.ranking AS songRanking, s.songName, a.artistName
                            FROM Chart c
                            JOIN re_chartsongs rs ON c.chartName = rs.chartName
                            JOIN Songs s ON rs.songID = s.songID
                            JOIN Artist a ON s.artistID = a.artistID
                            WHERE c.chartName = :chartName
                            ORDER BY rs.ranking";
                } else {
                    // For artist charts
                    $sql = "SELECT c.chartName, ra.ranking AS artistRanking, a.artistID, a.artistName, COUNT(*) AS songCount
                            FROM Chart c
                            JOIN re_chartartists ra ON c.chartName = ra.chartName
                            JOIN Artist a ON ra.artistID = a.artistID
                            JOIN Songs s ON a.artistID = s.artistID
                            WHERE c.chartName = :chartName
                            GROUP BY c.chartName, ra.ranking, a.artistID, a.artistName
                            HAVING COUNT(*) > 0
                            ORDER BY ra.ranking";
                }

                // Execute the SQL query and fetch the chart data
                $stmt = $dbc->prepare($sql);
                $stmt->bindValue(':chartName', $chartName, PDO::PARAM_STR);
                $stmt->execute();
                $chartData = $stmt->fetchAll(PDO::FETCH_ASSOC);

                // Output the chart information
                if (count($chartData) > 0) {
                    echo "<h3>Chart: $chartName</h3>";
                    echo "<ul>";
                    foreach ($chartData as $data) {
                        if ($isSongChart) {
                            echo "<li>" . $data['songRanking'] . " - " . $data['songName'] . " by " . $data['artistName'] . "</li>";
                        } else {
                            echo "<li>" . $data['artistRanking'] . " - " . $data['artistName'] . " (" . $data['songCount'] . " songs)</li>";
                        }
                    }
                    echo "</ul>";
                } else {
                    echo "No chart found with the name: $chartName";
                }
            }
        } catch (PDOException $e) {
            echo "Error: " . $e->getMessage();
        }
        ?>
    </main>
</body>
</html>