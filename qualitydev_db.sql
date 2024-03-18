-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Mar 18, 2024 alle 20:18
-- Versione del server: 10.4.28-MariaDB
-- Versione PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qualitydev_db`
--
CREATE DATABASE IF NOT EXISTS `qualitydev_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `qualitydev_db`;

-- --------------------------------------------------------

--
-- Struttura della tabella `max_seats_time_slot`
--

CREATE TABLE `max_seats_time_slot` (
  `id` int(11) NOT NULL,
  `time_slot` enum('20:00','21:00','22:00') NOT NULL,
  `max_seats` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `max_seats_time_slot`
--

INSERT INTO `max_seats_time_slot` (`id`, `time_slot`, `max_seats`) VALUES
(1, '20:00', 10),
(2, '21:00', 10),
(3, '22:00', 10);

-- --------------------------------------------------------

--
-- Struttura della tabella `prenotazioni`
--

CREATE TABLE `prenotazioni` (
  `id` int(11) NOT NULL,
  `id_user` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `reserved_seats` int(11) NOT NULL,
  `day` date NOT NULL,
  `time_slot` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `prenotazioni`
--

INSERT INTO `prenotazioni` (`id`, `id_user`, `name`, `phone`, `reserved_seats`, `day`, `time_slot`) VALUES
(4, '179375623', 'Giuseppe', '3214567394', 4, '2024-03-18', 1),
(5, '197091213', 'Famiglia Brambilla', '095462431', 7, '2024-03-19', 1);

--
-- Trigger `prenotazioni`
--
DELIMITER $$
CREATE TRIGGER `before_delete_prenotazioni` BEFORE DELETE ON `prenotazioni` FOR EACH ROW BEGIN
    DECLARE days date;
    SELECT COUNT(*) INTO days
    FROM seats_occupation
    WHERE day < CURDATE();

    -- Controlla se ci sono abbastanza posti disponibili nella nuova fascia oraria
    IF CURDATE() < days THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Non ci sono prenotazioni da eliminare';
    ELSE
        -- Aggiorna il numero di posti occupati nella tabella seats_occupation per la nuova fascia oraria
        DELETE FROM seats_occupation
        WHERE day < CURDATE();
    END IF;  
    -- Aggiorna il numero di posti occupati nella tabella seats_occupation per la fascia oraria da cancellare
    UPDATE seats_occupation
    SET free_seats = free_seats + OLD.reserved_seats
    WHERE time_slot = OLD.time_slot AND day = OLD.day;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `before_insert_prenotazioni` BEFORE INSERT ON `prenotazioni` FOR EACH ROW BEGIN

    DECLARE free_seat INT;
    DECLARE days date;
    SELECT COUNT(*) INTO days
    FROM seats_occupation
    WHERE day < CURDATE();

    -- Controlla se ci sono abbastanza posti disponibili nella nuova fascia oraria
    IF CURDATE() < days THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Non ci sono prenotazioni da eliminare';
    ELSE
        -- Aggiorna il numero di posti occupati nella tabella seats_occupation per la nuova fascia oraria
        DELETE FROM seats_occupation
        WHERE day < CURDATE();
    END IF;  
    SELECT free_seats INTO free_seat
    FROM seats_occupation
    WHERE time_slot = NEW.time_slot and day = NEW.day;

    -- Controlla se ci sono abbastanza posti disponibili
    IF (free_seat - NEW.reserved_seats) < 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Non ci sono abbastanza posti disponibili per questa fascia oraria';
    ELSE
        -- Aggiorna il numero di posti occupati nella tabella seats_occupation
        
        UPDATE seats_occupation
        SET free_seats = free_seats - NEW.reserved_seats
        WHERE time_slot = NEW.time_slot AND day = NEW.day;
    END IF;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `before_update_prenotazioni` BEFORE UPDATE ON `prenotazioni` FOR EACH ROW BEGIN
    DECLARE days date;
    SELECT COUNT(*) INTO days
    FROM seats_occupation
    WHERE day < CURDATE();

    -- Controlla se ci sono abbastanza posti disponibili nella nuova fascia oraria
    IF CURDATE() < days THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Non ci sono prenotazioni da eliminare';
    ELSE
        -- Aggiorna il numero di posti occupati nella tabella seats_occupation per la nuova fascia oraria
        DELETE FROM seats_occupation
        WHERE day < CURDATE();
    END IF;  
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Struttura della tabella `seats_occupation`
--

CREATE TABLE `seats_occupation` (
  `id` int(11) NOT NULL,
  `day` varchar(20) NOT NULL,
  `time_slot` int(11) NOT NULL,
  `free_seats` int(11) NOT NULL DEFAULT 10
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dump dei dati per la tabella `seats_occupation`
--

INSERT INTO `seats_occupation` (`id`, `day`, `time_slot`, `free_seats`) VALUES
(606, '2024-03-18', 1, 6),
(607, '2024-03-18', 2, 10),
(608, '2024-03-18', 3, 10),
(609, '2024-03-19', 1, 3),
(610, '2024-03-19', 2, 10),
(611, '2024-03-19', 3, 10);

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `max_seats_time_slot`
--
ALTER TABLE `max_seats_time_slot`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `prenotazioni`
--
ALTER TABLE `prenotazioni`
  ADD PRIMARY KEY (`id`);

--
-- Indici per le tabelle `seats_occupation`
--
ALTER TABLE `seats_occupation`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `max_seats_time_slot`
--
ALTER TABLE `max_seats_time_slot`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT per la tabella `prenotazioni`
--
ALTER TABLE `prenotazioni`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT per la tabella `seats_occupation`
--
ALTER TABLE `seats_occupation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=612;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
