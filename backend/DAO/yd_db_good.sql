-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : dim. 16 jan. 2022 à 09:41
-- Version du serveur :  10.4.18-MariaDB
-- Version de PHP : 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `yd_db1`
--

-- --------------------------------------------------------

--
-- Structure de la table `admin`
--

CREATE TABLE `admin` (
  `id_admin` int(11) NOT NULL,
  `id_user` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `expert`
--

CREATE TABLE `expert` (
  `id_expert` int(11) NOT NULL,
  `learner_id_learner` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `learner`
--

CREATE TABLE `learner` (
  `id_learner` int(11) NOT NULL,
  `expert_id_expert` int(11) DEFAULT NULL,
  `id_user` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `lesson`
--

CREATE TABLE `lesson` (
  `id_lesson` int(11) NOT NULL,
  `titre_Syllabus` varchar(50) DEFAULT NULL,
  `id_Syllabus` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `syllabus`
--

CREATE TABLE `syllabus` (
  `id_Syllabus` int(11) NOT NULL,
  `titre_Syllabus` varchar(50) DEFAULT NULL,
  `id_expert` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id_user` int(11) NOT NULL,
  `name_user` varchar(50) DEFAULT NULL,
  `email_user` varchar(50) DEFAULT NULL,
  `photo_user` varchar(50) DEFAULT NULL,
  `phone_user` varchar(15) DEFAULT NULL,
  `password_user` varchar(50) DEFAULT NULL,
  `gender_user` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `video`
--

CREATE TABLE `video` (
  `id_video` varchar(50) NOT NULL,
  `titre_video` varchar(50) DEFAULT NULL,
  `viewCount_video` int(11) DEFAULT NULL,
  `description_video` text DEFAULT NULL,
  `published_at_video` varchar(50) DEFAULT NULL,
  `thumbnails_video` varchar(50) DEFAULT NULL,
  `channel_id_video` varchar(50) DEFAULT NULL,
  `id_lesson` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id_admin`);

--
-- Index pour la table `expert`
--
ALTER TABLE `expert`
  ADD PRIMARY KEY (`id_expert`);

--
-- Index pour la table `learner`
--
ALTER TABLE `learner`
  ADD PRIMARY KEY (`id_learner`);

--
-- Index pour la table `lesson`
--
ALTER TABLE `lesson`
  ADD PRIMARY KEY (`id_lesson`),
  ADD KEY `FK_lesson_id_Syllabus` (`id_Syllabus`);

--
-- Index pour la table `syllabus`
--
ALTER TABLE `syllabus`
  ADD PRIMARY KEY (`id_Syllabus`),
  ADD KEY `FK_syllabus_id_expert` (`id_expert`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`);

--
-- Index pour la table `video`
--
ALTER TABLE `video`
  ADD PRIMARY KEY (`id_video`),
  ADD KEY `FK_video_id_lesson` (`id_lesson`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `admin`
--
ALTER TABLE `admin`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `expert`
--
ALTER TABLE `expert`
  MODIFY `id_expert` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `learner`
--
ALTER TABLE `learner`
  MODIFY `id_learner` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `lesson`
--
ALTER TABLE `lesson`
  MODIFY `id_lesson` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `syllabus`
--
ALTER TABLE `syllabus`
  MODIFY `id_Syllabus` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `lesson`
--
ALTER TABLE `lesson`
  ADD CONSTRAINT `FK_lesson_id_Syllabus` FOREIGN KEY (`id_Syllabus`) REFERENCES `syllabus` (`id_Syllabus`);

--
-- Contraintes pour la table `syllabus`
--
ALTER TABLE `syllabus`
  ADD CONSTRAINT `FK_syllabus_id_expert` FOREIGN KEY (`id_expert`) REFERENCES `expert` (`id_expert`);

--
-- Contraintes pour la table `video`
--
ALTER TABLE `video`
  ADD CONSTRAINT `FK_video_id_lesson` FOREIGN KEY (`id_lesson`) REFERENCES `lesson` (`id_lesson`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
