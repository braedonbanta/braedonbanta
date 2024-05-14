/* table creation */

CREATE TABLE User 
(   
    userID  CHAR(5)    NOT NULL,
    firstName   CHAR(15)    NOT NULL,
    lastName    CHAR(15)    NOT NULL,
    username    CHAR(15)    NOT NULL,
    userpassword    CHAR(15)    NOT NULL,
    PRIMARY KEY (userID) );

CREATE TABLE Artist
(   artistID CHAR(5)   NOT NULL,
    artistName CHAR(30) NOT NULL,
    PRIMARY KEY (artistID) );

CREATE TABLE Songs
(
    songID CHAR(5)  NOT NULL,
    songName    CHAR(30)    NOT NULL,
    songLength  CHAR(5) NOT NULL,
    releaseDate DATE    NOT NULL,
    artistID   CHAR(20),
    PRIMARY KEY (songID),
    FOREIGN KEY (artistID) REFERENCES Artist(artistID) );

CREATE TABLE mv_SongGenre
(
    genre   CHAR(15)    NOT NULL,
    songID CHAR(5)  NOT NULL,
    PRIMARY KEY (genre, songID),
    FOREIGN KEY (songID) REFERENCES Songs(songID) );

CREATE TABLE Playlist 
(
    playlistID  CHAR(5) NOT NULL,
    playlistName    CHAR(15)    NOT NULL,
    userID  CHAR(5)    NOT NULL,
    PRIMARY KEY (playlistID),
    FOREIGN KEY (userID) REFERENCES User(userID) );

CREATE TABLE Chart
(
    chartName CHAR(20) NOT NULL,
    updatedLast DATE, -- make trigger for this
    PRIMARY KEY (chartName) );

CREATE TABLE re_catalogues
(
    userID CHAR(5) NOT NULL,
    songID CHAR(5) NOT NULL,
    PRIMARY KEY (userID, songID),
    FOREIGN KEY (userID) REFERENCES User(userID),
    FOREIGN KEY (songID) REFERENCES Songs(songID) );

CREATE TABLE ur_follows
(
    follower    CHAR(5) NOT NULL,
    followed    CHAR(5) NOT NULL,
    PRIMARY KEY (follower, followed),
    FOREIGN KEY (follower) REFERENCES User(userID),
    FOREIGN KEY (followed) REFERENCES User(userID) );

CREATE TABLE re_likes
(
    userID_User  CHAR(5)     NOT NULL,
    userID_Playlist CHAR(5) NOT NULL,
    playlistID  CHAR(5) NOT NULL,
    PRIMARY KEY (userID_User, userID_Playlist, playlistID),
    FOREIGN KEY (userID_User) REFERENCES User(userID),
    FOREIGN KEY (userID_Playlist) REFERENCES Playlist(userID), 
    FOREIGN KEY (playlistID) REFERENCES Playlist(playlistID) );

CREATE TABLE re_has
(
    playlistID CHAR(5) NOT NULL,
    songID CHAR(5) NOT NULL,
    PRIMARY KEY (playlistID, songID),
    FOREIGN KEY (playlistID) REFERENCES Playlist(playlistID),
    FOREIGN KEY (songID) REFERENCES Songs(songID) );

CREATE TABLE re_makes
(
    songID CHAR(5) NOT NULL,
    artistID CHAR(5) NOT NULL,
    PRIMARY KEY (songID, artistID),
    FOREIGN KEY (songID) REFERENCES Songs(songID),
    FOREIGN KEY (artistID) REFERENCES Artist(artistID) );

CREATE TABLE re_chartsongs
(
    songID CHAR(5) NOT NULL,
    chartName CHAR(20) NOT NULL,
    ranking INT NOT NULL,
    PRIMARY KEY (songID, chartName),
    FOREIGN KEY (songID) REFERENCES Songs(songID),
    FOREIGN KEY (chartName) REFERENCES Chart(chartName)
);

CREATE TABLE re_chartartists
(
    artistID CHAR(5) NOT NULL,
    chartName CHAR(20) NOT NULL,
    ranking INT NOT NULL,
    PRIMARY KEY (artistID, chartName),
    FOREIGN KEY (chartName) REFERENCES Chart(chartName),
    FOREIGN KEY (artistID) REFERENCES Artist(artistID) );

