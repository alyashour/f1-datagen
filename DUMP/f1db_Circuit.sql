CREATE DATABASE  IF NOT EXISTS `f1db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `f1db`;
-- MySQL dump 10.13  Distrib 8.0.40, for macos14 (arm64)
--
-- Host: localhost    Database: f1db
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Circuit`
--

DROP TABLE IF EXISTS `Circuit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Circuit` (
  `Circuit_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(255) NOT NULL,
  `Country` varchar(255) NOT NULL,
  PRIMARY KEY (`Circuit_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Circuit`
--

LOCK TABLES `Circuit` WRITE;
/*!40000 ALTER TABLE `Circuit` DISABLE KEYS */;
INSERT INTO `Circuit` VALUES (1,'Whole bank','Rwanda'),(2,'Environmental agent','Saint Lucia'),(3,'Short difficult','Seychelles'),(4,'Rest present TV','Panama'),(5,'Family behavior','Jordan'),(6,'Degree hour even','Myanmar'),(7,'Leader develop','Puerto Rico'),(8,'Method today under','Tokelau'),(9,'Year','United States of America'),(10,'Determine street green','Timor-Leste'),(11,'Call agency','Gibraltar'),(12,'At dream','Venezuela'),(13,'Along','Nauru'),(14,'Enter evening wear avoid','Cocos (Keeling) Islands'),(15,'Fill positive along','Moldova'),(16,'Glass issue floor','Kyrgyz Republic'),(17,'Size book provide','Malta'),(18,'Rate their different','Uganda'),(19,'Clearly design price','Barbados'),(20,'Floor visit school present','Grenada'),(21,'Foreign different past','Solomon Islands'),(22,'Article everything','Norway'),(23,'You next house','Thailand'),(24,'Where','Bermuda'),(25,'Star total same','Slovenia'),(26,'Feel traditional','Chad'),(27,'Natural show','Gabon'),(28,'It grow southern','Dominica'),(29,'Shoulder such mother','Greenland'),(30,'Cultural prevent authority','French Guiana'),(31,'Game owner him','Guinea'),(32,'Wish others','Somalia'),(33,'Other industry','Moldova'),(34,'Building industry top','Singapore'),(35,'Specific message','Malaysia'),(36,'Economy','Sierra Leone'),(37,'Wait exactly not','Martinique'),(38,'Relationship for','Qatar'),(39,'Understand form rate','Albania'),(40,'Population down','Guadeloupe'),(41,'Project onto collection pretty','Ukraine'),(42,'Nice next','Azerbaijan'),(43,'Success range','Tuvalu'),(44,'Kind try TV','Tonga'),(45,'Local middle','Vietnam'),(46,'Exist would student','Botswana'),(47,'State real state','Zimbabwe'),(48,'Feeling audience','Benin'),(49,'Coach wonder along','Sweden'),(50,'Physical against amount instead','Marshall Islands'),(51,'Born bar','Netherlands'),(52,'Even direction','Svalbard & Jan Mayen Islands'),(53,'Table manager forget','Christmas Island'),(54,'Party strategy','Malta'),(55,'Probably white responsibility','Lesotho'),(56,'Care avoid','Montenegro'),(57,'Authority blood','Nepal'),(58,'Public price','South Georgia and the South Sandwich Islands'),(59,'The give unit','Saint Lucia'),(60,'Long generation here need','Indonesia'),(61,'However season','Mauritius'),(62,'Travel plant many','South Africa'),(63,'Attention along','Togo'),(64,'Born fight story','Myanmar'),(65,'Throughout level information','Morocco'),(66,'Voice success','Congo'),(67,'Pass would','Rwanda'),(68,'Four present','Mauritius'),(69,'Mention prepare term','Yemen'),(70,'Instead system','Turks and Caicos Islands'),(71,'Serious during','Isle of Man'),(72,'Spring follow','Serbia'),(73,'Responsibility far','Central African Republic'),(74,'Box happy','Germany'),(75,'Cost detail just','Equatorial Guinea'),(76,'Popular quite','Togo'),(77,'Factor step during','Colombia'),(78,'Notice main a','Australia'),(79,'Worry finish','Falkland Islands (Malvinas)'),(80,'Teacher rule political','Netherlands'),(81,'Outside Republican civil','Panama'),(82,'Note include soon','Australia'),(83,'When peace ask','Nepal'),(84,'Resource child contain','Sri Lanka'),(85,'Finally reveal college','Sweden'),(86,'Trial often create ability','Cocos (Keeling) Islands'),(87,'Although western anything','Wallis and Futuna'),(88,'Heart necessary','Brunei Darussalam'),(89,'Approach seem','Thailand'),(90,'Fall better board','Jamaica'),(91,'Customer local','United Kingdom'),(92,'Here pattern','Italy'),(93,'Woman never agency','Saint Martin'),(94,'Article contain','Paraguay'),(95,'Mission improve','Kiribati'),(96,'Part discuss lot','Australia'),(97,'Man produce','Taiwan'),(98,'Finish against your','Tonga'),(99,'Customer treat wait','Sri Lanka'),(100,'No himself level management','Japan');
/*!40000 ALTER TABLE `Circuit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-22 23:19:29
