-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3307:3306
-- Generation Time: Oct 24, 2023 at 08:40 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fbx-api`
--

-- --------------------------------------------------------

--
-- Table structure for table `locations`
--

CREATE TABLE `locations` (
  `Location_ID` int(11) NOT NULL,
  `Location_Name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `locations`
--

INSERT INTO `locations` (`Location_ID`, `Location_Name`) VALUES
(1, 'KMITL'),
(2, 'KMUTT'),
(3, 'KMUNB'),
(4, 'CU'),
(5, 'TU'),
(6, 'BU'),
(7, 'PSU');

-- --------------------------------------------------------

--
-- Table structure for table `post`
--

CREATE TABLE `post` (
  `Post_ID` int(11) NOT NULL,
  `User_ID` int(11) NOT NULL,
  `Location_ID` int(11) NOT NULL,
  `Post_Content` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `post`
--

INSERT INTO `post` (`Post_ID`, `User_ID`, `Location_ID`, `Post_Content`) VALUES
(6, 1, 1, 'ไปกินข้าวกัน'),
(7, 2, 4, 'ไปกินข้าวกัน'),
(8, 1, 4, 'ไปกินข้าวกัน'),
(9, 1, 4, 'ไปกินข้าวกัน'),
(10, 2, 4, 'ไปกินข้าวกัน'),
(11, 5, 4, 'ไปกินข้าวกัน');

-- --------------------------------------------------------

--
-- Table structure for table `tag_freinds`
--

CREATE TABLE `tag_freinds` (
  `Friend_ID` int(11) NOT NULL,
  `Post_ID` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `tag_freinds`
--

INSERT INTO `tag_freinds` (`Friend_ID`, `Post_ID`) VALUES
(2, 6),
(3, 6),
(1, 7),
(4, 7),
(5, 7),
(2, 8),
(4, 8),
(5, 8),
(3, 9),
(4, 9),
(5, 9),
(3, 10),
(4, 10),
(5, 10),
(3, 11),
(4, 11),
(1, 11);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `User_ID` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` int(50) NOT NULL,
  `Email` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`User_ID`, `Username`, `Password`, `Email`) VALUES
(1, 'Wanburhan Wae-Useng', 1234, 'a@g.com'),
(2, 'Pumipat lalun', 1234, 'b@g.com'),
(3, 'Narunart Tuntue', 1234, 'c@g.com'),
(4, 'Jaruphat kenphom', 1234, 'd@g.com'),
(5, 'Chanakan Senee', 1234, 'e@g.com'),
(6, 'Ronnawit Muankeaw', 1234, 'f@g.com');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `locations`
--
ALTER TABLE `locations`
  ADD PRIMARY KEY (`Location_ID`);

--
-- Indexes for table `post`
--
ALTER TABLE `post`
  ADD PRIMARY KEY (`Post_ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`User_ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `locations`
--
ALTER TABLE `locations`
  MODIFY `Location_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `post`
--
ALTER TABLE `post`
  MODIFY `Post_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `User_ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