/* insert statements */
-- Users
INSERT INTO User VALUES ('12345', 'gabe', 'vega', 'gabevega', 'ilovemusic');
INSERT INTO User VALUES ('67891', 'thomas', 'bourget', 'thombour', 'ilovemusic1');
INSERT INTO User VALUES ('13578', 'braedon', 'banta', 'braedbant', 'ilovemusic2');
INSERT INTO User VALUES ('19246', 'adam', 'pridgen', 'adampridg', 'ilovemusic3');
INSERT INTO User VALUES ('83591', 'haley', 'goldberg', 'haleygold', 'ilovemusic4');

-- Artists
INSERT INTO Artist Values('00001', 'Adele');
INSERT INTO Artist Values('00002', 'Bruno Mars');
INSERT INTO Artist Values('00003', 'Coldplay');
INSERT INTO Artist Values('00004', 'Drake');
INSERT INTO Artist Values('00005', 'Ed Sheeran');
INSERT INTO Artist Values('00006', 'Beyonce');
INSERT INTO Artist Values('00007', 'Taylor Swift');
INSERT INTO Artist Values('00008', 'Kendrick Lamar');

-- Songs
INSERT INTO Songs VALUES ('10001', 'Rolling in the Deep', '3:49', '2010-11-29', '00001');
INSERT INTO Songs VALUES ('10002', 'Someone Like You', '4:45', '2011-01-24', '00001');
INSERT INTO Songs VALUES ('10003', 'Hello', '4:55', '2015-10-23', '00001');
INSERT INTO Songs VALUES ('10004', 'Set Fire to the Rain', '4:01', '2011-11-21', '00001');
INSERT INTO Songs VALUES ('10005', 'Skyfall', '4:46', '2012-10-05', '00001');
INSERT INTO Songs VALUES ('10006', 'When We Were Young', '4:51', '2016-01-22', '00001');

INSERT INTO Songs VALUES ('10007', 'Just the Way You Are', '3:40', '2010-07-20', '00002');
INSERT INTO Songs VALUES ('10008', 'Locked Out of Heaven', '3:53', '2012-10-01', '00002');
INSERT INTO Songs VALUES ('10009', 'Grenade', '3:42', '2010-09-28', '00002');
INSERT INTO Songs VALUES ('10010', 'Uptown Funk', '4:31', '2014-11-10', '00002');
INSERT INTO Songs VALUES ('10011', 'Treasure', '2:56', '2013-05-10', '00002');
INSERT INTO Songs VALUES ('10012', '24K Magic', '3:46', '2016-10-07', '00002');

INSERT INTO Songs VALUES ('10013', 'Viva la Vida', '4:02', '2008-05-25', '00003');
INSERT INTO Songs VALUES ('10014', 'Fix You', '4:55', '2005-09-05', '00003');
INSERT INTO Songs VALUES ('10015', 'Clocks', '5:07', '2003-03-24', '00003');
INSERT INTO Songs VALUES ('10016', 'Yellow', '4:29', '2000-06-26', '00003');
INSERT INTO Songs VALUES ('10017', 'Paradise', '4:37', '2011-09-12', '00003');
INSERT INTO Songs VALUES ('10018', 'The Scientist', '5:09', '2002-11-11', '00003');

INSERT INTO Songs VALUES ('10019', 'Hotline Bling', '4:27', '2015-07-31', '00004');
INSERT INTO Songs VALUES ('10020', 'God''s Plan', '3:18', '2018-01-19', '00004');
INSERT INTO Songs VALUES ('10021', 'In My Feelings', '3:37', '2018-07-10', '00004');
INSERT INTO Songs VALUES ('10022', 'One Dance', '2:54', '2016-04-05', '00004');
INSERT INTO Songs VALUES ('10023', 'Started From the Bottom', '3:04', '2013-02-01', '00004');
INSERT INTO Songs VALUES ('10024', 'Hold On, Were Going Home', '3:47', '2013-08-07', '00004');

