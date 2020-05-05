-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 05, 2020 at 02:31 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `blockchain_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `blockchain_final`
--

CREATE TABLE `blockchain_final` (
  `id` int(11) NOT NULL,
  `prevHash` varchar(256) NOT NULL,
  `data` varchar(256) NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `hash` varchar(256) NOT NULL,
  `nonce` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blockchain_final`
--

INSERT INTO `blockchain_final` (`id`, `prevHash`, `data`, `time`, `hash`, `nonce`) VALUES
(0, '0', 'Genesis', '2020-05-04 21:43:33', '0', 0),
(1, '0', 'test_data1', '2020-05-05 00:21:03', '89865a5570113e7873eab13db4b91bf14d50602350c258516d1216f7ffb6c634', 274529),
(2, '89865a5570113e7873eab13db4b91bf14d50602350c258516d1216f7ffb6c634', 'test_data2', '2020-05-05 00:21:09', '03af015057902d82de353c683fbeec7b04b1baf406a1223d4de4af6e2f9b0757', 10588),
(3, '03af015057902d82de353c683fbeec7b04b1baf406a1223d4de4af6e2f9b0757', 'test_data3', '2020-05-05 00:21:20', 'c6a701d16df09c4514dbad9ee46e0b2bd1a2f4b1896d42330bee8916edaf6061', 140663),
(4, 'c6a701d16df09c4514dbad9ee46e0b2bd1a2f4b1896d42330bee8916edaf6061', 'test_data4', '2020-05-05 00:21:27', '60c267901b69cd2b112ada8268e5fbc48082da76719c53ec3705f195f3d68829', 98666);

-- --------------------------------------------------------

--
-- Table structure for table `data_entry`
--

CREATE TABLE `data_entry` (
  `id` int(10) NOT NULL,
  `data` varchar(11) NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `data_pool`
--

CREATE TABLE `data_pool` (
  `id` int(11) NOT NULL,
  `prevHash` varchar(256) NOT NULL,
  `data` varchar(256) NOT NULL,
  `time` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `hash` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `data_pool`
--

INSERT INTO `data_pool` (`id`, `prevHash`, `data`, `time`, `hash`) VALUES
(5, '60c267901b69cd2b112ada8268e5fbc48082da76719c53ec3705f195f3d68829', 'test_data5', '2020-05-05 00:30:11', '469ac1e39bf80cea356ccb8b8194f936f963293aab04ce9f636232a926edcbb9'),
(6, '469ac1e39bf80cea356ccb8b8194f936f963293aab04ce9f636232a926edcbb9', 'test_data6', '2020-05-05 00:30:20', '9043e638d7b45bffa5a5936d083bb04db9c8972dfab624e3017b82b444f0ce49');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blockchain_final`
--
ALTER TABLE `blockchain_final`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `data_entry`
--
ALTER TABLE `data_entry`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `data_pool`
--
ALTER TABLE `data_pool`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blockchain_final`
--
ALTER TABLE `blockchain_final`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `data_entry`
--
ALTER TABLE `data_entry`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT for table `data_pool`
--
ALTER TABLE `data_pool`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
