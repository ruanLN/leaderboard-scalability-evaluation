DROP DATABASE IF EXISTS db; 
CREATE DATABASE IF NOT EXISTS db;
USE db;
CREATE  TABLE IF NOT EXISTS `leaderboard_control` (
  `leaderboard_id` INT AUTO_INCREMENT ,
  `status` INT NOT NULL  ,
  PRIMARY KEY (`leaderboard_id`) )
ENGINE = InnoDB;

CREATE  TABLE IF NOT EXISTS `leaderboards` (
  `leaderboard_id` INT ,
  `user_id` VARCHAR( 64 )  ,
  `score` INT NOT NULL  ,
  PRIMARY KEY (`leaderboard_id`, `user_id`) )
ENGINE = InnoDB;