INSERT INTO Songs VALUES ('10025', 'Shape of You', '3:53', '2017-01-06', '00005');
INSERT INTO Songs VALUES ('10026', 'Thinking Out Loud', '4:41', '2014-09-24', '00005');
INSERT INTO Songs VALUES ('10027', 'Photograph', '4:19', '2015-05-11', '00005');
INSERT INTO Songs VALUES ('10028', 'Castle on the Hill', '4:21', '2017-01-06', '00005');
INSERT INTO Songs VALUES ('10029', 'Perfect', '4:23', '2017-09-26', '00005');
INSERT INTO Songs VALUES ('10030', 'The A Team', '4:18', '2011-06-12', '00005');

INSERT INTO Songs VALUES ('10031', 'Single Ladies (Put a Ring on It)', '3:13', '2008-10-13', '00006');
INSERT INTO Songs VALUES ('10032', 'Halo', '4:22', '2009-01-20', '00006');
INSERT INTO Songs VALUES ('10033', 'Crazy in Love', '3:56', '2003-05-20', '00006');
INSERT INTO Songs VALUES ('10034', 'Drunk in Love', '5:23', '2013-12-17', '00006');
INSERT INTO Songs VALUES ('10035', 'Irreplaceable', '3:47', '2006-10-23', '00006');
INSERT INTO Songs VALUES ('10036', 'Formation', '3:26', '2016-02-06', '00006');

INSERT INTO Songs VALUES ('10037', 'Shake It Off', '3:39', '2014-08-18', '00007');
INSERT INTO Songs VALUES ('10038', 'Love Story', '3:56', '2008-09-12', '00007');
INSERT INTO Songs VALUES ('10039', 'Blank Space', '3:51', '2014-11-10', '00007');
INSERT INTO Songs VALUES ('10040', 'You Belong with Me', '3:52', '2009-04-18', '00007');
INSERT INTO Songs VALUES ('10041', 'We Are Never Ever Getting Back Together', '3:13', '2012-08-13', '00007');
INSERT INTO Songs VALUES ('10042', 'Bad Blood', '3:19', '2015-05-17', '00007');

INSERT INTO Songs VALUES ('10043', 'HUMBLE.', '2:57', '2017-03-30', '00008');
INSERT INTO Songs VALUES ('10044', 'Alright', '3:39', '2015-06-30', '00008');
INSERT INTO Songs VALUES ('10045', 'DNA.', '3:05', '2017-04-14', '00008');
INSERT INTO Songs VALUES ('10046', 'Swimming Pools (Drank)', '3:40', '2012-07-31', '00008');
INSERT INTO Songs VALUES ('10047', 'LOYALTY.', '3:47', '2017-04-14', '00008');
INSERT INTO Songs VALUES ('10048', 'Love.', '3:33', '2017-04-14', '00008');

-- Genre
INSERT INTO mv_SongGenre VALUES('Soul', '10001');
INSERT INTO mv_SongGenre VALUES('Pop', '10002');
INSERT INTO mv_SongGenre VALUES('Pop', '10003');
INSERT INTO mv_SongGenre VALUES('Pop', '10004');
INSERT INTO mv_SongGenre VALUES('Pop', '10005');
INSERT INTO mv_SongGenre VALUES('Pop', '10006');

INSERT INTO mv_SongGenre VALUES('Pop', '10007');
INSERT INTO mv_SongGenre VALUES('Pop', '10008');
INSERT INTO mv_SongGenre VALUES('Pop', '10009');
INSERT INTO mv_SongGenre VALUES('Funk', '10010');
INSERT INTO mv_SongGenre VALUES('Pop', '10011');
INSERT INTO mv_SongGenre VALUES('Pop', '10012');

INSERT INTO mv_SongGenre VALUES('Pop Rock', '10013');
INSERT INTO mv_SongGenre VALUES('Alternative Rock', '10014');
INSERT INTO mv_SongGenre VALUES('Alternative Rock', '10015');
INSERT INTO mv_SongGenre VALUES('Alternative Rock', '10016');
INSERT INTO mv_SongGenre VALUES('Alternative Rock', '10017');
INSERT INTO mv_SongGenre VALUES('Alternative Rock', '10018');

INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10019');
INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10020');
INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10021');
INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10022');
INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10023');
INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10024');

INSERT INTO mv_SongGenre VALUES('Pop', '10025');
INSERT INTO mv_SongGenre VALUES('Pop', '10026');
INSERT INTO mv_SongGenre VALUES('Pop', '10027');
INSERT INTO mv_SongGenre VALUES('Pop', '10028');
INSERT INTO mv_SongGenre VALUES('Pop', '10029');
INSERT INTO mv_SongGenre VALUES('Folk', '10030');

