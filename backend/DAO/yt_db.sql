DROP TABLE IF EXISTS syllabus ;
CREATE TABLE syllabus (id_Syllabus INT AUTO_INCREMENT NOT NULL,
titre_Syllabus VARCHAR(50),
id_expert INT,
PRIMARY KEY (id_Syllabus)) ENGINE=InnoDB;

DROP TABLE IF EXISTS lesson ;
CREATE TABLE lesson (id_lesson INT AUTO_INCREMENT NOT NULL,
titre_Syllabus VARCHAR(50),
id_Syllabus INT,
PRIMARY KEY (id_lesson)) ENGINE=InnoDB;

DROP TABLE IF EXISTS video ;
CREATE TABLE video (id_video VARCHAR(50) NOT NULL,
titre_video VARCHAR(50),
viewCount_video INT,
description_video TEXT,
published_at_video VARCHAR(50),
thumbnails_video VARCHAR(50),
channel_id_video VARCHAR(50),
id_lesson INT,
PRIMARY KEY (id_video)) ENGINE=InnoDB;

DROP TABLE IF EXISTS users ;
CREATE TABLE users (id_user INT AUTO_INCREMENT NOT NULL,
name_user VARCHAR(50),
email_user VARCHAR(50),
photo_user VARCHAR(50),
phone_user VARCHAR(15),
password_user VARCHAR(50),
gender_user CHAR(1),
PRIMARY KEY (id_user)),CREATE INDEX idx_user
ON users (id_user); ENGINE=InnoDB;

DROP TABLE IF EXISTS admin ;
CREATE TABLE admin (id_admin INT AUTO_INCREMENT NOT NULL,
id_user INT,
PRIMARY KEY (id_admin)) ENGINE=InnoDB;

DROP TABLE IF EXISTS learner ;
CREATE TABLE learner (id_learner INT AUTO_INCREMENT NOT NULL,
expert_id_expert INT,
id_user INT,
PRIMARY KEY (id_learner)) ENGINE=InnoDB;

DROP TABLE IF EXISTS expert ;
CREATE TABLE expert (id_expert INT AUTO_INCREMENT NOT NULL,
learner_id_learner INT,
PRIMARY KEY (id_expert)) ENGINE=InnoDB;

ALTER TABLE syllabus ADD CONSTRAINT FK_syllabus_id_expert FOREIGN KEY (id_expert) REFERENCES expert (id_expert);
ALTER TABLE lesson ADD CONSTRAINT FK_lesson_id_Syllabus FOREIGN KEY (id_Syllabus) REFERENCES syllabus (id_Syllabus);
ALTER TABLE video ADD CONSTRAINT FK_video_id_lesson FOREIGN KEY (id_lesson) REFERENCES lesson (id_lesson);
ALTER TABLE admin ADD CONSTRAINT FK_admin_id_user FOREIGN KEY (id_user) REFERENCES user (id_user);
ALTER TABLE learner ADD CONSTRAINT FK_learner_expert_id_expert FOREIGN KEY (expert_id_expert) REFERENCES expert (id_expert);
ALTER TABLE learner ADD CONSTRAINT FK_learner_id_user FOREIGN KEY (id_user) REFERENCES user (id_user);
ALTER TABLE expert ADD CONSTRAINT FK_expert_learner_id_learner FOREIGN KEY (learner_id_learner) REFERENCES learner (id_learner);

