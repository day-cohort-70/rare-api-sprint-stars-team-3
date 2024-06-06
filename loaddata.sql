CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" VARCHAR,
  "last_name" VARCHAR,
  "email" VARCHAR,
  "bio" VARCHAR,
  "username" VARCHAR,
  "password" VARCHAR,
  "profile_image_url" VARCHAR,
  "created_on" date,
  "is_active" INTEGER
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" CURRENT_DATE,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" VARCHAR,
  "publication_date" date,
  "image_url" VARCHAR,
  "content" VARCHAR,
  "approved" bit,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" VARCHAR,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" VARCHAR
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" VARCHAR
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" VARCHAR
);

INSERT INTO Categories(label) VALUES ('News'),('Science');
INSERT INTO Tags (label) VALUES ('JavaScript');
INSERT INTO Reactions (label, image_url) VALUES ('happy', 'https://pngtree.com/so/happy');


INSERT INTO Categories (label) VALUES ('Technology'), ('Entertainment');
INSERT INTO Tags (label) VALUES ('#programming'), ('#coding'), ('#webdev');
INSERT INTO Reactions (label, image_url) VALUES ('Like', 'http://example.com/like.png'), ('Dislike', 'http://example.com/dislike.png');

-- Insert initial data into Users table
INSERT INTO Users (first_name, last_name, email, bio, username, password, profile_image_url, created_on, is_active)
VALUES
('John', 'Doe', 'john.doe@example.com', 'Software Engineer', 'johndoe', 'password123', 'http://example.com/johndoe.jpg', '2024-05-29', 1),
('Jane', 'Doe', 'jane.doe@example.com', 'Web Developer', 'janedoe', 'password456', 'http://example.com/janedoe.jpg', '2024-05-28', 1),
('Alice', 'Smith', 'alice.smith@example.com', 'UI Designer', 'alismit', 'password789', 'http://example.com/alice-smith.jpg', '2024-05-27', 1);

-- Insert initial data into Posts table
INSERT INTO Posts (user_id, category_id, title, publication_date, image_url, content, approved)
VALUES
(1, 1, 'Introduction to Web Development', '2024-06-01', 'http://example.com/intro-web-dev.jpg', 'A comprehensive guide to web development.', 1),
(2, 2, 'Learning JavaScript', '2024-06-02', 'http://example.com/javascript-guide.jpg', 'Master the basics of JavaScript.', 1),
(3, 3, 'Design Principles for Beginners', '2024-06-03', 'http://example.com/design-principles.jpg', 'Understand the fundamentals of design.', 1);

-- Insert initial data into Comments table
INSERT INTO Comments (post_id, author_id, content)
VALUES
(1, 2, 'Great introduction'),
(2, 1, 'Ive been waiting for this guide.'),
(1, 2, 'Master the basics of JavaScript.'),
(3, 2, 'Great introduction');


INSERT INTO PostTags (post_id, tag_id)
VALUES
(1, 1), -- Assuming post with id 1 has tag with id 1
(2, 2), -- Assuming post with id 2 has tag with id 2
(3, 3); -- Assuming post with id 3 has tag with id 3

DELETE FROM Posts WHERE id = 1;
DELETE FROM Posts WHERE id = 2;
DELETE FROM Posts WHERE id = 3;
INSERT INTO Posts (user_id, category_id, title, publication_date, image_url, content, approved)
VALUES
(1, 4, 'Introduction to Web Development', '2024-06-01', 'https://sklc-tinymce-2021.s3.amazonaws.com/comp/2023/02/179_1675948994.png', 'A comprehensive guide to web development.', 1),
(2, 4, 'Learning JavaScript', '2024-06-02', 'https://sllearnenginedev.blob.core.windows.net/material-images/95433922af1f4ecb996b9a6dd502b5c5-JS_1.png', 'Master the basics of JavaScript.', 1),
(1, 4, 'Design Principles for Beginners', '2024-06-03', 'https://saigontechnology.com/assets/media/software-development-process-models.png', 'Understand the fundamentals of design.', 1),
(1, 1, 'How to accelerate software development with generative AI', '2024-08-01', 'https://datasciencedojo.com/wp-content/uploads/Generative-AI-roadmap-1030x1030.jpg', 'Generative AI tools can significantly improve software developers productivity on common tasks.', 1),
(1, 4, 'Thomas Dohmke on improving engineering experience using generative AI', '2024-02-01', 'https://www1.onpassive.com/blog/wp-content/uploads/2022/11/11160344/AI-powered-software-development-768x768.jpg', 'A Look At Artificial Intelligences Role In Software Development.', 1),
(2, 4, 'Introduction to Web Development', '2024-06-01', 'https://sklc-tinymce-2021.s3.amazonaws.com/comp/2023/02/179_1675948994.png', 'A comprehensive guide to web development.', 1),
(2, 4, 'Learning JavaScript', '2024-06-02', 'https://sllearnenginedev.blob.core.windows.net/material-images/95433922af1f4ecb996b9a6dd502b5c5-JS_1.png', 'Master the basics of JavaScript.', 1);












-- Delete items from the database
-- DELETE FROM Users
-- WHERE id BETWEEN 11 AND 15;