INSERT INTO mv_SongGenre VALUES('R&B', '10031');
INSERT INTO mv_SongGenre VALUES('R&B', '10032');
INSERT INTO mv_SongGenre VALUES('R&B', '10033');
INSERT INTO mv_SongGenre VALUES('R&B', '10034');
INSERT INTO mv_SongGenre VALUES('R&B', '10035');
INSERT INTO mv_SongGenre VALUES('Pop', '10036');

INSERT INTO mv_SongGenre VALUES('Pop', '10037');
INSERT INTO mv_SongGenre VALUES('Country Pop', '10038');
INSERT INTO mv_SongGenre VALUES('Pop', '10039');
INSERT INTO mv_SongGenre VALUES('Country Pop', '10040');
INSERT INTO mv_SongGenre VALUES('Pop', '10041');
INSERT INTO mv_SongGenre VALUES('Pop', '10042');

INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10043');
INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10044');
INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10045');
INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10046');
INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10047');
INSERT INTO mv_SongGenre VALUES('Hip-Hop', '10048');

-- Playlists
INSERT INTO Playlist VALUES(11111, 'SaturdayFun', '67891');
INSERT INTO Playlist VALUES(11112, 'IAmSad', '83591');
INSERT INTO Playlist VALUES(11113, 'MusicForBoat', '12345');
INSERT INTO Playlist VALUES(11114, 'HomeWork', '13578');
INSERT INTO Playlist VALUES(11115, 'Jogging', '19246');

-- Chart
INSERT INTO Chart VALUES ('Top 10 Global Songs', CURRENT_DATE);
INSERT INTO Chart VALUES ('Top 5 Pop', CURRENT_DATE);
INSERT INTO Chart VALUES ('Best of Taylor Swift', CURRENT_DATE);

-- re_chartsongs
INSERT INTO re_chartsongs VALUES ('10025', 'Top 10 Global Songs', 1);
INSERT INTO re_chartsongs VALUES ('10001', 'Top 10 Global Songs', 2);
INSERT INTO re_chartsongs VALUES ('10007', 'Top 10 Global Songs', 3);

INSERT INTO re_chartsongs VALUES ('10025', 'Top 5 Pop', 1);
INSERT INTO re_chartsongs VALUES ('10007', 'Top 5 Pop', 2);
INSERT INTO re_chartsongs VALUES ('10039', 'Top 5 Pop', 3);
INSERT INTO re_chartsongs VALUES ('10040', 'Top 5 Pop', 4);
INSERT INTO re_chartsongs VALUES ('10027', 'Top 5 Pop', 5);

INSERT INTO re_chartsongs VALUES ('10037', 'Best of Taylor Swift', 1);
INSERT INTO re_chartsongs VALUES ('10038', 'Best of Taylor Swift', 2);

-- re_catalogues
INSERT INTO re_catalogues VALUES ('12345', '10025');  -- User: gabe, Song: Shape of You
INSERT INTO re_catalogues VALUES ('12345', '10032');  -- User: gabe, Song: Halo

INSERT INTO re_catalogues VALUES ('67891', '10037');  -- User: thomas, Song: Shake It Off
INSERT INTO re_catalogues VALUES ('67891', '10011');  -- User: thomas, Song: Treasure

INSERT INTO re_catalogues VALUES ('13578', '10016');  -- User: braedon, Song: Yellow
INSERT INTO re_catalogues VALUES ('13578', '10046');  -- User: braedon, Song: Swimming Pools (Drank)

INSERT INTO re_catalogues VALUES ('19246', '10003');  -- User: adam, Song: Hello
INSERT INTO re_catalogues VALUES ('19246', '10029');  -- User: adam, Song: Perfect

INSERT INTO re_catalogues VALUES ('83591', '10020');  -- User: haley, Song: God's Plan
INSERT INTO re_catalogues VALUES ('83591', '10044');  -- User: haley, Song: Alright

-- ur_follows
INSERT INTO ur_follows VALUES ('12345', '67891');  -- User: gabe follows thomas
INSERT INTO ur_follows VALUES ('12345', '83591');  -- User: gabe follows haley

