-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 18, 2023 at 05:50 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cardia`
--

-- --------------------------------------------------------

--
-- Table structure for table `patient_detail`
--

CREATE TABLE `patient_detail` (
  `patient_id` int(5) NOT NULL,
  `patient_name` varchar(40) NOT NULL,
  `phone` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `age` varchar(40) NOT NULL,
  `gender` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient_detail`
--

INSERT INTO `patient_detail` (`patient_id`, `patient_name`, `phone`, `email`, `address`, `age`, `gender`, `password`, `created_at`) VALUES
(1, 'Ranveer', '6381268719', 'prq@gmail.com', 'MTM', '12', 'Male', '12345', '2023-11-26 09:10:38'),
(2, 'Ranvir', '6381268719', 'ranveer@gmail.com', 'Mumbai, India', '56', 'Male', '12345', '2023-12-18 16:47:40');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `patient_detail`
--
ALTER TABLE `patient_detail`
  ADD PRIMARY KEY (`patient_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `patient_detail`
--
ALTER TABLE `patient_detail`
  MODIFY `patient_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