INSERT INTO ur_follows VALUES ('67891', '13578');  -- User: thomas follows braedon
INSERT INTO ur_follows VALUES ('67891', '19246');  -- User: thomas follows adam

-- re_likes
INSERT INTO re_likes VALUES ('12345', '67891', '11111');  -- User: gabe likes thomas's playlist "SaturdayFun"
INSERT INTO re_likes VALUES ('12345', '67891', '11112');  -- User: gabe likes thomas's playlist "IAmSad"

INSERT INTO re_likes VALUES ('67891', '13578', '11114');  -- User: thomas likes braedon's playlist "HomeWork"
INSERT INTO re_likes VALUES ('67891', '13578', '11115');  -- User: thomas likes braedon's playlist "Jogging"

INSERT INTO re_likes VALUES ('83591', '19246', '11113');  -- User: haley likes adam's playlist "MusicForBoat"
INSERT INTO re_likes VALUES ('83591', '19246', '11114');  -- User: haley likes adam's playlist "HomeWork"

-- re-has
INSERT INTO re_has VALUES ('11111', '10008'); -- Bruno Mars - Locked Out of Heaven
INSERT INTO re_has VALUES ('11111', '10010'); -- Bruno Mars - Uptown Funk
INSERT INTO re_has VALUES ('11111', '10019'); -- Drake - Hotline Bling

INSERT INTO re_has VALUES ('11112', '10002'); -- Adele - Someone Like You
INSERT INTO re_has VALUES ('11112', '10011'); -- Bruno Mars - Treasure
INSERT INTO re_has VALUES ('11112', '10036'); -- Beyonce - Formation

INSERT INTO re_has VALUES ('11113', '10005'); -- Adele - Skyfall
INSERT INTO re_has VALUES ('11113', '10017'); -- Coldplay - Paradise
INSERT INTO re_has VALUES ('11113', '10034'); -- Beyonce - Drunk in Love

INSERT INTO re_has VALUES ('11114', '10004'); -- Adele - Set Fire to the Rain
INSERT INTO re_has VALUES ('11114', '10014'); -- Coldplay - Fix You
INSERT INTO re_has VALUES ('11114', '10041'); -- Taylor Swift - We Are Never Ever Getting Back Together

INSERT INTO re_has VALUES ('11115', '10003'); -- Adele - Hello
INSERT INTO re_has VALUES ('11115', '10012'); -- Bruno Mars - 24K Magic
INSERT INTO re_has VALUES ('11115', '10029'); -- Ed Sheeran - Perfect

-- re_makes
INSERT INTO Songs (songID, songName, songLength, releaseDate, artistID) VALUES ('10049', 'Midnight Sadness', '3:00', '2024-04-29', NULL);
INSERT INTO Songs (songID, songName, songLength, releaseDate, artistID) VALUES ('10050', 'Starlit Diamond', '2:80', '2024-04-29', NULL);
INSERT INTO Songs (songID, songName, songLength, releaseDate, artistID) VALUES ('10051', 'Moonlight With You', '3:20', '2024-04-29', NULL);

INSERT INTO re_makes (songID, artistID) VALUES ('10049', '00001');
INSERT INTO re_makes (songID, artistID) VALUES ('10050', '00002'); 
INSERT INTO re_makes (songID, artistID) VALUES ('10051', '00001');

-- re_chartartists
INSERT INTO Chart (chartName) VALUES ('Top Artists');

INSERT INTO re_chartartists VALUES ('00001', 'Top Artists', 1); -- Adele
INSERT INTO re_chartartists VALUES ('00002', 'Top Artists', 2); -- Bruno Mars
INSERT INTO re_chartartists VALUES ('00003', 'Top Artists', 3); -- Coldplay
INSERT INTO re_chartartists VALUES ('00008', 'Top Artists', 4); -- kendrick
INSERT INTO re_chartartists VALUES ('00005', 'Top Artists', 5); -- Ed Sheeran
INSERT INTO re_chartartists VALUES ('00004', 'Top Artists', 6); -- drake
INSERT INTO re_chartartists VALUES ('00007', 'Top Artists', 7); -- taylor
INSERT INTO re_chartartists VALUES ('00006', 'Top Artists', 8); -- beyonce
